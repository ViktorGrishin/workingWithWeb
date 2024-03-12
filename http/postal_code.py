import requests

PLACE = "Москва, Петровка, 38"
API_KEY = "40d1649f-0493-4b70-98ba-98533de7710b"
response = requests.request(
    method='GET',
    url="https://geocode-maps.yandex.ru/1.x",
    params={
        "apikey": API_KEY,
        "geocode": PLACE,
        "format": "json"
    }
)

if response:
    data = response.json()
    toponym = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    postal_code = toponym['metaDataProperty']['GeocoderMetaData']['Address']['postal_code']
    print(postal_code)

else:
    print("Ошибка выполнения запроса:")
    print("Http статус:", response.status_code, "(", response.reason, ")")