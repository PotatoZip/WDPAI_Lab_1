import json
import random
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Type


class SimpleRequestHandler(BaseHTTPRequestHandler):

    users = [
        {
            'id': 1,
            'first_name': 'Michal',
            'last_name': 'Mucha',
            'role': 'Instructor'
        }
    ]

    def do_OPTIONS(self):
        self.send_response(200, "OK")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # response: dict = {
        #     "message": "This is a GET request",
        #     "path": self.path
        # }

        self.wfile.write(json.dumps(self.users).encode())

    def do_POST(self) -> None:
        content_length: int = int(self.headers['Content-Length'])
        post_data: bytes = self.rfile.read(content_length)
        received_data: dict = json.loads(post_data.decode())

        newUser: dict = {
            'id': random.randint(1, 1000000),
            'first_name': received_data['firstName'],
            'last_name': received_data['lastName'],
            'role': received_data['role']
        }
        self.users.append(newUser)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        self.wfile.write(json.dumps(self.users).encode())

    def do_DELETE(self) -> None:
        content_length: int = int(self.headers['Content-Length'])
        post_data: bytes = self.rfile.read(content_length)
        received_data: dict = json.loads(post_data.decode())
        user_id = received_data['id']

        SimpleRequestHandler.users = [user for user in self.users if user['id'] != user_id]

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        self.wfile.write(json.dumps(self.users).encode())

def run(
        server_class: Type[HTTPServer] = HTTPServer,
        handler_class: Type[BaseHTTPRequestHandler] = SimpleRequestHandler,
        port: int = 8000
        ) -> None:
    
    server_address: tuple = ('', port)
    httpd: HTTPServer = server_class(server_address, handler_class)

    print(f"Starting HTTP server on port {port}...")

    httpd.serve_forever()

if __name__ == '__main__':
    run()