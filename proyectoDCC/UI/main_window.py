import sys
import inspect
from PySide2 import QtWidgets
from proyectoDCC.main import Main
from proyectoDCC.interface_DCC import InterfaceDCC

class DccWidget(QtWidgets.QWidget):
    
    def __init__(self):
        super(DccWidget, self).__init__()

        self.__main = Main()

        self.setWindowTitle('Pipeline')
        self.setFixedSize(400,200)

        vertical_layout = QtWidgets.QVBoxLayout()
        self.setLayout(vertical_layout)

        funciones_interface = [func[0] for func in inspect.getmembers(InterfaceDCC, predicate=inspect.isfunction)]
        for nombre_funcion in funciones_interface:
            try:
                nombres = [nom.capitalize() for nom in nombre_funcion.split('_')]
                nombre_btn = ' '.join(nombres)
                app_btn = QtWidgets.QPushButton(nombre_btn)
                ui_func = self.__getattribute__(nombre_funcion)
                app_btn.clicked.connect(ui_func)
                vertical_layout.addWidget(app_btn)
            except AttributeError:
                #print('Error Code: Capitan')
                pass


    def crear_esfera(self):
        nombre,opcion = QtWidgets.QInputDialog().getText(
            self,
            'Nombre',
            'Nombre de la esfera a crear',
            QtWidgets.QLineEdit.Normal
        )
        if opcion:
            self.__main.crear_esfera()

    def crear_cubo(self):
        nombre,opcion = QtWidgets.QInputDialog().getText(
            self,
            'Nombre',
            'Nombre del cubo a crear',
            QtWidgets.QLineEdit.Normal
        )
        if opcion:
            self.__main.crear_cubo()

    def guardar_escena(self):
        nombre,opcion = QtWidgets.QInputDialog().getText(
            self,
            'Nombre',
            'Nombre de la escena a guardar',
            QtWidgets.QLineEdit.Normal
        )
        if opcion:
            self.__main.guardar_escena()

def main():
    app = QtWidgets.QApplication()
    dcc_widget = DccWidget()
    dcc_widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()