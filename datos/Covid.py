import pandas as pd
from archivos.Archivo import cargar_datos, guardar_datos, guardar_imagen


class Covid:

    NOMBRE_ARCHIVO = '/covid/metadata.csv'
    TIPO_ARCHIVO_IMAGEN = '/covid/images/'
    TIPO_ARCHIVO_MASK = '/covid/masks/'

    def __init__(self):
        self.__df = cargar_datos(self.NOMBRE_ARCHIVO)

    def leer_registros(self):
        return self.__df.values

    def crear_registro(self, nombre, formato, dimensiones, url, archivo_imagen, archivo_mask):
        nuevo_registro = pd.DataFrame([[nombre, formato, dimensiones, url]], columns=['FILE NAME', 'FORMAT', 'SIZE', 'URL'])
        self.__df = pd.concat([self.__df, nuevo_registro], ignore_index=True)
        guardar_datos(self.NOMBRE_ARCHIVO, self.__df)
        guardar_imagen(archivo_imagen, self.TIPO_ARCHIVO_IMAGEN, nombre, formato)
        guardar_imagen(archivo_mask, self.TIPO_ARCHIVO_MASK, nombre, formato)

    def actualizar_registro(self, nombre_antiguo, nombre_nuevo, formato_nuevo, dimensiones_nuevo, url_nuevo, archivo_imagen_nuevo, archivo_mask_nuevo):
        self.__df.loc[self.__df['FILE NAME'] == nombre_antiguo, ['FILE NAME', 'FORMAT', 'SIZE', 'URL']] = [nombre_nuevo, formato_nuevo, dimensiones_nuevo, url_nuevo]
        guardar_datos(self.NOMBRE_ARCHIVO, self.__df)
        guardar_imagen(archivo_imagen_nuevo, self.TIPO_ARCHIVO_IMAGEN, nombre_nuevo, formato_nuevo)
        guardar_imagen(archivo_mask_nuevo, self.TIPO_ARCHIVO_MASK, nombre_nuevo, formato_nuevo)

    def eliminar_registro(self, nombre):
        self.__df = self.__df[self.__df['FILE NAME'] != nombre]
        guardar_datos(self.NOMBRE_ARCHIVO, self.__df)