# This is an example of bad security practice
# Do not hard-code your API keys in your code
# Use environment variables or other secure methods instead

import requests

# Hard-coded API key ID and secret
API_KEY_ID = "XXX"
API_KEY_SECRET = "1234"

# Example API request using the hard-coded key
response = requests.get("https://example.com/api/v1/data", auth=(API_KEY_ID, API_KEY_SECRET))
data = response.json()
print(data)
