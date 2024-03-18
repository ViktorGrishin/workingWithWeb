import requests
import json

with open('guests.json') as file:
    guests = json.load(file)

url = 'http://' + guests['server'] + ':' + str(guests['port'])
kind = guests["beings"]
gifts = []
response = requests.get(url=url)
if response:
    data = response.json()
    for guest in data:
        name = guest['entity'].split()
        is_good = False
        for part in name:
            for entity in kind:
                if entity in part:
                    is_good = True
                    break
        if is_good and (len(guest['gift'].split()) % 2 == 0):
            gifts.append(guest['gift'])

gifts.sort(reverse=True)
print('\n'.join(gifts))

