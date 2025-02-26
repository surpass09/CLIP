import requests
import json

# Path to your JSON file
file_path = "/Users/suryapasupuleti/Documents/coding/LinkUp/load_data/JSON_with_last_names_and_emails.json"

# API endpoint
api_url = "http://127.0.0.1:8000/otlk/post/JSON/"

# Read the JSON file
try:
    with open(file_path, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"❌ Error: The file '{file_path}' was not found.")
    exit(1)
except json.JSONDecodeError:
    print(f"❌ Error: The file '{file_path}' contains invalid JSON.")
    exit(1)

# Send the entire JSON data
try:
    response = requests.post(api_url, json=data)
    response.raise_for_status()  # Raise an exception for HTTP errors
except requests.exceptions.RequestException as e:
    print(f"❌ Failed to send data: {e}")
    exit(1)

# Check the response
if response.status_code == 201:
    print("✅ Data sent successfully!")
    print("Response:", json.dumps(response.json(), indent=4))  # Pretty-print JSON response
else:
    print(f"❌ Failed to send data. Status Code: {response.status_code}")
    print("Response:", response.text)