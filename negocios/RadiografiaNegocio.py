from datos.Covid import Covid
from datos.Normal import Normal
from datos.NeumoniaViral import NeumoniaViral
from datos.OpacidadPulmonar import OpacidadPulmonar


class RadiografiaNegocio:

    TIPO_NORMAL = 'normal'
    TIPO_COVID = 'covid'
    TIPO_NEUMONIA_VIRAL = 'neumonia viral'
    TIPO_OPACIDAD_PULMONAR = 'opacidad pulmonar'

    def __init__(self):
        self.__covid = Covid()
        self.__normal = Normal()
        self.__neumonia_viral = NeumoniaViral()
        self.__opacidad_pulmonar = OpacidadPulmonar()

    def listar(self, tipo):
        lista = self.__normal.leer_registros()
        if tipo == self.TIPO_COVID:
            lista = self.__covid.leer_registros()
        elif tipo == self.TIPO_NEUMONIA_VIRAL:
            lista = self.__neumonia_viral.leer_registros()
        elif tipo == self.TIPO_OPACIDAD_PULMONAR:
            lista = self.__opacidad_pulmonar.leer_registros()
        return lista

    def registrar(self, tipo, nombre, formato, dimensiones, url, archivo_imagen, archivo_mask):
        if tipo == self.TIPO_NORMAL:
            self.__normal.crear_registro(nombre, formato, dimensiones, url, archivo_imagen, archivo_mask)
        elif tipo == self.TIPO_COVID:
            self.__covid.crear_registro(nombre, formato, dimensiones, url, archivo_imagen, archivo_mask)
        elif tipo == self.TIPO_NEUMONIA_VIRAL:
            self.__neumonia_viral.crear_registro(nombre, formato, dimensiones, url, archivo_imagen, archivo_mask)
        elif tipo == self.TIPO_OPACIDAD_PULMONAR:
            self.__opacidad_pulmonar.crear_registro(nombre, formato, dimensiones, url, archivo_imagen, archivo_mask)

    def actualizar(self, tipo, nombre_anterior, nombre_nuevo, formato_nuevo, dimensiones_nuevo, url_nuevo, archivo_imagen_nuevo, archivo_mask_nuevo):
        if tipo == self.TIPO_NORMAL:
            self.__normal.actualizar_registro(nombre_anterior, nombre_nuevo, formato_nuevo, dimensiones_nuevo, url_nuevo, archivo_imagen_nuevo, archivo_mask_nuevo)
        elif tipo == self.TIPO_COVID:
            self.__covid.actualizar_registro(nombre_anterior, nombre_nuevo, formato_nuevo, dimensiones_nuevo, url_nuevo, archivo_imagen_nuevo, archivo_mask_nuevo)
        elif tipo == self.TIPO_NEUMONIA_VIRAL:
            self.__neumonia_viral.actualizar_registro(nombre_anterior, nombre_nuevo, formato_nuevo, dimensiones_nuevo, url_nuevo, archivo_imagen_nuevo, archivo_mask_nuevo)
        elif tipo == self.TIPO_OPACIDAD_PULMONAR:
            self.__opacidad_pulmonar.actualizar_registro(nombre_anterior, nombre_nuevo, formato_nuevo, dimensiones_nuevo, url_nuevo, archivo_imagen_nuevo, archivo_mask_nuevo)

    def eliminar(self, tipo, nombre):
        if tipo == self.TIPO_NORMAL:
            self.__normal.eliminar_registro(nombre)
        elif tipo == self.TIPO_COVID:
            self.__covid.eliminar_registro(nombre)
        elif tipo == self.TIPO_NEUMONIA_VIRAL:
            self.__neumonia_viral.eliminar_registro(nombre)
        elif tipo == self.TIPO_OPACIDAD_PULMONAR:
            self.__opacidad_pulmonar.eliminar_registro(nombre)