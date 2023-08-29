from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Main'}
    return render_template('index_sem_1.html', **context)


@app.route('/clothes/')
def clothes():
    context = {'title': 'Clothes'}
    return render_template('clothes.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Shoes'}
    return render_template('shoes.html', **context)


@app.route('/jackets/')
def jackets():
    context = {'title': 'Jackets'}
    return render_template('jackets.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
