import sys
from PyQt6.QtWidgets import QApplication
from controladores.controlador_iniciar_sesion import Controlador_iniciar_sesion
from vistas.vista_main_menu import MainMenu
app = QApplication(sys.argv)
main_menu=MainMenu() 

class MainMenu_ext: 
    def __init__(self): 
        self.controlador = Controlador_iniciar_sesion(main_menu) 
    def abrirSegunda(self):
        self.controlador.abrirSegunda()

#app = QApplication(sys.argv)
main_menu = MainMenu_ext()

app.exec()