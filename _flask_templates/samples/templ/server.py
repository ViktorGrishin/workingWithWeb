from flask import Flask, render_template, json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)


@app.route('/my_sample')
def sample():
    return render_template('my_sample.html')


@app.route('/deque')
def deque():
    return render_template('deque.html', title='Очередь')


@app.route('/my_deq/<deq>')
def my_deq(deq):
    deq = deq.split()
    return render_template('my_deq.html', user_list=deq, title='Вторая очередь')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
