import os.path
import sys
#import fabrica
from proyectoDCC import fabrica



class ProyectoDccError(Exception):
    pass


class Main:

    def __init__(self):
        self.__fabrica = fabrica.Fabrica()
        self.__dcc_instancia = self.get_dcc_instancia()()

    def get_dcc_instancia(self):
        path_interpreter = sys.executable
        interprete = os.path.basename(path_interpreter).split('.')[0]
        instancia = self.__fabrica.get_instance(interprete)

        if not instancia:
            raise ProyectoDccError('Este DCC: instancia no esta soportado')

        return instancia

    def crear_esfera(self,nombre):
        self.__dcc_instancia.crear_esfera(nombre)

    def crear_cubo(self,nombre):
        self.__dcc_instancia.crear_cubo(nombre)

    def guardar_escena(self,nombre):
        self.__dcc_instancia.guardar_escena(nombre)
