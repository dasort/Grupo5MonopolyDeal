from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QSoundEffect
from vistas.vista_main_menu import MainMenu
from controladores.controlador_crear_partida import ControladorCrearPartida
from controladores.controlador_opciones import ControladorOpciones
from controladores.controlador_estadisticas import ControladorEstadisticas
from controladores.controlador_como_juego import ControladorComoJuego
from controladores.controlador_iniciar_sesion import Controlador_iniciar_sesion

class ControladorMainMenu:
    def __init__(self): 
        super().__init__()
        self.__vista = MainMenu(self)

        self.__volumen = 1 # <-- Máximo por default.
        
        # Configuración del sonido:
        self.sound_effect = QSoundEffect()
        self.sound_effect.setSource(QUrl.fromLocalFile("imagenes/sonido/click.wav"))
        self.sound_effect.setVolume(self.__volumen)
        
        self.__vista.show()

    # Sonido de los botones:
    def sonido_click(self):
        self.sound_effect.play()
    
    # Botón crear partida:
    def mostrar_crear_partida(self):
        self.sonido_click()
        self.__vista.hide()
        ControladorCrearPartida(self)    

    # Botón opciones:
    def mostrar_opciones(self):
        self.sonido_click()
        self.__vista.hide()
        ControladorOpciones(self) # <-- Así puedo actualizar el volumen.
        
    # Botón cómo jugar:
    def mostrar_como_juego(self):
        self.sonido_click()
        self.__vista.hide()
        ControladorComoJuego(self)
    
    # Botón estadísticas:
    def mostrar_estadisticas_inicio_sesion(self):
        self.sonido_click()
        self.__vista.hide()
        controlador_iniciar_sesion = Controlador_iniciar_sesion(main_menu=self)
        controlador_iniciar_sesion.inicializar_vista() # <-- 
    
    # Getters:
    def get_volumen(self):
        return self.__volumen
    
    def get_vista(self):
        return self.__vista

    # Setters:
    def set_volumen(self, volumen):
        self.__volumen = volumen
        self.sound_effect.setVolume(self.__volumen)