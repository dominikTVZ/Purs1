import requests

params = {
    'id':1
}
response = requests.delete('http://192.168.86.210/temperatura', params = params)


print(response.status_code)
print(response.text)