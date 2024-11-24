from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QIcon

class Estadisticas(QDialog):
    def __init__(self, main_menu, parent=None):
        super().__init__(parent)
        self.main_menu = main_menu
        self.setWindowTitle("Estadisticas")
        self.setGeometry(570, 240, 400, 300)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))

#    ^
#   / \
#    |
#    |
#    |

# Por hacer.