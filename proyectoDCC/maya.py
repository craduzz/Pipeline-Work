import os.path

from proyectoDCC.interface_DCC import InterfaceDCC

import maya.standalone as standalone
import maya.cmds as cmds

standalone.initialize(name='python')
cmds.file(f=True, new=True)

'''
try:
    import maya.standalone as standalone
    standalone.initialize(name='python')
    
    print("maya standalone imported successfully")
except:
    pass

try:
    import maya.cmds as cmds

    cmds.file(f=True, new=True)
except ImportError:
    pass
'''


class Maya(InterfaceDCC):


    def __init__(self):
        pass

    def crear_esfera(self, nombre):
        nuevo_nombre = 'up_'+nombre
        cmds.polySphere(r=1, n=nuevo_nombre)

    def crear_cubo(self, nombre):
        nuevo_nombre = 'up_'+nombre
        cmds.polyCube(name=nuevo_nombre)

    def guardar_escena(self, shot_folder,name):
        scene_file_path = os.path.join(shot_folder,'maya\\'+name+'.ma')

        dir_path = os.path.dirname(scene_file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        cmds.file(rename=scene_file_path)
        cmds.file(force=True, type='mayaAscii', save=True)
        print('Archivo guardado exitosamente')
        return scene_file_path

    def exportar_alembic(self, shot_folder, name):
        alembic_file_path = os.path.join(shot_folder, 'maya\\' + name + '.abc')

        dir_path = os.path.dirname(alembic_file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        start_frame = cmds.playbackOptions(q=True, min=True)
        end_frame = cmds.playbackOptions(q=True, max=True)

        cmds.AbcExport(j=f"-frameRange {start_frame} {end_frame} -dataFormat Ogawa -file {alembic_file_path}")

    def crear_video(self, shot_folder, nombre, path):
        print("Esta opcion no esta disponible en este DCC, solo en Nuke")
        cmds.confirmDialog(message="Esta opcion no esta disponible en este DCC, solo en Nuke")