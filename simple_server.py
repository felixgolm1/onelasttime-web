import http.server
import socketserver
import sys

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
httpd = socketserver.TCPServer(("", port), Handler)
print(f"Serving on port {port}")
httpd.serve_forever()
