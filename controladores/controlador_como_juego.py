from vistas.vista_como_juego import ComoJuego


class ControladorComoJuego:
    
    def __init__(self, main_menu): 
        super().__init__()
        self.__main_menu = main_menu
        self.__vista = ComoJuego(self)
        self.__vista.show()
    
    def volver(self):
        self.__vista.hide()
        var = self.__main_menu.get_vista().show()
