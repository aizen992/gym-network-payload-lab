import http.server
import json

class GymServerHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the incoming data length and payload
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        # Print what the server received
        print(f"\n[SERVER] Received Gym Workout Payload over HTTP!")
        print(f"-> Member ID: {data.get('member_id')}")
        print(f"-> Focus Areas: {', '.join(data.get('focus', []))}")
        
        # Send an HTTP 200 OK response back to the client
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        response = {"status": "success", "message": "Workout payload received and logged!"}
        self.wfile.write(json.dumps(response).encode('utf-8'))

if __name__ == "__main__":
    server_address = ('localhost', 8000)
    httpd = http.server.HTTPServer(server_address, GymServerHandler)
    print("[SERVER] Gym HTTP server listening on http://localhost:8000 ...")
    httpd.serve_forever()