import os
from http.server import BaseHTTPRequestHandler, HTTPServer

APP_ENV = os.getenv("APP_ENV", "unknown")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = f"API Python OK - APP_ENV={APP_ENV}\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

server = HTTPServer(("0.0.0.0", 5000), Handler)
server.serve_forever()
