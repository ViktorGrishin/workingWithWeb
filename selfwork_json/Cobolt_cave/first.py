import csv
import json
golden_rooms = []
with open('things.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        items = (row['item1'], row['item2'], row['item3'])
        if any(map(lambda x: 'gold' in x, items)):
            golden_rooms.append({"room": row["room"],
                                 "size": int(row["size"])})

with open('treasure.json', 'w') as file:
    json.dump(golden_rooms, file)
