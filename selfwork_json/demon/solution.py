import json
import sys

import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('server')
parser.add_argument('port')
parser.add_argument('rooms', nargs='*')
parser.add_argument('--mult', default=2)
parser.add_argument('--not_mult', default=None)

args = parser.parse_args()
server = args.server
port = args.port
rooms = args.rooms
mult = int(args.mult)
not_mult = args.not_mult

url = f'http://{server}:{port}'

resp = requests.request(method="GET",
                        url=url)

if not resp:
    sys.exit()

data = resp.json()
places = list(data.keys())
places.sort()
answer = []
for place in places:
    numbers = data[place]
    sila = []
    for num in numbers:
        if num % 5 == 0:
            sila.append(num // mult)
        elif not_mult is None:
            sila.append(num)
        else:
            sila.append(num % int(not_mult))
    answer.append({"place": place,
                   "rests": sum(map(lambda x: x % 5, sila)),
                   "smallest": min(sila)})

with open("box.json", 'w') as file:
    json.dump(answer, file)
