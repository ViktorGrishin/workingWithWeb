import requests

CITIES = ['Хабаровск', 'Уфа', 'Нижний Новгород', 'Калининград', 'Новокузнецк']
API_KEY = "40d1649f-0493-4b70-98ba-98533de7710b"
for city in CITIES:
    response = requests.request(
        method='GET',
        url="https://geocode-maps.yandex.ru/1.x",
        params={
            "apikey": API_KEY,
            "geocode": city,
            "format": "json"
        }
    )
    if response:
        data = response.json()
        toponym = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        components = toponym["metaDataProperty"]["GeocoderMetaData"]['Address']['Components']
        province = None
        for part in components:
            if part["kind"] == 'province':
                province = part['name']
                break
        if province is not None:
            print(f"{city}: {province}")
        else:
            print(f"Ошибка обработки запроса для города: {city}")

    else:
        print(f"Ошибка выполнения для города: {city}")
        print("Http статус:", response.status_code, "(", response.reason, ")")
