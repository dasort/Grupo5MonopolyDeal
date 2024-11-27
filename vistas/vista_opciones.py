from PyQt6.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QSpacerItem, QSizePolicy, QFrame, QMessageBox, QSlider
from PyQt6.QtGui import QGuiApplication, QPixmap
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class Opciones(QDialog):
    def __init__(self, controlador, parent=None):
        super().__init__(parent)

        self.__controlador = controlador
        
        self.setWindowTitle("Opciones")
        self.setGeometry(570, 240, 400, 428)
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
        
        # ---
        
        # Layout para el volumen:
        self.volumen_widget = QWidget()
        self.volumen_widget.setFixedWidth(320)
        self.layout_volumen = QHBoxLayout(self.volumen_widget)
        self.layout_volumen.setSpacing(10)
        
        # Icono para el volumen:
        self.boton = QPushButton(self) # <-- Este es el contenedor principal.
        self.boton.setStyleSheet("""
            QPushButton {
                border: 2px solid #444;
                border-radius: 10px;
                background-color: #222; /* <-- Es perfecto no cambiar */
                font-size: 20px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #333; /* <-- Tampoco */
            }
        """)
        self.boton.setMinimumWidth(40)
        self.boton.setFixedHeight(40)
        self.boton.clicked.connect(self.__controlador.alternar_volumen)

        self.layout_boton = QHBoxLayout(self.boton)

        self.icono_label = QLabel(self)
        pixmap = self.obtener_pixmap_inicial_volumen()
        self.icono_label.setPixmap(pixmap)
        self.icono_label.setFixedSize(30, 30)
        self.layout_boton.addWidget(self.icono_label)
        
        self.layout_volumen.addWidget(self.boton)
        
        # Label para el volumen:
        self.volumen_label = QLabel("Volumen:", self)
        self.volumen_label.setStyleSheet("""
            font-size: 18px;
            text-align: left;
        """)
        self.layout_volumen.addWidget(self.volumen_label)
        
        # Slider para el volumen:
        self.slider_volumen = QSlider(Qt.Orientation.Horizontal, self)
        self.slider_volumen.setMinimum(0)
        self.slider_volumen.setMaximum(100)
        self.slider_volumen.setValue(self.__controlador.obtener_volumen())
        self.slider_volumen.valueChanged.connect(self.__controlador.cambiar_volumen)
        self.slider_volumen.setFixedWidth(165)
        self.layout_volumen.addWidget(self.slider_volumen)
        
        self.main_layout.addWidget(self.volumen_widget)

        # ---
        
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
    
    def cambiar_pixmap_volumen(self):
        volumen = self.__controlador.obtener_volumen()
        if volumen >= 50:
            pixmap = QPixmap("imagenes/ui/volumen_alto.png").scaled(25, 25)
        elif volumen > 1:
            pixmap = QPixmap("imagenes/ui/volumen_bajo.png").scaled(25, 25)
        else:
            pixmap = QPixmap("imagenes/ui/volumen_apagado.png").scaled(25, 25)
        self.icono_label.setPixmap(pixmap)
    
    def obtener_pixmap_inicial_volumen(self):
        volumen = self.__controlador.obtener_volumen()
        if volumen >= 50:
            pixmap = QPixmap("imagenes/ui/volumen_alto.png").scaled(25, 25)
        elif volumen > 1:
            pixmap = QPixmap("imagenes/ui/volumen_bajo.png").scaled(25, 25)
        else:
            pixmap = QPixmap("imagenes/ui/volumen_apagado.png").scaled(25, 25)
        return pixmap
    
    def alternar_icono(self, estado):
        if estado == "apagado":
            pixmap = QPixmap("imagenes/ui/volumen_apagado.png").scaled(25, 25)
            self.slider_volumen.setValue(0)
        else:
            pixmap = QPixmap("imagenes/ui/volumen_alto.png").scaled(25, 25)
            self.slider_volumen.setValue(100)
        self.icono_label.setPixmap(pixmap)
    
    def mostrar_creditos(self):
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Créditos")
        mensaje.setText("Nosotros desarrollamos este juego:  ")
        mensaje.setInformativeText(
            "\n\nBonifacio, Lucas\n"
            "Cárdenas, Franco\n"
            "Lopes, Carlos\n"
            "Gonzales, Nadin\n"
            "Williams, Dahiana\n"
            "Vidal, Maida Diego\n"
            "Ampuero, Alejandro\n\n"
            "Contreras, Joel (No participó)\n"
            "Cabana, Ricardo (Abandonó)\n")
            
        mensaje.setIcon(QMessageBox.Icon.Information)
        mensaje.setStandardButtons(QMessageBox.StandardButton.Ignore)
        mensaje.exec()

    def centrar_ventana(self):
        forma_pantalla = QGuiApplication.primaryScreen().availableGeometry()
        forma_ventana = self.frameGeometry()
        centro_pantalla = forma_pantalla.center()
        forma_ventana.moveCenter(centro_pantalla)
        self.move(forma_ventana.topLeft())