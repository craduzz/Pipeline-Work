import abc


class InterfaceDCC(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def crear_esfera(self):
        pass

    @abc.abstractmethod
    def crear_cubo(self):
        pass

    @abc.abstractmethod
    def guardar_escena(self):
        pass
