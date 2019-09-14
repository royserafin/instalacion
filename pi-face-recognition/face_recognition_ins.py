# USAGE
# python pi_face_recognition.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle

# import the necessary packages
import face_recognition
import argparse
import imutils
import pickle
from time import sleep
import cv2
from PIL import Image
import numpy as np
from numpy import linalg as la
from picamera import PiCamera

#camera = PiCamera()

#camera.start_preview(alpha = 200)
#sleep(5)
#camera.stop_preview()
# load the known faces and embeddings along with OpenCV's Haar
# cascade for face detection
print("[INFO] loading encodings + face detector...")
data = pickle.loads(open('encodings.pickle', "rb").read())
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
indexes = []
counts = {}
for i in range(10):
    with PiCamera() as camera:
        camera.resolution = (320,240)
        camera.framerate = 24
        sleep(2)
        image = np.empty((240*320*3,), dtype = np.uint8)
        camera.capture(image, 'bgr')
        frame = image.reshape((240, 320, 3))
    print('../Faces/' + str(i) + '.jpg')
    #frame = Image.open('../Faces/' + str(i) + '.jpg')
    #frame = cv2.imread('../Faces/' + str(i) + '.jpg')
    frame = imutils.resize(frame, width=500)
    # convert the input frame from (1) BGR to grayscale (for face
    # detection) and (2) from BGR to RGB (for face recognition)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # detect faces in the grayscale frame
    rects = detector.detectMultiScale(gray, scaleFactor=1.1,
	    minNeighbors=5, minSize=(30, 30),
	    flags=cv2.CASCADE_SCALE_IMAGE)
    #print(rects)
    # OpenCV returns bounding box coordinates in (x, y, w, h) order
    # but we need them in (top, right, bottom, left) order, so we
    # need to do a bit of reordering
    boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]
    #print(boxes)
    if len(boxes)>0:
    	boxes = [(int(boxes[0][0]),int(boxes[0][1]),int(boxes[0][2]),int(boxes[0][3]))]
    #print(boxes)
    # compute the facial embeddings for each face bounding box
    encodings = face_recognition.face_encodings(rgb, boxes)

    name = ''

    for encoding in encodings:
    	# attempt to match each face in the input image to our known
    	# encodings
    	norms = face_recognition.face_distance(data["encodings"], encoding)
    	index = np.argmin(norms)
    	name = data["names"][index]
    	counts[name] = counts.get(name, 0) + 1
for key, value in counts.items():
    print(key, value)
nombre = max(counts, key=counts.get)

archivo = '../Imagenes/' + nombre + '/' + nombre + '.jpg'
print(archivo)

# do a bit of cleanup
#cv2.destroyAllWindows()
