import pandas as pd

df3=pd.read_csv('rnped_fuerocomun/report_12_01_2018_2.csv')

def estadisticas(nombre, apellido, edad, estado, municipio):
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
    res['municipio'] =df3[(df3['fuerocomun_desapentidad'] == estado.upper()) & (df3['fuerocomun_desapmunicipio')] == municipio.upper()].shape[0]

    return res
