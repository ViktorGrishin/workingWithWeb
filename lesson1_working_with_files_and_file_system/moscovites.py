from zipfile import ZipFile
import json

count = 0
with ZipFile('input.zip') as archive:
    for filename in archive.namelist():
        if filename.endswith('.json'):
            with archive.open(filename) as file:
                data = json.load(file)
                if data["city"] == 'Москва':
                    count += 1

print(count)
