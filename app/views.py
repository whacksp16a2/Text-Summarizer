from app import app
import masterSummarizer as MS
from flask import render_template, request, url_for
from pirateSpeak import toPirateSpeak

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def form():
    book_name=request.form['name']
    print book_name
    output_text = MS.getSummary(book_name, 3)
    if output_text:
        print "it works"

    language = request.form['language']
    if language == 'pirate':
        output_text = toPirateSpeak(output_text)
    elif language == 'yoda':
        output_text = 'implemented, this was not'

    return render_template('index.html', output_text=output_text)

@app.route('/dev')
def dev():
    return '<h1> Congratulations, you found the dev page. </h1>'

@app.route('/yo')
def yo():
    return '<a href="www.goathub.co">yo</a>'

@app.route('/sum/<a>/<b>')
def math(a, b):
    return "sum: " + str(int(a) + int(b))
