import os.path

from proyectoDCC.interface_DCC import InterfaceDCC

try:
    import nuke
except ImportError:
    pass

class Nuke(InterfaceDCC):

    def __init__(self):
        pass

    def crear_esfera(self,nombre):
        viewer = nuke.toNode('Viewer1')
        sphere = nuke.nodes.Sphere(name=nombre)

        viewer.setInput(0,sphere)

    def crear_cubo(self, nombre):
        viewer = nuke.toNode('Viewer1')
        cube = nuke.nodes.Cube(name=nombre)

        viewer.setInput(0, cube)

    def guardar_escena(self, shot_folder,name):
        print(shot_folder)
        scene_file_path = os.path.join(shot_folder, 'nuke\\' + name + '.nknc')

        dir_path = os.path.dirname(scene_file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        #nuke.message("Advertencia: Este archivo sera guardado para Nuke non-commercial")
        nuke.scriptSaveAs(filename=scene_file_path,overwrite=-1)
        return scene_file_path

    #esta parte no la pude probar por que el nodo WriteGeo esta bloqueado en la version no comercial.
    def exportar_alembic(self, shot_folder, name):

        alembic_file_path = os.path.join(shot_folder, 'nuke\\' + name + '.abc')

        dir_path = os.path.dirname(alembic_file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        write = nuke.nodes.WriteGeo(file=alembic_file_path,file_type='abc',writeGeometries=True,storageFormat='Ogawa')
        write.Execute()

    def crear_video(self,shot_folder,nombre,path):

        dash_ = '\lp'
        dash_ = dash_.replace('lp','')

        path = path.replace(dash_,'/')+'/'

        for seq in nuke.getFileNameList(path):
            readNode = nuke.nodes.Read()
            readNode.knob('file').fromUserText(path + seq)

        readNode.knob('name').setText(nombre)

        viewer = nuke.toNode('Viewer1')
        viewer.setInput(0, readNode)

        write_n = nuke.nodes.Write(file_type='mov')
        readNode.setInput(0, write_n)

        write_n.knob('mov64_codec').setValue('h.264')

        scene_file_path = os.path.join(shot_folder, 'nuke\\' + nombre + '.mov')

        dir_path = os.path.dirname(scene_file_path)
        #print(dir_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        write_n.knob('file').setValue(scene_file_path)
        last_frame = readNode.knob('last').getValue()
        nuke.execute("Write1", 1, int(last_frame), 1)