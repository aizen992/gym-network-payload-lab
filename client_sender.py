import json
import urllib.request

# Load JSON workout data
with open("workout.json", "r") as f:
    workout_data = json.load(f)

url = "http://localhost:8000/"
json_payload = json.dumps(workout_data).encode("utf-8")

# Prepare the HTTP POST request
req = urllib.request.Request(
    url,
    data=json_payload,
    headers={'Content-Type': 'application/json'},
    method='POST'
)

print(f"Sending gym payload ({len(json_payload)} bytes) to server...")
try:
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print(f"Server Response: {response_body}")
except Exception as e:
    print(f"Connection failed: {e}. Make sure the server is running!")