import requests
import urllib3
import json

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
    'http://api.kaltimprov.go.id/api/v2/generate/samarinda/diskominfo/cctv', headers=my_headers, verify=False)
# print(response.text)

data = response.json()
# parse_json = json.loads(data)
# nama = parse_json['Data']['nama']
# print(nama)
for s in range(len(data['data'])):
    print("Nama Tempat {} \n URL :  {}.".format(
        data['data'][s]['nama'], data['data'][s]['url']))
