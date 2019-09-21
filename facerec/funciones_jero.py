import json
from cv2 import cvtcolor

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
    
    try:
        img=misc.imread(f'Imagenes/{file}/{file}.jpg')
    except:
        img=misc.imread(f'Imagenes/{file}/{file}.png')
    plt.imshow(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detect faces in the grayscale frame
    rects = detector.detectMultiScale(gray, scaleFactor=1.1,
    minNeighbors=5, minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)
    boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]
    (x,y,w,h)=rects[0]
    plt.figure()
    new_img=misc.imresize(img,(200,200))
    plt.imshow(new_img[boxes[0][0]-h//4:boxes[0][2]+h//4,boxes[0][3]-w//4:boxes[0][1]+w//4,:])

