#from interface_DCC import InterfaceDCC
import os.path

from proyectoDCC.interface_DCC import InterfaceDCC

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

    def guardar_escena(self, shot_folder,name):
        scene_file_path = os.path.join(shot_folder,'houdini\\'+name+'.hip')

        dir_path = os.path.dirname(scene_file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        hou.hipFile.save(file_name=scene_file_path)
        return scene_file_path
