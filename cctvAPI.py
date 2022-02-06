import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

token = ""
with open('assets/file/token.txt', 'r') as f:
    token = f.read()

my_headers = {
    'Authorization': 'Bearer '+token.strip(),
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
response = requests.get(
    'http://api.kaltimprov.go.id/api/v2/generate/samarinda/dishub/cctv', headers=my_headers, verify=False)
print(response.json())
