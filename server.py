# -*- coding: utf-8 -*-
import os
import json
import stripe
import gspread
from datetime import datetime
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

from dotenv import load_dotenv

load_dotenv()
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

# Initialize gspread
try:
    gc = gspread.service_account(filename='credentials.json')
    # Open the sheet by title
    sheet = gc.open('Onle last time web traffic').sheet1
    print("Google Sheets connected successfully.")
except Exception as e:
    print(f"Warning: Could not connect to Google Sheets. Check credentials.json and sharing permissions. Error: {e}")
    sheet = None

class BackendServer(SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        parsed_path = urlparse(self.path)
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data) if post_data else {}
            
            if parsed_path.path == '/create-payment-intent':
                intent = stripe.PaymentIntent.create(
                    amount=3500,
                    currency='eur',
                    automatic_payment_methods={
                        'enabled': True,
                    },
                    metadata={
                        'deliveryMode': data.get('deliveryMode'),
                    }
                )
                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'clientSecret': intent.client_secret}).encode('utf-8'))
                
            elif parsed_path.path == '/api/waitlist':
                email = data.get('email')
                if sheet and email:
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    sheet.append_row([now, "WAITLIST", email, "N/A", "N/A"])
                
                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'ok'}).encode('utf-8'))
                
            elif parsed_path.path == '/api/track':
                events = data.get('events', [])
                if sheet and events:
                    rows_to_insert = []
                    for ev in events:
                        rows_to_insert.append([
                            ev.get('timestamp', datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                            ev.get('sessionId', 'unknown'),
                            ev.get('page', 'unknown'),
                            ev.get('event', 'unknown'),
                            ev.get('details', ''),
                            ev.get('scroll', ''),
                            ev.get('timeSpent', '')
                        ])
                    sheet.append_rows(rows_to_insert)
                
                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'ok'}).encode('utf-8'))
                
            else:
                self.send_response(404)
                self.end_headers()
                
        except Exception as e:
            self.send_response(400)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))

if __name__ == '__main__':
    port = 8003
    print(f"Starting Backend API server on port {port}...")
    httpd = HTTPServer(('localhost', port), BackendServer)
    httpd.serve_forever()
