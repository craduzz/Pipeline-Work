import abc


#python 3.x
#----------------------------------------------
class InterfaceDCC(metaclass=abc.ABCMeta):
#----------------------------------------------

#python 2.x
#----------------------------------------------
#class InterfaceDCC(object):
#    __metaclass__ = abc.ABCMeta
#----------------------------------------------


    @abc.abstractmethod
    def crear_esfera(self):
        pass

    @abc.abstractmethod
    def crear_cubo(self):
        pass

    @abc.abstractmethod
    def guardar_escena(self):
        pass


