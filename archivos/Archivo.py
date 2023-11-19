import pandas as pd
import os
import shutil


def cargar_datos(nombre_archivo):
    try:
        ruta = os.path.dirname(os.path.abspath(__file__)) + '/data' + nombre_archivo
        df = pd.read_csv(ruta)
        return df
    except FileNotFoundError:
        print('El archivo no existe')
        return pd.DataFrame(columns=['FILE NAME', 'FORMAT', 'SIZE', 'URL'])


def guardar_datos(nombre_archivo, df):
    try:
        ruta = os.path.dirname(os.path.abspath(__file__)) + '/data' + nombre_archivo
        df.to_csv(ruta, index=False)
    except FileNotFoundError:
        print('El archivo no existe')


def guardar_imagen(archivo, tipo, nombre, formato):
    if archivo:
        nuevo_nombre_archivo = f"{nombre}.{formato}"
        ruta = os.path.dirname(os.path.abspath(__file__)) + '/data' + tipo + nuevo_nombre_archivo
        shutil.copy(archivo, ruta)