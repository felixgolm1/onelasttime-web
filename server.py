import http.server
import socketserver
import os
import re

class RangeRequestHandler(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        if 'Range' not in self.headers:
            return super().send_head()
        
        try:
            path = self.translate_path(self.path)
            f = open(path, 'rb')
        except OSError:
            self.send_error(404, "File not found")
            return None
        
        fs = os.fstat(f.fileno())
        size = int(fs.st_size)
        
        range_header = self.headers.get('Range')
        match = re.search(r'bytes=(\d+)-(\d*)', range_header)
        
        if not match:
            self.send_error(400, "Bad Request")
            return None
            
        first_byte = int(match.group(1))
        last_byte = int(match.group(2)) if match.group(2) else size - 1
        
        if first_byte >= size or last_byte >= size:
            self.send_error(416, "Requested Range Not Satisfiable")
            self.send_header("Content-Range", f"bytes */{size}")
            self.end_headers()
            return None
            
        length = last_byte - first_byte + 1
        
        self.send_response(206)
        self.send_header("Content-type", self.guess_type(path))
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Range", f"bytes {first_byte}-{last_byte}/{size}")
        self.send_header("Content-Length", str(length))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        
        return f

    def copyfile(self, source, outputfile):
        if 'Range' not in self.headers:
            super().copyfile(source, outputfile)
            return
            
        range_header = self.headers.get('Range')
        match = re.search(r'bytes=(\d+)-(\d*)', range_header)
        if not match:
            return
            
        first_byte = int(match.group(1))
        fs = os.fstat(source.fileno())
        size = int(fs.st_size)
        last_byte = int(match.group(2)) if match.group(2) else size - 1
        
        length = last_byte - first_byte + 1
        source.seek(first_byte)
        
        chunk_size = 64 * 1024
        while length > 0:
            chunk = source.read(min(length, chunk_size))
            if not chunk:
                break
            try:
                outputfile.write(chunk)
            except Exception:
                break
            length -= len(chunk)

if __name__ == '__main__':
    port = 8000
    socketserver.TCPServer.allow_reuse_address = True
    try:
        httpd = socketserver.TCPServer(("", port), RangeRequestHandler)
        print(f"Server START (Range Support ON) -> http://localhost:{port}")
        httpd.serve_forever()
    except OSError:
        print(f"Puerto {port} ocupado. Probando 8002...")
        httpd = socketserver.TCPServer(("", 8002), RangeRequestHandler)
        print(f"Server START (Range Support ON) -> http://localhost:8002")
        httpd.serve_forever()
