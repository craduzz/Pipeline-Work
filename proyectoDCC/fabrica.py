from proyectoDCC.houdini import Houdini
from proyectoDCC.maya import Maya
from proyectoDCC.nuke import Nuke




class Fabrica:
    def __init__(self):
        self.__fabrica = {
            'maya': Maya,
            'houdini':Houdini,
            'nuke':Nuke
        }
    def get_instance(self,nombre):
        if 'houdini' in nombre:
            nombre = 'houdini'
        #esta linea es por que asi se llama la version no comercial de houdini
        if 'hindie' in nombre:
            nombre = 'houdini'

        if 'Nuke' in nombre:
            nombre = 'nuke'

        return self.__fabrica.get(nombre,None)
