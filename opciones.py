from PyQt6.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon

class Opciones(QDialog):
    def __init__(self, main_menu, parent=None):
        super().__init__(parent)
        self.main_menu = main_menu
        self.setWindowTitle("Opciones")
        self.setGeometry(300, 200, 600, 400)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.adjustSize()
        self.setMinimumSize(600, 400)
        
        self.main_widget = QWidget(self)
        self.main_widget.setLayout(self.layout)

        self.label = QLabel("Ajustes y configuraciones del juego", self)
        self.layout.addWidget(self.label)

        self.btn_volver = QPushButton("Volver al Menú Principal", self)
        self.btn_volver.clicked.connect(self.volver)
        self.layout.addWidget(self.btn_volver)

    def volver(self):
        self.hide()
        self.main_menu.show()