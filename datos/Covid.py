import pandas as pd
from archivos.Archivo import cargar_datos, guardar_datos


class Covid:

    NOMBRE_ARCHIVO = '/covid/metadata.csv'

    def __init__(self):
        self.__df = cargar_datos(self.NOMBRE_ARCHIVO)

    def leer_registros(self):
        return self.__df.values

    def crear_registro(self, nombre, formato, dimensiones, url):
        nuevo_registro = pd.DataFrame([[nombre, formato, dimensiones, url]], columns=['FILE NAME', 'FORMAT', 'SIZE', 'URL'])
        self.__df = pd.concat([self.__df, nuevo_registro], ignore_index=True)
        guardar_datos(self.NOMBRE_ARCHIVO, self.__df)

    def actualizar_registro(self, nombre_antiguo, nombre_nuevo, formato_nuevo, dimensiones_nuevo, url_nuevo):
        self.__df.loc[self.__df['FILE NAME'] == nombre_antiguo, ['FILE NAME', 'FORMAT', 'SIZE', 'URL']] = [nombre_nuevo, formato_nuevo, dimensiones_nuevo, url_nuevo]
        guardar_datos(self.NOMBRE_ARCHIVO, self.__df)

    def eliminar_registro(self, nombre):
        self.__df = self.__df[self.__df['FILE NAME'] != nombre]
        guardar_datos(self.NOMBRE_ARCHIVO, self.__df)