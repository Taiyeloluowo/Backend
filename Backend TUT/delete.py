from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {"id": 1, "name": "Taiye", "role": "AI Engineer"},
    {"id": 2, "name": "Rachael", "role": "Software Manager"},
    {"id": 3, "name": "Idris", "role": "Software Engineer"}
]


class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_DELETE(self):
        global data
        content_size = int(self.headers.get("Content-Length", 0))
        raw_data = self.rfile.read(content_size).decode("utf-8")

        try:
            delete_data = json.loads(raw_data)
            id_to_delete = delete_data.get("id")

            if not id_to_delete:
                self.send_data({"error": "Missing ID in request"}, status=400)
                return

            for item in data:
                if item["id"] == id_to_delete:
                    data.remove(item)
                    self.send_data({
                        "Message": "Data deleted successfully!",
                        "Remaining Data": data
                    }, status=200)
                    return

            self.send_data({"error": "Record not found"}, status=404)

        except json.JSONDecodeError:
            self.send_data({"error": "Invalid JSON format"}, status=400)


def run():
    print("Application is running on http://localhost:5000")
    HTTPServer(('localhost', 5000), BasicAPI).serve_forever()

print("Application is running")
run()