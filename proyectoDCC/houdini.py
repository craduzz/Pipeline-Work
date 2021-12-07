from proyectoDCC import interface_DCC
from interface_DCC import InterfaceDCC

try:
    import hou
except ImportError:
    pass


class Houdini(InterfaceDCC):

    def __init__(self):
        pass

    def crear_esfera(self,nombre):
        obj_node = hou.node('obj')
        geo_node = obj_node.createNode('geo')
        sphere_node = geo_node.createNode('sphere')
        sphere_node.setName(nombre)

    def crear_cubo(self, nombre):
        obj_node = hou.node('obj')
        geo_node = obj_node.createNode('geo')
        sphere_node = geo_node.createNode('box')
        sphere_node.setName(nombre)

    def guardar_escena(self, path):
        hou.hipfile.save(file_name=path)
