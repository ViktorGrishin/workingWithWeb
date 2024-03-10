from zipfile import ZipFile

with ZipFile('input.zip') as archive:
    files = archive.namelist()

for filename in files:
    count = filename.count('/')
    if filename[-1] == '/':
        count -= 1
        filename = filename[:-1]
    filename = filename.split('/')[-1]
    print('  ' * count + filename)
