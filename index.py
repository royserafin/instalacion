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
import pandas as pd


app = Flask(__name__)


@app.route('/')
def hello(name=None):
    return render_template('index.html')

@app.route('/questions.html')
def questions(name=None):
    return render_template('questions.html')

@app.route('/message.html')
def message(name=None):
    return render_template('message.html')
    
@app.route('/guardadato/<nombre>/<apellido>', methods = ['POST'])
def guardadato(nombre, apellido):
    text_file=open("datos_usuario.txt",'w')
    n = text_file.write(nombre + '\n')
    n = text_file.write(apellido + '\n')
    text_file.close()
    
    return jsonify(respuesta='ke pedo puto')
    
@app.route('/guardadato2/<edad>', methods = ['POST'])
def guardadato2(edad):
    text_file=open("datos_usuario.txt",'a')
    n = text_file.write(edad + '\n')
    text_file.close()
    
    return jsonify(respuesta='ke pedo puto')
    
@app.route('/guardadato3/<estatura>', methods = ['POST'])
def guardadato3(estatura):
    text_file=open("datos_usuario.txt",'a')
    n = text_file.write(estatura + '\n')
    text_file.close()
    
    return jsonify(respuesta='ke pedo puto')
    
@app.route('/guardadato4/<estado>/<municipio>', methods = ['POST'])
def guardadato4(estado, municipio):
    text_file=open("datos_usuario.txt",'a')
    n = text_file.write(estado + '\n')
    n = text_file.write(municipio + '\n')
    text_file.close()
    
    return jsonify(respuesta='Ok')

@app.route('/comotu/<nombre>/<apellido>/<edad>/<estado>/<municipio>/<nombre_stats>/<apellido_stats>/<edad_stats>/<estado_stats>/<municipio_stats>')
def comotu(nombre, apellido, edad, estado, municipio, nombre_stats, apellido_stats, edad_stats, estado_stats, municipio_stats):              
    #print(nombre.split())
    nombre, apellido = nombre.split()
    #print(nombre,edad,estado,municipio)
    edad = edad.strip()
    datos_estadisticas = estadisticas(nombre, apellido, edad, estado, municipio)
    #print(datos_estadisticas['nombre'])
    nombre_stats = datos_estadisticas['nombre']
    apellido_stats = datos_estadisticas['apellido']
    edad_stats = datos_estadisticas['edad']
    estado_stats = datos_estadisticas['estado']
    municipio_stats = datos_estadisticas['municipio']
    #print(datos_estadisticas)
    return render_template('comotu.html', nombre = nombre, apellido = apellido, edad = edad, estado=estado, municipio=municipio, nombre_stats = nombre_stats, apellido_stats = apellido_stats, edad_stats = edad_stats, estado_stats = estado_stats, municipio_stats = municipio_stats)

@app.route('/caracara/<nombre>/<nombreD>/<edadD>/<estaturaD>/<estadoD>/<municipioD>/<fechaD>/<nombreU>/<edadU>/<estaturaU>/<estadoU>/<municipioU>')
def cara(nombre, nombreD, edadD, estaturaD, estadoD, municipioD, fechaD, nombreU, edadU, estaturaU, estadoU, municipioU):
    # leer el txt o name
    # buscar en el json el nombre y obtener sus datos
    # enviar eso por post a javascript
    
    # leer txt de usuario actual que contiene nombre datos
    # ya se donde esta guardada la foto de la persona,
    
    text_file=open("datos_usuario.txt",'r')
    n = text_file.readline()
    n2 = text_file.readline()
    n = n.upper()
    n2 = n2.upper()
    nombreU = n + ' ' + n2
    edadU = text_file.readline()
    edadU = edadU.upper()
    estaturaU = text_file.readline()
    estaturaU = estaturaU.upper()
    estadoU = text_file.readline()
    estadoU = estadoU.upper()
    municipioU = text_file.readline()
    municipioU = municipioU.upper()
    text_file.close()
    return render_template('caracara.html', nombre = nombre, nombreD = nombreD, edadD=edadD, estaturaD = estaturaD, estadoD = estadoD, municipioD = municipioD, fechaD = fechaD, nombreU = nombreU, edadU = edadU, estadoU = estadoU, estaturaU = estaturaU, municipioU =municipioU)

@app.route('/camara')
def camara(name=None):
    return render_template('facedetector/example/camara.html')
    
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/image-send', methods = ['POST'])
def imagesend():
	#i = request.files['foto'].read()
	data = request.files['imagen'].read()
	foto_index = request.form["foto"]
	imgdata = base64.b64decode(data)
	print('ya')
	
	filename = 'static/Faces/' + foto_index + '.jpg'  # I assume you have a way of picking unique filenames
	#with open(filename, 'wb') as f:
	#    f.write(data)
	
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
	
	nombreU = "1"
	edadU = "2"
	estaturaU = "3"
	estadoU = "4"
	municipioU = "5"
	
	return jsonify(nombre = nombre, nombreD = nombreD, edadD=edadD, estaturaD = estaturaD, estadoD = estadoD, municipioD = municipioD, fechaD = fechaD, nombreU = nombreU, edadU = edadU, estaturaU = estaturaU, estadoU = estadoU, municipioU = municipioU)
	
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

def acentos(cad):
    cad = cad.replace("á", "a")
    cad = cad.replace("é", "e")
    cad = cad.replace("í", "i")
    cad = cad.replace("ó", "o")
    cad = cad.replace("ú", "u")
    cad = cad.replace("Á","A")
    cad = cad.replace("É","E")
    cad = cad.replace("Í","I")
    cad = cad.replace("Ó","O")
    cad = cad.replace("Ú","U")
    return cad

def estadisticas(nombre, apellido, edad, estado, municipio):
    df3=pd.read_csv('report_12_01_2018_2.csv')
    nombre = acentos(nombre)
    apellido = acentos(apellido)
    estado = acentos(estado)
    municipio = acentos(municipio)
    res = {
        'nombre': 0,
        'apellido': 0,
        'edad': 0,
        'estado': 0,
        'municipio': 0
        }

    res['nombre'] = df3[(df3['prim_nombre'] == nombre.upper()) | (df3['seg_nombre'] == nombre.upper())].shape[0]
    res['apellido'] = df3[(df3['apellido_pat'] == apellido.upper()) | (df3['apellido_mat'] == nombre.upper())].shape[0]
    res['edad'] =df3[df3['fuerocomun_edad'] == edad].shape[0]
    res['estado'] =df3[df3['fuerocomun_desapentidad'] == estado.upper()].shape[0]
    res['municipio'] =df3[(df3['fuerocomun_desapentidad'] == estado.upper()) & (df3['fuerocomun_desapmunicipio'] == municipio.upper())].shape[0]

    return res
