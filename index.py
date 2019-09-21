from flask import render_template
from flask import Flask
from flask import request, jsonify
import base64
import facerec.face_recognition_ins as fr
import face_recognition
import argparse
import imutils
import pickle
from time import sleep
import cv2
from PIL import Image
import numpy as np
from numpy import linalg as la


app = Flask(__name__)

nombre = ''
@app.route('/')
def hello(name=None):
    return render_template('index.html')

@app.route('/questions.html')
def questions(name=None):
    return render_template('questions.html')


@app.route('/caracara/<nombre>/<edad>')
def cara(nombre, edad):
    # leer el txt o name
    # buscar en el json el nombre y obtener sus datos
    # enviar eso por post a javascript
    
    # leer txt de usuario actual que contiene nombre datos
    # ya se donde esta guardada la foto de la persona,
    return render_template('caracara.html', nombre = nombre, edad=edad)


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
	print('ya')

	filename = 'Faces/' + foto_index + '.jpg'  # I assume you have a way of picking unique filenames
#	with open(filename, 'wb') as f:
#		f.write(data)

	nombre = fr.encuentra_cara()
	text_file=open("match_text.txt",'w')
	n = text_file.write(nombre)
	text_file.close()
	
	
	return jsonify(result=nombre)
    
	

