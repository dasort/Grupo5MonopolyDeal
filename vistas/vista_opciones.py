from PyQt6.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QSpacerItem, QSizePolicy, QFrame
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from controladores.controlador_opciones import ControladorOpciones


class Opciones(QDialog):
    def __init__(self, main_menu, parent=None):
        super().__init__(parent)

        self.main_menu = main_menu
        
        self.setWindowTitle("Opciones")
        self.setGeometry(570, 240, 400, 300)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))

        #Controlador
        self.controlador = ControladorOpciones(self)
        self.controlador.centrar_ventana()

        #Layout
        self.layout = QVBoxLayout()
        self.layout_para_centrar_botones = QVBoxLayout()
        self.layout.addSpacing(10)

        #Titulo
        self.label = QLabel("Ajustes y configuraciones del juego:", self)
        self.layout.addWidget(self.label)
        self.layout.addSpacing(20)

        #Linea
        linea1 = QFrame(self)
        linea1.setFrameShape(QFrame.Shape.HLine)
        linea1.setFrameShadow(QFrame.Shadow.Sunken)
        self.layout.addWidget(linea1)

        self.layout.addSpacing(10)

        #Botones a,b,c ------------
        boton_a = QPushButton("Version prémium", self)
        boton_a.setFixedWidth(250)
        boton_a.setEnabled(False)

        boton_b = QPushButton("Recompensa diaria", self)
        boton_b.setFixedWidth(250)
        boton_b.setEnabled(False)

        boton_c = QPushButton("Activar cheats", self)
        boton_c.setFixedWidth(250)
        boton_c.setEnabled(False)
        #------------

        self.layout_para_centrar_botones.addWidget(boton_a, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_para_centrar_botones.addSpacing(2)
        self.layout_para_centrar_botones.addWidget(boton_b, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_para_centrar_botones.addSpacing(2)
        self.layout_para_centrar_botones.addWidget(boton_c, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addLayout(self.layout_para_centrar_botones)
        self.layout.addSpacing(10)
        
        #Otra Linea: 
        linea1 = QFrame(self)
        linea1.setFrameShape(QFrame.Shape.HLine)
        linea1.setFrameShadow(QFrame.Shadow.Sunken)
        self.layout.addWidget(linea1)

        self.layout.addSpacing(10)

        # Boton Créditos:
        boton_creditos = QPushButton("Créditos", self)
        boton_creditos.clicked.connect(self.controlador.mostrar_creditos)
        self.layout.addWidget(boton_creditos)

        self.layout.addSpacing(10)

        #Otra Linea: 
        linea1 = QFrame(self)
        linea1.setFrameShape(QFrame.Shape.HLine)
        linea1.setFrameShadow(QFrame.Shadow.Sunken)
        self.layout.addWidget(linea1)

        self.layout.addSpacing(10)

        # Volver:
        self.boton_volver = QPushButton("Volver al Menú Principal", self)
        self.boton_volver.clicked.connect(self.controlador.volver)
        self.layout.addWidget(self.boton_volver)
        self.setLayout(self.layout) 