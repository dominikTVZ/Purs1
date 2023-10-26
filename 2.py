import requests

response = requests.get('http://192.168.86.210/')
print(response.text)
print(response.status_code)

print(response.headers)