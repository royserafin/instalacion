import cv2
import numpy as np

img = cv2.imread('instalacion/static/Imagenes/ACOSTA  MONTOYA  JOEL___/ACOSTA  MONTOYA  JOEL___1.jpg')
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
