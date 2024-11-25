
from vistas.vista_iniciar_sesion import IniciarSesion
from vistas.vista_main_menu import MainMenu
from controladores.controlador_crear_cuenta import Controlador_crear_cuenta


class Controlador_iniciar_sesion():
    def __init__(self,main_menu):
        self.main_menu = main_menu
        self._vista = IniciarSesion(self)  
        self._vista.show()
        
        
    def abrirSegunda(self):
        self._var = Controlador_crear_cuenta()
        self._vista.close()
        
        


    
    






