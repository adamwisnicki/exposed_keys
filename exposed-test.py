from requests.auth import HTTPBasicAuth
import requests

url = 'https://api_url'
headers = {'Accept': 'application/json'}
auth = HTTPBasicAuth('apikey', 'MzCelu46sLDlWMG0H/RLemUHIFPCSErb6t7YC2Jq')
files = {'file': open('filename', 'rb')}

req = requests.get(url, headers=headers, auth=auth, files=files)
