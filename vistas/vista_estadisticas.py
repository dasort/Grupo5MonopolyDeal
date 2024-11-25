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

        #self.main_layout.addWidget(self.titulo_label)
        #self.main_layout.addLayout(self.layout_nombre)
        #self.main_layout.addLayout(self.layout_partidas_jugadas)
        #self.main_layout.addLayout(self.layout_partidas_ganadas)
        #self.main_layout.addWidget(self.boton_iniciar_sesion)
        #self.main_layout.addWidget(self.boton_volver)

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