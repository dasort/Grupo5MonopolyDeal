from PyQt6.QtWidgets import QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QGridLayout, QMessageBox, QSizePolicy, QSpacerItem
from PyQt6.QtGui import QIcon, QPixmap, QIntValidator 
from PyQt6.QtCore import Qt
from controlador_crear_partida import ControladorCrearPartida 

class CrearPartida(QDialog):
    def __init__(self, main_menu, parent=None):
        super().__init__(parent)
        
        self.main_menu = main_menu
        
        self.minimo_jugadores = 2
        self.maximo_jugadores = 5
        self.jugadores = []
        
        #Ventana inicio
        self.setWindowTitle("Crear Partida")
        self.setGeometry(370, 185, 875, 517)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))
        self.adjustSize()
        self.setMinimumSize(875, 500)
        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)
        
        self.controlador = ControladorCrearPartida(self)  #Llamo a todos los metodos desde el controlador 

        self.layout_derecha = QVBoxLayout()
        self.layout_derecha.setContentsMargins(0, 0, 0, 0)
        self.layout_derecha.setSpacing(0)

        self.widget_izquierda = QWidget()
        self.widget_derecha_arriba = QWidget()
        self.widget_derecha_abajo = QWidget()

        self.widget_izquierda.setStyleSheet("""
            background-color: rgba(89, 45, 22, 1);
            border-right: 4px solid rgba(72, 26, 11, 1);
        """)
        self.widget_derecha_arriba.setStyleSheet("""
            background-color: rgba(196, 114, 48, 1);
            border-bottom: 4px solid rgba(72, 26, 11, 1);
        """)
        self.widget_derecha_abajo.setStyleSheet("""
            background-color: rgba(209, 154, 101, 1);
            border-top: 0;
        """)
        
        self.widget_derecha_arriba.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.widget_derecha_abajo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        self.layout_izquierda = QVBoxLayout(self.widget_izquierda)
        self.layout_izquierda.setContentsMargins(8, 8, 12, 8)
        self.layout_izquierda.setSpacing(8)

        self.layout_derecha_arriba = QHBoxLayout(self.widget_derecha_arriba)
        self.layout_derecha_arriba.setContentsMargins(20, 10, 20, 12)
        self.layout_derecha_arriba.setSpacing(12)

        self.layout_derecha_abajo = QVBoxLayout(self.widget_derecha_abajo)
        self.layout_derecha_abajo.setContentsMargins(5, 5, 5, 5)
        self.layout_derecha_abajo.setSpacing(10)
        
        self.controlador.cargar_iconos()
        
        self.jugadores_layout = QVBoxLayout()
        self.jugadores_layout.setSpacing(5)
        self.layout_derecha_abajo.addLayout(self.jugadores_layout)
        
        self.layout_derecha_abajo.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        #Boton agregar Jugador
        self.agregar_jugador_boton = QPushButton("Agregar Jugador", self)
        self.agregar_jugador_boton.setStyleSheet("""
            QPushButton {
                background-color: #25B31D;
                color: white;
                padding: 6px;
                font-size: 20px;
                outline: none;
                border: 3px solid #9AF593;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #4FD947;
                outline: none;
            }
            QPushButton:disabled {
                background-color: #208521;
                color: #B5B5B5;
                border: 3px solid #59B358;
            }
        """)
        self.agregar_jugador_boton.setFixedSize(230, 60)
        self.agregar_jugador_boton.clicked.connect(self.controlador.agregar_jugador)
        self.layout_izquierda.addWidget(self.agregar_jugador_boton)

        #Boton quitar jugador
        self.quitar_jugador_boton = QPushButton("Quitar Jugador", self)
        self.quitar_jugador_boton.setStyleSheet("""
            QPushButton {
                background-color: #E64444;
                color: white;
                padding: 6px;
                font-size: 20px;
                outline: none;
                border: 3px solid #F79090;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #F06262;
            }
            QPushButton:disabled {
                background-color: #B53636;
                color: #949494;
                border: 3px solid #BF6666;
            }
        """)
        self.quitar_jugador_boton.setFixedSize(230, 60)
        self.quitar_jugador_boton.setEnabled(False)
        self.quitar_jugador_boton.clicked.connect(self.controlador.quitar_jugador)
        self.layout_izquierda.addWidget(self.quitar_jugador_boton)

        texto_en_qss = (
            "(Opcional): Inicia sesión para<br>"
            "guardar tus estadísticas."
        )
        self.aclaracion_label = QLabel(texto_en_qss)
        self.aclaracion_label.setStyleSheet("""
            color: #FFC592;
            border-right: 0;
            font-size: 18px;
        """)
        self.layout_izquierda.addWidget(self.aclaracion_label)
        
        self.layout_izquierda.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        
        self.aviso_qcc = (
            "(Agrega 2 o más jugadores<br>"
            "para crear una partida)."
        )
        self.aviso_label = QLabel(self.aviso_qcc)
        self.aviso_label.setStyleSheet("""
            color: #D47034;
            border-right: 0;
            font-size: 18px;
            padding-top: 4px;
            padding-bottom: 4px;
            background-color: #78391D;
            outline: none;
            border: 2px solid #914A27;
            border-radius: 5px;
        """)
        self.layout_izquierda.addWidget(self.aviso_label)

        #Boton crear partida
        self.crear_partida_boton = QPushButton("Crear Partida", self)
        self.crear_partida_boton.setStyleSheet("""
            QPushButton {
                background-color: #80452B;
                padding: 6px;
                font-size: 25px;
                outline: none;
                border: 3px solid #C77750;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #A16043;
            }
            QPushButton:disabled {
                background-color: #693A24;
                color: #949494;
                border: 3px solid #8A5135;
            }
        """)
        self.crear_partida_boton.setFixedSize(230, 60)
        self.crear_partida_boton.setEnabled(False)
        self.crear_partida_boton.clicked.connect(self.controlador.crear_partida)
        self.layout_izquierda.addWidget(self.crear_partida_boton)

        #Boton Volver 
        self.boton_volver = QPushButton("Volver al Menú Principal", self)
        self.boton_volver.setStyleSheet("""
            QPushButton {
                background-color: #80452B;
                padding: 6px;
                font-size: 20px;
                outline: none;
                border: 3px solid #C77750;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #A16043;
            }
        """)
        
        self.boton_volver.setFixedSize(230, 60)
        self.boton_volver.clicked.connect(self.controlador.volver)
        self.layout_izquierda.addWidget(self.boton_volver)

        #Layout
        self.main_layout.addWidget(self.widget_izquierda)
        self.layout_derecha.addWidget(self.widget_derecha_arriba)
        self.layout_derecha.addWidget(self.widget_derecha_abajo)
        self.main_layout.addLayout(self.layout_derecha)
