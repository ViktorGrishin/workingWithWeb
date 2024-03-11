from zipfile import ZipFile
import os


def human_read_format(size):
    if size // 1024 == 0:
        return f'{size}Б'
    size = round(size / 1024)
    if size // 1024 == 0:
        return f'{size}КБ'
    size = round(size / 1024)
    if size // 1024 == 0:
        return f'{size}МБ'
    size = round(size / 1024)
    return f'{size}ГБ'


with ZipFile('input.zip') as archive:
    files = archive.namelist()
    info = archive.infolist()

for i, filename in enumerate(files):
    count = filename.count('/')
    if filename[-1] == '/':
        count -= 1
        filename = filename[:-1]
    filename = filename.split('/')[-1]
    if not info[i].is_dir():
        print('  ' * count + filename + ' ' + human_read_format(info[i].file_size))
    else:
        print('  ' * count + filename)
