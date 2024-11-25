from PyQt6.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QSpacerItem, QSizePolicy, QFrame, QMessageBox
from PyQt6.QtGui import QIcon, QGuiApplication
from PyQt6.QtCore import Qt

class Opciones(QDialog):
    def __init__(self, main_menu, parent=None):
        super().__init__(parent)
        self.main_menu = main_menu
        self.setWindowTitle("Opciones")
        self.setGeometry(570, 240, 400, 300)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))
        self.centrar_ventana()

        # ---

        self.layout = QVBoxLayout()
        self.layout_para_centrar_botones = QVBoxLayout()

        # ---
        
        self.layout.addSpacing(10)
        
        # Título:
        self.label = QLabel("Ajustes y configuraciones del juego:", self)
        self.layout.addWidget(self.label)
        
        self.layout.addSpacing(20)
        
        # Literalmente una línea:
        linea1 = QFrame(self)
        linea1.setFrameShape(QFrame.Shape.HLine)
        linea1.setFrameShadow(QFrame.Shadow.Sunken)
        self.layout.addWidget(linea1)
        
        self.layout.addSpacing(10)
        
        # Separador:
        # self.layout.addSpacerItem(QSpacerItem(20, 400, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # Boton a:
        boton_a = QPushButton("Version prémium", self)
        boton_a.setFixedWidth(250)
        boton_a.setEnabled(False)
        #self.layout.addWidget(boton_a)
        
        # Boton b:
        boton_b = QPushButton("Recompensa diaria", self)
        boton_b.setFixedWidth(250)
        boton_b.setEnabled(False)
        #self.layout.addWidget(boton_b)
        
        # Boton c:
        boton_c = QPushButton("Activar cheats", self)
        boton_c.setFixedWidth(250)
        boton_c.setEnabled(False)
        #self.layout.addWidget(boton_c)
        
        self.layout_para_centrar_botones.addWidget(boton_a, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_para_centrar_botones.addSpacing(2)
        self.layout_para_centrar_botones.addWidget(boton_b, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_para_centrar_botones.addSpacing(2)
        self.layout_para_centrar_botones.addWidget(boton_c, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addLayout(self.layout_para_centrar_botones)
        
        self.layout.addSpacing(10)
        
        # Otra línea:
        linea1 = QFrame(self)
        linea1.setFrameShape(QFrame.Shape.HLine)
        linea1.setFrameShadow(QFrame.Shadow.Sunken)
        self.layout.addWidget(linea1)
        
        self.layout.addSpacing(10)
        
        # Boton Créditos:
        boton_creditos = QPushButton("Créditos", self)
        boton_creditos.clicked.connect(self.mostrar_creditos)
        self.layout.addWidget(boton_creditos)
        
        self.layout.addSpacing(10)
        
        # Otra línea:
        linea1 = QFrame(self)
        linea1.setFrameShape(QFrame.Shape.HLine)
        linea1.setFrameShadow(QFrame.Shadow.Sunken)
        self.layout.addWidget(linea1)
        
        self.layout.addSpacing(10)
        
        # Volver:
        self.boton_volver = QPushButton("Volver al Menú Principal", self)
        self.boton_volver.clicked.connect(self.volver)
        self.layout.addWidget(self.boton_volver)
        
        self.setLayout(self.layout)
        
    def mostrar_creditos(self):
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Créditos")
        mensaje.setText("Nosotros desarrollamos este juego:")
        mensaje.setInformativeText(
            "\n\nBonifacio, Lucas\n"
            "Cárdenas, Franco\n"
            "Lopes, Carlos\n"
            "Gonzales, Nadin\n"
            "Cabana, Ricardo (Abandonó)\n"
            "Williams, Dahiana\n"
            "Vidal, Maida Diego\n"
            "Ampuero, Alejandro\n"
            "Contreras, Joel\n")
        mensaje.setIcon(QMessageBox.Icon.Information)
        mensaje.setStandardButtons(QMessageBox.StandardButton.Ignore)
        mensaje.exec()

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