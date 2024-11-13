from PyQt6.QtWidgets import QApplication
from tablero_pantalla import Tablero

jugadores = [
    {"nombre": "Jugador 1", "dinero": 1000, "avatar": "avatar1.jpg", "mano": ["Carta 1", "Carta 2", "Carta 3"]},
    {"nombre": "Jugador 2", "dinero": 800, "avatar": "avatar2.jpg", "mano": ["Carta 4", "Carta 5", "Carta 6"]},
    {"nombre": "Jugador 3", "dinero": 1200, "avatar": "avatar3.jpg", "mano": ["Carta 7", "Carta 8", "Carta 9"]},
]

app = QApplication([])
ventana = Tablero(1000, jugadores)
ventana.show()
app.exec()
