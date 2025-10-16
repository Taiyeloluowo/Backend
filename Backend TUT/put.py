from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {
        "name": "Sam Larry",
        "track": "AI Developer"
    }
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status = 200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

def do_PUT(self):
        """
        Handles PUT requests: expects a new item in the request body
        and replaces the existing 'data' list with the new data.
        """
        content_length = int(self.headers['Content-Length']) # Get the size of the data
        post_data = self.rfile.read(content_length) # Read the data
        
        try:
            new_data = json.loads(post_data.decode('utf-8'))
            global data # Need to declare 'data' as global to modify the outer list
            
            # Simple PUT implementation: assume the client sends the entire replacement list
            if isinstance(new_data, list):
                data[:] = new_data # Replace the contents of the global 'data' list
                self.send_data({"message": "Data successfully updated (PUT).", "current_data": data}, status=200)
            else:
                 self.send_data({"message": "Invalid data format. Expected a list."}, status=400)
                
        except json.JSONDecodeError:
            self.send_data({"message": "Invalid JSON format in request body."}, status=400)
        except Exception as e:
            self.send_data({"message": f"An error occurred: {e}"}, status=500)


def run():
        HTTPServer(('localhost', 8000), BasicAPI).serve_forever()

print("Application is running")
run()