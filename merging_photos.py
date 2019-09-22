import os
from pathlib import Path

dict = {}
dict1 = {}
dict2 = {}
dict3 = {}

directory = 'Fotos_con_match_guionbajo'
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        dict[filename] = [directory]
        dict1[filename] = [directory]
        #print(filename)

directory = 'Fotos_sin_match_guionbajo'
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        if filename in dict:
            dict[filename].append(directory)
        else:
            dict[filename] = [directory]
        dict2[filename] = [directory]

        #print(filename)

directory = 'static/Imagenes'
pathlist = Path(directory).glob('**/*.jpg')
for path in pathlist:
    # because path is object not string
    path_in_str = str(path).split("\\")[3]
    if path_in_str in dict:
        dict[path_in_str].append(directory)
    else:
        dict[path_in_str] = [directory]
    dict3[path_in_str] = [directory]
     #print(path_in_str)

# Matches apellidos de Imagenes con Fotos_con_match_guionbajo
def match(nombre):
    lista = nombre.split("_")
    paterno,materno = lista[2:]
    apellidos = "_"+paterno+"_" + materno
    res = False
    for key, value in dict1.items():
        if apellidos in key:
            print(key)
            res = True
    return res

print("Matches apellidos de Imagenes con Fotos_con_match_guionbajo")
for key, value in dict3.items():
    if match(key):
        print(key)

# Matches apellidos de Imagenes con Fotos_con_match_guionbajo
def match2(nombre):
    lista = nombre.split("_")
    paterno,materno = lista[2:]
    apellidos = paterno+" " + materno +" "
    apellidos = apellidos[0:len(apellidos)-5]
    res = False
    #print(apellidos)
    for key, value in dict2.items():
        if apellidos in key:
            print(key)
            res = True
    return res

print("Matches apellidos de Imagenes con Fotos_sin_match_guionbajo")
for key, value in dict3.items():
    if match2(key):
        print(key)




#print(dict)
# Se revisan manualmente las fotos para ver su utilidad
#Perfect matches
print("Matches perfectos de Imagenes")
for key, value in dict.items():
    if len(value)>1:
        print(key,value)
