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


def get_files_sizes():
    out = ''
    for file in os.listdir():
        if os.path.isfile(file):
            out += f"{file} {human_read_format(os.stat(file).st_size)}\n"
    return out.strip()
