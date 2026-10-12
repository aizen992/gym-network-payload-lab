A lightweight, event-driven HTTP client-server system built in Python to simulate logging structured gym workout data over a local network connection.

This project demonstrates core backend networking concepts—including JSON serialization, UTF-8 payload encoding, HTTP POST methods, and client-server response handling—without external dependencies.

🛠️ Tech Stack & Concepts
Language: Python 3 (Standard Library: json, urllib.request, http.server)

Data Format: JSON (JavaScript Object Notation)

Networking Protocol: HTTP / TCP (Port 8000)

Key Concepts: Client-Server Architecture, Data Serialization/Deserialization, HTTP Methods & Headers, Exception Handling, Git Version Control

📁 Repository Structure
Plaintext
gym-network-payload-lab/
│
├── workout_log.json     # Sample workout dataset containing exercise metrics
├── client_sender.py     # HTTP client script that serializes and transmits payload
├── server.py            # Local HTTP server listening for POST payloads
├── LICENSE              # Repository license
└── README.md            # Project documentation
⚙️ How It Works
Data Serialization: The client reads structured exercise data from workout_log.json and uses json.dumps() paired with .encode('utf-8') to transform the payload into raw binary bytes.

Network Transmission: The client constructs an HTTP POST request targeting http://localhost:8000/, setting the header Content-Type: application/json.

Server Processing: The HTTP server listens on port 8000, receives the byte stream, decodes and parses the JSON body, logs the exercise metrics, and responds with an HTTP 200 OK JSON confirmation.

🚀 Quick Start Guide
Prerequisites
Python 3.x installed on your system.

1. Clone the Repository
PowerShell
git clone https://github.com/aizen992/gym-network-payload-lab.git
cd gym-network-payload-lab
2. Start the HTTP Server
Open your terminal/PowerShell and launch the server:

PowerShell
python server.py
Expected Output:

Plaintext
[SERVER] Gym HTTP server listening on http://localhost:8000 ...
3. Send the Gym Payload
Open a second terminal window in the same folder and execute the client script:

PowerShell
python client_sender.py
Expected Output:

Plaintext
Sending gym payload (184 bytes) to server...
Server Response: {"status": "success", "message": "Workout payload received!"}
📋 Sample Payload Schema (workout_log.json)
JSON
{
  "member_id": "GYM-8842",
  "date": "2026-10-12",
  "session": "Chest & Shoulders",
  "exercises": [
    {
      "name": "Incline Dumbbell Press",
      "sets": 4,
      "reps": 10,
      "weight_kg": 32
    }
  ]
}