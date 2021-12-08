import os.path
import sys
import json
from random import randrange

import ffmpeg

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

        if not instancia:
            raise ProyectoDccError('Este DCC: instancia no esta soportado')

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

    def create_video(self):
        path = input('Please enter the absolute path of the image sequence: ')
        fps = 0
        while fps <= 0:
            fps = input('Now please add the framerate of the video: ')
            if fps <= 0:
                print(f"{fps} is not a valid framerate, please add a framerate higher than 1.")
        name = input('Please add the name of the video to create: ')

        name.replace(' ','_')
        self.__render_vid(path,fps,name)



    def __render_vid(self,path,fps,name):
        ffmpeg.input(path,pattern_type = 'glob', framerate=fps).output(f'{name}.mp4').run()