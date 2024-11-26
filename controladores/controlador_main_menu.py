from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QSoundEffect
from vistas.vista_main_menu import MainMenu
from controladores.controlador_crear_partida import ControladorCrearPartida
from controladores.controlador_opciones import ControladorOpciones
# from controladores.controlador_estadistica import ControladorEstadística
from controladores.controlador_como_juego import ControladorComoJuego


class ControladorMainMenu:
    def __init__(self): 
        super().__init__()
        self.__vista = MainMenu(self)

        # Configuración del sonido:
        self.sound_effect = QSoundEffect()
        self.sound_effect.setSource(QUrl.fromLocalFile("imagenes/sonido/click.wav"))
        self.sound_effect.setVolume(50)
        
        self.__vista.show()

    # Sonido de los botones:
    def sonido_click(self):
        self.sound_effect.play()
    
    # Botón crear partida:
    def mostrar_crear_partida(self):
        self.sonido_click()
        self.__vista.hide()
        ControladorCrearPartida(ControladorMainMenu)    

    # Botón opciones:
    def mostrar_opciones(self):
        self.sonido_click()
        self.__vista.hide()
        ControladorOpciones(ControladorMainMenu)
        
    # Botón cómo jugar:
    def mostrar_como_juego(self):
        self.sonido_click()
        self.__vista.hide()
        ControladorComoJuego(ControladorMainMenu)
    
    # Botón estadísticas:
    def mostrar_estadisticas_inicio_sesion(self):
        self.sonido_click()
        self.__vista.hide()
        # ControladorEstadisticas(self)