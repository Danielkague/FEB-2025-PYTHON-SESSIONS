import requests

# Make the GET request
response = requests.get("https://api.github.com/events")

# Parse the JSON response
events = response.json()

# Print a single event (e.g., the first event)
if events:  # Check if the response contains events
    print(events[0])  # Print the first event
else:
    print("No events found.")
