from flask import render_template
from flask import Flask
from flask import request, jsonify
import base64
import facerec.face_recognition_ins as fr



app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('index.html')

@app.route('/questions.html')
def questions(name=None):
    return render_template('questions.html')


@app.route('/caracara')
def cara(name=None):
    return render_template('caracara.html')


@app.route('/message.html')
def message(name=None):
    return render_template('message.html')

@app.route('/camara')
def camara(name=None):
    return render_template('facedetector/example/camara.html')

@app.route('/image-send', methods=['POST'])
def imagesend():
	#i = request.files['foto'].read()
	
	data = request.files['imagen'].read()
	foto_index = request.form["foto"]
	imgdata = base64.b64decode(data)

	filename = 'Faces/' + foto_index + '.jpg'  # I assume you have a way of picking unique filenames
#	with open(filename, 'wb') as f:
#		f.write(data)
	nombre = fr.encuentra_cara()
	
	return jsonify(result=nombre)
    
	

