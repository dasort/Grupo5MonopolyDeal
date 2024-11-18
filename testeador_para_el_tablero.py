
# ----------------------------------------------------------------------------------------

# Ejecuten directamente esto para tener ya 3 jugadores cargados con algunas cartas.

# ----------------------------------------------------------------------------------------

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

    # 3 jugadores de prueba:
    jugadores = [
        {
            "nombre": "Jugador 1",
            "dinero": 1000,
            "avatar": "imagenes/ui/perfilRecortado1.png",
            "mano": [
                {
                    "nombre": "Carta 1",
                    "imagen": "imagenes/cartas/propiedadRosa.png",
                    "descripcion_imagen": "imagenes/ui/queHacePropiedades.png"
                },
                {
                    "nombre": "Carta 2",
                    "imagen": "imagenes/cartas/dinero3.png",
                    "descripcion_imagen": "imagenes/ui/queHaceDinero.png"
                },
                {
                    "nombre": "Carta 3",
                    "imagen": "imagenes/cartas/esMiCumpleanos.png",
                    "descripcion_imagen": "imagenes/ui/queHaceEsMiCumpleanos.png"
                },
            ],
            "propiedades": [
                {"imagen": "imagenes/cartas/propiedadRosa.png"},
                {"imagen": "imagenes/cartas/propiedadAzul.png"},
            ],
            "banco": [
                {"imagen": "imagenes/cartas/dinero1.png"},
                {"imagen": "imagenes/cartas/dinero2.png"},
            ],
            "acciones": [
                {"imagen": "imagenes/cartas/alquilerDoble.png"}
            ],
        },
        {
            "nombre": "Jugador 2",
            "dinero": 800,
            "avatar": "imagenes/ui/perfilRecortado5.png",
            "mano": [
                {
                    "nombre": "Carta 1",
                    "imagen": "imagenes/cartas/propiedadAzul.png",
                    "descripcion_imagen": "imagenes/ui/queHacePropiedades.png"
                },
                {
                    "nombre": "Carta 2",
                    "imagen": "imagenes/cartas/tratoForzoso.png",
                    "descripcion_imagen": "imagenes/ui/queHaceTratoForzoso.png"
                },
                {
                    "nombre": "Carta 3",
                    "imagen": "imagenes/cartas/comodinCelesteMarron.png",
                    "descripcion_imagen": "imagenes/ui/queHaceComodin.png"
                },
                {
                    "nombre": "Carta 4",
                    "imagen": "imagenes/cartas/alquilerRojoAmarillo.png",
                    "descripcion_imagen": "imagenes/ui/queHaceAlquiler.png"
                },
            ],
            "propiedades": [
                {"imagen": "imagenes/cartas/propiedadRosa.png"},
                {"imagen": "imagenes/cartas/propiedadAzul.png"},
            ],
            "banco": [
                {"imagen": "imagenes/cartas/dinero1.png"},
                {"imagen": "imagenes/cartas/dinero2.png"},
            ],
            "acciones": [
                {"imagen": "imagenes/cartas/alquilerDoble.png"}
            ],
        },
        {
            "nombre": "Jugador 3",
            "dinero": 1200,
            "avatar": "imagenes/ui/perfilRecortado3.png",
            "mano": [
                {
                    "nombre": "Carta 1",
                    "imagen": "imagenes/cartas/propiedadRosa.png",
                    "descripcion_imagen": "imagenes/ui/queHaceAlquilerDoble.png"
                },
                {
                    "nombre": "Carta 2",
                    "imagen": "imagenes/cartas/comodinMulticolor.png",
                    "descripcion_imagen": "imagenes/ui/queHaceComodin.png"
                },
                {
                    "nombre": "Carta 3",
                    "imagen": "imagenes/cartas/alquilerMulticolor.png",
                    "descripcion_imagen": "imagenes/ui/queHaceAlquiler.png"
                },
            ],
            "propiedades": [
                {"imagen": "imagenes/cartas/propiedadRosa.png"},
                {"imagen": "imagenes/cartas/propiedadAzul.png"},
            ],
            "banco": [
                {"imagen": "imagenes/cartas/dinero1.png"},
                {"imagen": "imagenes/cartas/dinero2.png"},
            ],
            "acciones": [
                {"imagen": "imagenes/cartas/alquilerDoble.png"}
            ],
        },
    ]

    # Inicializar la ventana principal
    main_menu = MainMenu()
    ventana = Tablero(main_menu, 1000, jugadores)
    ventana.show()

    # Ejecutar la aplicación
    sys.exit(app.exec())