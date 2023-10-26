import requests

response = requests.post('http://192.168.86.210/svi_bodovi')


print(response.status_code)
print(response.text)