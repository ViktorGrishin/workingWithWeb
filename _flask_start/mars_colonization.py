from flask import Flask, url_for

# http://127.0.0.1:8080/
# http://127.0.0.1:8080/index
# http://127.0.0.1:8080/promotion


app = Flask('Колонизация')


@app.route('/')
def mission():
    return 'Миссия: колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return """Человечество вырастает из детства.<br>Человечеству мала одна планета.<br>
    Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!"""


@app.route('/image_mars')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="https://strek-time.ru/wp-content/uploads/d/0/c/d0cc49cccc7857301415d1da4a71157e.jpeg" 
                        alt="здесь должна была быть картинка, но не нашлась" width=500>
                    <div>Вот она какая, красная планета </div>
                    
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
