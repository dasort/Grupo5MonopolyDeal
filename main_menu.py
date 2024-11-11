from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from crear_partida import CrearPartida
from opciones import Opciones
from iniciar_sesion import IniciarSesion

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monopoly Deal")
        self.setGeometry(300, 200, 600, 400)
        self.setWindowIcon(QIcon("monopoly_icon.png"))

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)

        self.titulo_label = QLabel("Monopoly Deal", self)
        self.titulo_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.titulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.titulo_label)

        self.boton_crear_partida = QPushButton("Crear una Partida", self)
        self.boton_crear_partida.setStyleSheet("font-size: 20px;")
        self.boton_crear_partida.clicked.connect(self.mostrar_crear_partida)
        self.layout.addWidget(self.boton_crear_partida)

        self.boton_opciones = QPushButton("Opciones", self)
        self.boton_opciones.setStyleSheet("font-size: 20px;")
        self.boton_opciones.clicked.connect(self.mostrar_opciones)
        self.layout.addWidget(self.boton_opciones)

        self.boton_iniciar_sesion = QPushButton("Iniciar Sesión o Crear Usuario", self)
        self.boton_iniciar_sesion.setStyleSheet("font-size: 20px;")
        self.boton_iniciar_sesion.clicked.connect(self.mostrar_iniciar_sesion)
        self.layout.addWidget(self.boton_iniciar_sesion)

        # Crear instancias de las ventanas secundarias
        self.crear_partida_window = CrearPartida(self)
        self.opciones_window = Opciones(self)
        self.iniciar_sesion_window = IniciarSesion(self)

    def mostrar_crear_partida(self):
        self.hide()
        self.crear_partida = CrearPartida(self) 
        self.crear_partida.exec()

    def mostrar_opciones(self):
        self.hide()
        self.opciones = Opciones(self)
        self.opciones.exec()

    def mostrar_iniciar_sesion(self):
        self.hide()
        self.iniciar_sesion = IniciarSesion(self)
        self.iniciar_sesion.exec()
