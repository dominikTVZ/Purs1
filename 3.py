import requests

poruka = {'username':PURS, 'password':1234}
response = requests.post('http://192.168.86.210/login', json = poruka)


if response.status_code == 200:
    print(response.text)
    print(response.status_code)
else :
    print('Krivo je!')
