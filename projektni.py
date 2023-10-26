import requests

payload = {'ime':'"Dominik', 'prezime': 'Lucic', 'ip': "192.168.86.103"}
response = requests.post('http://192.168.86.210/', json = payload)
print(response.text)
print(response.status_code)