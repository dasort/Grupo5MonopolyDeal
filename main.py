import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont, QFontDatabase
from controladores.controlador_main_menu import ControladorMainMenu


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Fuente personalizada:
    path_a_font_id = Path(__file__).resolve()
    path_a_font_id = path_a_font_id.parent
    path_a_font_id = path_a_font_id / "multimedia/ui/OMDFMP+KabelMediumITC.ttf"
    font_id = QFontDatabase.addApplicationFont(path_a_font_id.as_posix())
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
    app_font = QFont(font_family)
    app_font.setPointSize(12) # <-- Tamaño de la fuente.
    app.setFont(app_font)     # <-- Aplicar la fuente a toda la aplicación.

    # Inicializar la ventana principal:
    try:
        controlador = ControladorMainMenu()
    except Exception as e:
        print(f"\n(¡Error!): No se pudo inicializar el programa: {e}\n")
        sys.exit(1)

    sys.exit(app.exec())