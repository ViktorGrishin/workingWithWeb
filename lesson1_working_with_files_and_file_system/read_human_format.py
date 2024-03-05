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
