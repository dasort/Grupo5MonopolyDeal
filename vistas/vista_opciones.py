from PyQt6.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QSpacerItem, QSizePolicy, QFrame, QMessageBox
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class Opciones(QDialog):
    def __init__(self, controlador, parent=None):
        super().__init__(parent)

        self.__controlador = controlador
        
        self.setWindowTitle("Opciones")
        self.setGeometry(570, 240, 400, 345)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))

        # Layouts:
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        self.main_layout.setContentsMargins(0, 20, 0, 0)
        self.main_layout.setSpacing(20)
        self.setLayout(self.main_layout)
        
        self.layout_botones_centrales = QVBoxLayout()
        self.layout_botones_centrales.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        self.layout_botones_centrales.setSpacing(10)

        # Título:
        self.titulo_label = QLabel("Ajustes y configuraciones del juego:", self)
        self.titulo_label.setStyleSheet("""
            font-size: 18px;
            text-align: left;
        """)
        self.main_layout.addWidget(self.titulo_label)

        # Línea 1:
        self.linea1 = QFrame(self)
        self.linea1.setFrameShape(QFrame.Shape.HLine)
        self.linea1.setFrameShadow(QFrame.Shadow.Sunken)
        self.main_layout.addWidget(self.linea1)

        # Botones centrales:
        boton_a = self.crear_boton_central("Version prémium")
        boton_a.setToolTip("Disponible en la v2.0.")
        self.layout_botones_centrales.addWidget(boton_a)

        boton_b = self.crear_boton_central("Recompensa diaria")
        boton_b.setToolTip("Disponible solo en la versión prémium.")
        self.layout_botones_centrales.addWidget(boton_b)

        boton_c = self.crear_boton_central("Activar cheats")
        boton_c.setToolTip("Disponible en una recompensa diaria.")
        self.layout_botones_centrales.addWidget(boton_c)

        self.main_layout.addLayout(self.layout_botones_centrales)
        
        # Línea 2: 
        self.linea2 = QFrame(self)
        self.linea2.setFrameShape(QFrame.Shape.HLine)
        self.linea2.setFrameShadow(QFrame.Shadow.Sunken)
        self.main_layout.addWidget(self.linea2)

        # Botón Créditos:
        self.boton_creditos = self.crear_boton("Créditos")
        self.boton_creditos.clicked.connect(self.mostrar_creditos)
        self.boton_creditos.setToolTip("Visualizá los desarrolladores de este juego.")
        self.main_layout.addWidget(self.boton_creditos)

        # Botón Volver:
        self.boton_volver = self.crear_boton("Volver al Menú Principal")
        self.boton_volver.clicked.connect(self.__controlador.volver)
        self.boton_volver.setToolTip("Volvé al Menú Principal.")
        self.main_layout.addWidget(self.boton_volver)

    def crear_boton(self, texto):
        boton = QPushButton(texto, self)
        boton.setStyleSheet("""
            QPushButton {
                border: 2px solid #444;
                border-radius: 5px;
                background-color: #222; /* <-- Es perfecto no cambiar */
                font-size: 18px;
                text-align: center;
            }
            QPushButton:hover {
                background-color: #333; /* <-- Tampoco */
            }
        """)
        boton.setFixedHeight(30)
        boton.setFixedWidth(320)
    
        return boton
    
    def crear_boton_central(self, texto):
        boton = QPushButton(texto, self)
        boton.clicked.connect(self.mostrar_creditos)
        boton.setEnabled(False)
        boton.setStyleSheet("""
            font-size: 17px;
        """)
        
        boton.setFixedHeight(32)
        boton.setFixedWidth(250)
    
        return boton
    
    def mostrar_creditos(self):
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Créditos")
        mensaje.setText("Nosotros desarrollamos este juego:  ")
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

    def centrar_ventana(self):
        forma_pantalla = QGuiApplication.primaryScreen().availableGeometry()
        forma_ventana = self.frameGeometry()
        centro_pantalla = forma_pantalla.center()
        forma_ventana.moveCenter(centro_pantalla)
        self.move(forma_ventana.topLeft())