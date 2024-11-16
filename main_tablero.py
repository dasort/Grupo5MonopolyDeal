from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont, QFontDatabase
from tablero_pantalla import Tablero
from main_menu import MainMenu
import sys

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Fuente personalizada:
    font_id = QFontDatabase.addApplicationFont("imagenes/ui/OMDFMP+KabelMediumITC.ttf")
    if font_id == -1:
        print("Error: No se pudo cargar la fuente personalizada.")
    else:
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        app_font = QFont(font_family)
        app_font.setPointSize(12) # <-- Tamaño de la fuente.
        app.setFont(app_font)     # <-- Aplicar la fuente a toda la aplicación.

    # Jugadores de prueba:
    jugadores = [
        {"nombre": "Jugador 1", "dinero": 1000, "avatar": "imagenes/ui/perfilRecortado1.png", "mano": ["Carta 1", "Carta 2", "Carta 3"],
         "propiedades": [{"imagen": "imagenes/cartas/propiedadRosa.png"}, {"imagen": "imagenes/cartas/propiedadAzul.png"}],
         "banco": [{"imagen": "imagenes/cartas/dinero1.png"}, {"imagen": "imagenes/cartas/dinero2.png"}],
         "acciones": [{"imagen": "imagenes/cartas/alquilerDoble.png"}]},
        
        {"nombre": "Jugador 2", "dinero": 800, "avatar": "imagenes/ui/perfilRecortado5.png", "mano": ["Carta 4", "Carta 5", "Carta 6"],
         "propiedades": [{"imagen": "imagenes/cartas/propiedadRosa.png"}, {"imagen": "imagenes/cartas/propiedadAzul.png"}],
         "banco": [{"imagen": "imagenes/cartas/dinero1.png"}, {"imagen": "imagenes/cartas/dinero2.png"}],
         "acciones": [{"imagen": "imagenes/cartas/alquilerDoble.png"}]},
        
        {"nombre": "Jugador 3", "dinero": 1200, "avatar": "imagenes/ui/perfilRecortado3.png", "mano": ["Carta 7", "Carta 8", "Carta 9"],
         "propiedades": [{"imagen": "imagenes/cartas/propiedadRosa.png"}, {"imagen": "imagenes/cartas/propiedadAzul.png"}],
         "banco": [{"imagen": "imagenes/cartas/dinero1.png"}, {"imagen": "imagenes/cartas/dinero2.png"}],
         "acciones": [{"imagen": "imagenes/cartas/alquilerDoble.png"}]},
    ]

    # Inicializar la ventana principal
    main_menu = MainMenu()
    ventana = Tablero(main_menu, 1000, jugadores)
    ventana.show()

    # Ejecutar la aplicación
    sys.exit(app.exec())