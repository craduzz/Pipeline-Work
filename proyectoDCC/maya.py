from proyectoDCC import interface_DCC
from interface_DCC import InterfaceDCC

try:
    import maya.cmds as cmds
except ImportError:
    pass

class Maya(InterfaceDCC):
    def __init__(self):
        pass

    def crear_esfera(self, nombre):
        nuevo_nombre = 'up_'+nombre
        cmds.sphere(r=10, name=nuevo_nombre)

    def crear_cubo(self, nombre):
        nuevo_nombre = 'up_'+nombre
        cmds.polyCube(name=nuevo_nombre)

    def guardar_escena(self, path):
        cmds.file(rename=path)
        cmds.file(force=True, type='mayaAscii', save=True)