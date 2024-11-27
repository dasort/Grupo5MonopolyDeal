from vistas.vista_opciones import Opciones


class ControladorOpciones:
    def __init__(self, main_menu):
        self.__main_menu = main_menu
        self.__vista = Opciones(self)
        self.__vista.show()

    def volver(self):
        self.__vista.hide()
        #var = self.__main_menu()
        self.__main_menu.get_vista().show() # <-- Así trabajo con el mismo de antes.
    
    def cambiar_volumen(self, valor):
        volumen = valor / 100 # <-- Para convertirlo en un número flotante, el cual setVolume puede manejar (0.0 ~ 1.0).
        self.__main_menu.set_volumen(volumen)
        self.__vista.cambiar_pixmap_volumen()
    
    def obtener_volumen(self):
        return int (self.__main_menu.get_volumen() * 100)
    
    def alternar_volumen(self):
        if self.obtener_volumen() >= 50:
            self.__vista.cambiar_icono("apagado")
            self.cambiar_volumen(0)
        else:
            self.__vista.cambiar_icono("alto")
            self.cambiar_volumen(100)