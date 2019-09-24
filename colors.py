import cv2
import numpy as np
import os
from pathlib import Path

directory = 'static/Imagenes'
pathlist = Path(directory).glob('**/*1.jpg')
for path in pathlist:
    dir = str(path).split("\\")
    parent = dir[2]
    child = dir[3]
    path_in_str = f'{directory}/{parent}/{child}'
    #print(path_in_str)
    img = cv2.imdecode(np.fromfile(path_in_str, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    output = path_in_str.split("1")
    output = ''.join(output)
    #print(output)
    #img = cv2.imread(path_in_str.encode('utf-8'))
    height, width, channels = img.shape
    x = height if height > width else width
    y = height if height > width else width
    square= np.zeros((x,y,3), np.uint8)
    ini =(x-width)//2
    fin = ini + width
    ini_2 = (y-height)//2
    fin_2 = ini_2 + height
    square[ini_2:fin_2, ini:fin] = img
    cv2.imwrite(output,square)
    os.remove(path_in_str)
    print(output)
    #img = cv2.imread(f'{directory})
pathlist = Path(directory).glob('**/*.jpg')
for path in pathlist:
    dir = str(path).split("\\")
    parent = dir[2]
    child = dir[3]
    path_in_str = f'{directory}/{parent}/{child}'
    #print(path_in_str)
    img = cv2.imdecode(np.fromfile(path_in_str, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    #print(output)
    #img = cv2.imread(path_in_str.encode('utf-8'))
    height, width, channels = img.shape
    if height != width:
        x = height if height > width else width
        y = height if height > width else width
        square= np.zeros((x,y,3), np.uint8)
        ini =(x-width)//2
        fin = ini + width
        ini_2 = (y-height)//2
        fin_2 = ini_2 + height
        square[ini_2:fin_2, ini:fin] = img
        cv2.imwrite(path_in_str,square)
        print(path_in_str)
img = cv2.imread('static/Imagenes/ACOSTA  MONTOYA  JOEL___/ACOSTA  MONTOYA  JOEL___1.jpg')
#get size
height, width, channels = img.shape
print (img,height, width, channels)
# Create a black image
x = height if height > width else width
y = height if height > width else width
square= np.zeros((x,y,3), np.uint8)
#
#This does the job
#
square[(y-height)//2:y-(y-height)//2, (x-width)//2:x-(x-width)//2] = img
cv2.imwrite('out_img.jpg',square)
#cv2.imshow("original", img)
#cv2.imshow("black square", square)
#cv2.waitKey(0)
