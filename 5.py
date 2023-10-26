import requests

poruka = {'temperatura': 40}
response = requests.post('http://192.168.86.210/temperatura', json = poruka)


print(response.status_code)
print(response.text)