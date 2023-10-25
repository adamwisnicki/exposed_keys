# This is an example of bad security practice
# Do not hard-code your API keys in your code
# Use environment variables or other secure methods instead

import requests

# Hard-coded API key ID and secret
API_KEY_ID = "AKIAW6RRNZ6C2RTT5BZG"
API_KEY_SECRET = "VJL5zhbpRZZ8hpZKngKxG7wNdAfLhTdUN0d2jFGp"

# Example API request using the hard-coded key
response = requests.get("https://example.com/api/v1/data", auth=(API_KEY_ID, API_KEY_SECRET))
data = response.json()
print(data)
