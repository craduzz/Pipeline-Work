import os.path
import sys
import json
from random import randrange


from . import fabrica



class ProyectoDccError(Exception):
    pass


class Main:

    MAIN_FOLDER = 'G:\\MayaPluginTest'

    def __init__(self):
        self.__scene_path = None
        self.__interprete = None
        self.__fabrica = fabrica.Fabrica()
        self.__numero_shot = str(randrange(100,999))
        self.__shot_folder = os.path.join(self.MAIN_FOLDER,self.__numero_shot)
        self.__dcc_instancia = self.get_dcc_instancia()()

    def get_dcc_instancia(self):
        path_interpreter = sys.executable
        __interprete = os.path.basename(path_interpreter).split('.')[0]
        instancia = self.__fabrica.get_instance(__interprete)


        print(__interprete)
        print("''''''''''''''''''''''''''''''''''''")
        if not instancia:
            raise ProyectoDccError('Este DCC:'+__interprete + 'instancia no esta soportado')

        return instancia

    def crear_esfera(self,nombre):
        self.__dcc_instancia.crear_esfera(nombre)

    def crear_cubo(self,nombre):
        self.__dcc_instancia.crear_cubo(nombre)

    def guardar_escena(self,nombre):
        self.__scene_path = self.__dcc_instancia.guardar_escena(self.__shot_folder,nombre)

    def save_metadata(self):
        if not self.__scene_path:
            raise ValueError('La escena no ha sido guardada. No se puede guardar la metadata')
        metadata = self.__get_metadata()
        data = {}
        meta_dir = os.path.dirname(self.__scene_path)
        meta_archivo = os.path.join(meta_dir,'metadata.json')
        if os.path.exists(meta_archivo):
            with open(meta_archivo,'r') as archivo:
                data = json.load(archivo)

        for key,value in metadata.items():
            data[key] = value

        with open(meta_archivo,'w+') as archivo:
            json.dump(data, archivo)


        print('Metadata Guardada')

    def __get_metadata(self):
        #for key,value in os.environ.items():
        #    print(f'key --> {key}\nValue --> {value}')
        data = {
            'escena':self.__scene_path,
            'DCC':self.__interprete,
            'usuario':os.getenv('USERNAME',''),
            'shot':self.__numero_shot,
            'os':os.getenv('OS','')
        }
        return data

    def exportar_alembic(self, nombre):
        if self.__dcc_instancia.__getattribute__('exportar_alembic'):
            self.__dcc_instancia.exportar_alembic(self.__shot_folder, nombre)
        else:
            print('La instancia no tiene este metodo')


    def crear_video(self,nombre,path):
        if self.__dcc_instancia.__getattribute__('crear_video'):
            self.__dcc_instancia.crear_video(self.__shot_folder, nombre,path)
        else:
            print('La instancia no tiene este metodo')

    def test_cmd(self):
        print("sirve")
