from flask import Flask, render_template

app = Flask("Марс будет НАШ!")

app.config['SECRET_KEY'] = 'my_secret_key'


@app.route('/')
@app.route('/index')
def index():
    title = 'Марсиане скажут спасибо'
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    prof = prof.lower()
    return render_template('profession.html', title='На, работай!', prof=prof)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
