import os.path
import sys
import json
from random import randrange


from . import fabrica



class ProyectoDccError(Exception):
    pass


class Main:

    MAIN_FOLDER = 'G:\\MayaPluginTest'
    totalFilesM = 0
    totalFilesH = 0
    totalFilesN = 0
    totalFiles  = 0
    totalDir    = 0

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

    def crear_resumen(self):
        typeOfFile = ''
        TEXT_FILE_NAME = 'resumenDeProduccion.txt'
        if os.path.exists(self.MAIN_FOLDER+'/'+TEXT_FILE_NAME):
            os.remove(self.MAIN_FOLDER+'/'+TEXT_FILE_NAME)

        with open(f'{self.MAIN_FOLDER}/{TEXT_FILE_NAME}', 'a')as f:
            f.writelines("lista de los directorios de los archivos disponibles: \n")


        for base, dirs, files in os.walk(self.MAIN_FOLDER):
            print("buscando en: ",base)
            for directorios in dirs:
                print(f"sub dirs: {directorios}")
                self.totalDir += 1

                if 'maya' in directorios:
                    typeOfFile = 'm'

                elif 'houdini' in directorios:
                    typeOfFile = 'h'

                elif 'nuke' in directorios:
                    typeOfFile = 'n'

            for Files in files:
                print(f"sub files: {Files}")

                with open(f'{self.MAIN_FOLDER}/{TEXT_FILE_NAME}','a')as f:
                    f.writelines(f"{base}/{Files} \n")

                if typeOfFile == 'm':
                    self.totalFilesM += 1
                elif typeOfFile == 'h':
                    self.totalFilesH += 1
                elif typeOfFile =='n':
                    self.totalFilesN += 1

                self.totalFiles = self.totalFilesN + self.totalFilesH + self.totalFilesM

        #print(f" files: {self.totalFiles}, dirs: {self.totalDir}")

        with open(f'{self.MAIN_FOLDER}/{TEXT_FILE_NAME}', 'a')as f:
            f.writelines(f'\n\nTotal de archivos \n Maya: {self.totalFilesM} \n Houdini: {self.totalFilesH} \n Nuke: {self.totalFilesN} \n  Total de archivos: {self.totalFiles}')

        print(f" maya files: {self.totalFilesM}, houdini files: {self.totalFilesH}, nuke files: {self.totalFilesN}, total files: {self.totalFiles} ")
