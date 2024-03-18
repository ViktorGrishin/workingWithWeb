import requests

server = input()
port = input()
a, b = input(), input()
url = server + ':' + port
param = {'a': a,
         'b': b}
response = requests.request(url=url, method='GET',
                            params=param)

if response:
    data = response.json()
    print(*sorted(data['result']))
    print(data['check'])
else:
    print('error')