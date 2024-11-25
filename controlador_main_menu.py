from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtMultimedia import QMediaPlayer
from crear_partida import CrearPartida
from como_juego import ComoJuego
from opciones import Opciones
from estadisticas import Estadisticas


class controlador_main_menu (QMainWindow):
    def __init__(self): 
        super().__init__()
        
        
        self.player = QMediaPlayer()
        
        #funciones de los botones
        self.boton_crear_partida=CrearPartida(self)
        self.boton_opciones=Opciones(self)
        self.boton_como_juego=ComoJuego(self)
        self.boton_estadisticas=Estadisticas(self)
    
    #sonido de botones
    def sonido_click(self):
        self.player.stop()
        self.player.play()
    
    #boton crear partida    
    def mostrar_crear_partida(self):
        self.sonido_click()
        self.hide()
        self.boton_crear_partida.exec()
    
    #boton opciones:
    
    def mostrar_opciones(self):
        self.sonido_click()
        self.hide()
        self.boton_opciones.exec()
        
    #boton como jugar:
    def mostrar_como_juego(self):
        self.sonido_click()
        self.hide()
        self.boton_como_juego.exec()
    
    #boton estadisticas:
    def mostrar_estadisticas_inicio_sesion(self):
        self.sonido_click()
        self.hide()
        self.boton_estadisticas.exec()
