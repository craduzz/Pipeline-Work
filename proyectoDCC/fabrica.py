from proyectoDCC.houdini import Houdini
from proyectoDCC.maya import Maya




class Fabrica:
    def __init__(self):
        self.__fabrica = {
            'maya': Maya,
            'houdini':Houdini
        }
    def get_instance(self,nombre):
        if 'houdini' in nombre:
            nombre = 'houdini'

        #esta linea es por que asi se llama la version no comercial del houdini
        if 'hindie' in nombre:
            nombre = 'houdini'
        return self.__fabrica.get(nombre,None)
