import requests

params = {
    'id':202
}
response = requests.get('http://192.168.86.210/hocu_bod', params = params)


print(response.status_code)
print(response.text)
print(response.headers.get('hocu_sve_bodove'))