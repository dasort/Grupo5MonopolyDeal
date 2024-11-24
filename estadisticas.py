from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QIcon, QGuiApplication

class Estadisticas(QDialog):
    def __init__(self, main_menu, parent=None):
        super().__init__(parent)
        self.main_menu = main_menu
        self.setWindowTitle("Estadisticas")
        self.setGeometry(570, 240, 400, 300)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))
        self.centrar_ventana()

#    ^
#   / \
#    |
#    |
#    |

# Por hacer.




    def volver(self):
        self.hide()
        self.main_menu.show()
    
    def centrar_ventana(self):
        """Método para centrar la ventana en el centro de la pantalla."""
        forma_pantalla = QGuiApplication.primaryScreen().availableGeometry()
        forma_ventana = self.frameGeometry()
        centro_pantalla = forma_pantalla.center()
        forma_ventana.moveCenter(centro_pantalla)
        self.move(forma_ventana.topLeft())