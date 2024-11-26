from vistas.vista_opciones import Opciones


class ControladorOpciones:
    def __init__(self, main_menu):
        self.__main_menu = main_menu
        self.__vista = Opciones(self)
        self.__vista.show()

    def volver(self):
        self.__vista.hide()
        var = self.__main_menu()