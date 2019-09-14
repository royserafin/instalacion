from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('index.html')

@app.route('/questions.html')
def questions(name=None):
    return render_template('questions.html')


@app.route('/caracara.html')
def cara(name=None):
    return render_template('caracara.html')


@app.route('/message.html')
def message(name=None):
    return render_template('message.html')

@app.route('/camara')
def camara(name=None):
    return render_template('facedetector/example/camara.html')

