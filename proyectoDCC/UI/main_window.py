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
        self.setFixedSize(400, 200)

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
                print('Error Code: Caps')

        guardar_metadata_btn = QtWidgets.QPushButton('Guardar Metadata')
        guardar_metadata_btn.clicked.connect(self.guardar_metadata)
        vertical_layout.addWidget(guardar_metadata_btn)

        exportar_alembic_btn = QtWidgets.QPushButton('Exportar alembic')
        exportar_alembic_btn.clicked.connect(self.exportar_alembic)
        vertical_layout.addWidget(exportar_alembic_btn)


    def guardar_metadata(self):
        self.__main.save_metadata()

    def exportar_alembic(self):
        nombre, opcion = QtWidgets.QInputDialog().getText(
            self,
            'Exportar alembic',
            'Nombre del alembic a exportar',
            QtWidgets.QLineEdit.Normal
        )
        if opcion:
            self.__main.exportar_alembic(nombre)


    def crear_esfera(self):
        nombre, opcion = QtWidgets.QInputDialog().getText(
            self,
            'Nombre',
            'Nombre de la esfera a crear',
            QtWidgets.QLineEdit.Normal
        )
        if opcion:
            self.__main.crear_esfera(nombre)

    def crear_cubo(self):
        nombre, opcion = QtWidgets.QInputDialog().getText(
            self,
            'Nombre',
            'Nombre del cubo a crear',
            QtWidgets.QLineEdit.Normal
        )
        if opcion:
            self.__main.crear_cubo(nombre)

    def guardar_escena(self):
        nombre, opcion = QtWidgets.QInputDialog().getText(
            self,
            'Nombre',
            'Nombre de la escena a guardar',
            QtWidgets.QLineEdit.Normal
        )
        if opcion:
            self.__main.guardar_escena(nombre)


def main():
    app = QtWidgets.QApplication()
    dcc_widget = DccWidget()
    dcc_widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
