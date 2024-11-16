from PyQt6.QtWidgets import QApplication
from tablero_pantalla import Tablero
from main_menu import MainMenu

main_menu = MainMenu

# Si parece confuso es porque agregué las cartas de propiedades, banco y acciones.
jugadores = [
    {"nombre": "Jugador 1", "dinero": 1000, "avatar": "imagenes/ui/perfilRecortado1.png", "mano": ["Carta 1", "Carta 2", "Carta 3"],
     "propiedades": [{"imagen": "imagenes/cartas/propiedadRosa.png"},{"imagen": "imagenes/cartas/propiedadAzul.png"}],
     "banco": [{"imagen": "imagenes/cartas/dinero1.png"},{"imagen": "imagenes/cartas/dinero2.png"}],
     "acciones": [{"imagen": "imagenes/cartas/alquilerDoble.png"}]},
    
    {"nombre": "Jugador 2", "dinero": 800, "avatar": "imagenes/ui/perfilRecortado5.png", "mano": ["Carta 4", "Carta 5", "Carta 6"],
    "propiedades": [{"imagen": "imagenes/cartas/propiedadRosa.png"},{"imagen": "imagenes/cartas/propiedadAzul.png"}],
     "banco": [{"imagen": "imagenes/cartas/dinero1.png"},{"imagen": "imagenes/cartas/dinero2.png"}],
     "acciones": [{"imagen": "imagenes/cartas/alquilerDoble.png"}]},
    
    {"nombre": "Jugador 3", "dinero": 1200, "avatar": "imagenes/ui/perfilRecortado3.png", "mano": ["Carta 7", "Carta 8", "Carta 9"],
    "propiedades": [{"imagen": "imagenes/cartas/propiedadRosa.png"},{"imagen": "imagenes/cartas/propiedadAzul.png"}],
     "banco": [{"imagen": "imagenes/cartas/dinero1.png"},{"imagen": "imagenes/cartas/dinero2.png"}],
     "acciones": [{"imagen": "imagenes/cartas/alquilerDoble.png"}]},
]

app = QApplication([])
ventana = Tablero(main_menu, 1000, jugadores)
ventana.show()
app.exec()
