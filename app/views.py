from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', output_text='sample text')

@app.route('/index', methods=['POST'])
def form():
    name=request.form(name)
    return render_template('index.html', output_text=name)

@app.route('/dev')
def dev():
    return '<h1> Congratulations, you found the dev page. </h1>'

@app.route('/yo')
def yo():
    return '<a href="www.goathub.co">yo</a>'

@app.route('/sum/<a>/<b>')
def math(a, b):
    return "sum: " + str(int(a) + int(b))
