import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

HOSTNAME = socket.gethostname()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = f"Hello from Swarm container: {HOSTNAME}\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

server = HTTPServer(("0.0.0.0", 5000), Handler)
server.serve_forever()
