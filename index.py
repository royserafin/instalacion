from flask import render_template, redirect, url_for
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
import json
from numpy import linalg as la
#import misc



app = Flask(__name__)

nombre = ''
@app.route('/')
def hello(name=None):
    return render_template('index.html')

@app.route('/questions.html')
def questions(name=None):
    return render_template('questions.html')


@app.route('/caracara/<nombre>/<nombreD>/<edadD>/<estaturaD>/<estadoD>/<municipioD>/<fechaD>/<nombreU>/<edadU>/<estaturaU>/<estadoU>/<municipioU>')
def cara(nombre, nombreD, edadD, estaturaD, estadoD, municipioD, fechaD, nombreU, edadU, estaturaU, estadoU, municipioU):
    # leer el txt o name
    # buscar en el json el nombre y obtener sus datos
    # enviar eso por post a javascript
    
    # leer txt de usuario actual que contiene nombre datos
    # ya se donde esta guardada la foto de la persona,
    return render_template('caracara.html', nombre = nombre, nombreD = nombreD, edadD=edadD, estaturaD = estaturaD, estadoD = estadoD, municipioD = municipioD, fechaD = fechaD, nombreU = nombreU, edadU = edadU, estadoU = estadoU, estaturaU = estaturaU, municipioU =municipioU)


@app.route('/message.html')
def message(name=None):
    return render_template('message.html')

@app.route('/camara')
def camara(name=None):
    return render_template('facedetector/example/camara.html')

@app.route('/image-send', methods = ['POST'])
def imagesend():
	
	#i = request.files['foto'].read()
	data = request.files['imagen'].read()
	foto_index = request.form["foto"]
	imgdata = base64.b64decode(data)
	print('ya')
	
	filename = 'static/Faces/' + foto_index + '.jpg'  # I assume you have a way of picking unique filenames
	with open(filename, 'wb') as f:
	    f.write(data)
	
	nombre = fr.encuentra_cara()
	text_file=open("match_text.txt",'w')
	n = text_file.write(nombre)
	text_file.close()
	datos_desaparecidos = datos_desaparecido(nombre)
	nombreD =  datos_desaparecidos['nombre']
	edadD= datos_desaparecidos['edad']
	estaturaD = datos_desaparecidos['estatura']
	estadoD = datos_desaparecidos['estado']
	municipioD = datos_desaparecidos['municipio']
	fechaD = datos_desaparecidos['fecha']
	nombreU = "Rodolfo Ocampo Blanco"
	edadU = "25"
	estaturaU = "1.74"
	estadoU = "Ciudad de Mexico"
	municipioU = "Miguel Hidalgo"
	#return render_template('index.html')
	return jsonify(nombre = nombre, nombreD = nombreD, edadD=edadD, estaturaD = estaturaD, estadoD = estadoD, municipioD = municipioD, fechaD = fechaD, nombreU = nombreU, edadU = edadU, estaturaU = estaturaU, estadoU = estadoU, municipioU =municipioU)
	
#res={'nombre':,'apellido','edad','estatura','estado','municipio'}
def datos_desaparecido(nombre):
    with open('personasdesaparecidas.json','r',encoding='utf8') as f:
        datastore=json.load(f)
    for persona in datastore:
        file=f"{persona['versiones'][0]['prim_nombre']}_{persona['versiones'][0]['seg_nombre']}_{persona['versiones'][0]['apellido_pat']}_{persona['versiones'][0]['apellido_mat']}"
        if(file==nombre):
            res={'nombre':f"{persona['versiones'][0]['prim_nombre']} {persona['versiones'][0]['seg_nombre']} {persona['versiones'][0]['apellido_pat']} {persona['versiones'][0]['apellido_mat']}"
                   ,'edad':persona['versiones'][0]['fuerocomun_edad']
                   ,'estatura':persona['versiones'][0]['fuerocomun_estatura']
                   ,'estado':persona['versiones'][0]['fuerocomun_desapentidad']
                   ,'municipio':persona['versiones'][0]['fuerocomun_desapmunicipio']
                   ,'fecha':persona['versiones'][0]['fuerocomun_desapfecha']}
            res['fecha']=res['fecha'].replace('/','-')
            return res
            
def recorta_cara(file):
    detector = cv2.CascadeClassifier('facerec/haarcascade_frontalface_default.xml')    
    try:
        img=cv2.imread(file)
    except:
        img=cv2.imread(file)
    #plt.imshow(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detect faces in the grayscale frame
    rects = detector.detectMultiScale(gray, scaleFactor=1.1,
    minNeighbors=5, minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)
    boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]
    (x,y,w,h)=rects[0]
    #plt.figure()
    new_img=cv2.resize(img,(200,200))
    cv2.imwrite(file, new_img)
    #plt.imshow(new_img[boxes[0][0]-h//4:boxes[0][2]+h//4,boxes[0][3]-w//4:boxes[0][1]+w//4,:])
