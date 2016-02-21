from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', output_text='text')

@app.route('/dev')
def dev():
    return '<h1> Congratulations, you found the dev page. </h1>'

@app.route('/yo')
def yo():
    return '<a href="www.goathub.co">yo</a>'

@app.route('/sum/<a>/<b>')
def math(a, b):
    return "sum: " + str(int(a) + int(b))
