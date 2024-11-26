from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QGridLayout, QMessageBox, QSizePolicy, QSpacerItem
from PyQt6.QtGui import QIcon, QPixmap, QShortcut, QKeySequence
from PyQt6.QtCore import Qt


class CrearPartida(QMainWindow):
    def __init__(self, controlador, parent=None):
        super().__init__(parent)
        
        self.__controlador = controlador  # Llamo a todos los metodos desde el controlador 
        
        self.minimo_jugadores = 2
        self.maximo_jugadores = 5
        self.jugadores = []
        
        # Ventana inicio:
        self.setWindowTitle("Crear Partida")
        self.setGeometry(370, 185, 875, 517)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))
        self.adjustSize()
        self.setMinimumSize(875, 500)
        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

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
        
        self.cargar_iconos()
        
        self.jugadores_layout = QVBoxLayout()
        self.jugadores_layout.setSpacing(5)
        self.layout_derecha_abajo.addLayout(self.jugadores_layout)
        
        self.layout_derecha_abajo.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Botón agregar jugador:
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
        self.agregar_jugador_boton.clicked.connect(self.agregar_jugador)
        self.layout_izquierda.addWidget(self.agregar_jugador_boton)

        self.shortcut1 = QShortcut(QKeySequence("+"), self)
        self.shortcut1.activated.connect(self.agregar_jugador)

        # Botón quitar jugador:
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
        self.quitar_jugador_boton.clicked.connect(self.__controlador.quitar_jugador)
        self.layout_izquierda.addWidget(self.quitar_jugador_boton)
        
        self.shortcut2 = QShortcut(QKeySequence("-"), self)
        self.shortcut2.activated.connect(self.__controlador.quitar_jugador)

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

        # Botón crear partida:
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
        self.crear_partida_boton.clicked.connect(self.__controlador.crear_partida)
        self.layout_izquierda.addWidget(self.crear_partida_boton)

        # Botón volver:
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
        self.boton_volver.clicked.connect(self.__controlador.volver)
        self.layout_izquierda.addWidget(self.boton_volver)

        # Layout:
        self.main_layout.addWidget(self.widget_izquierda)
        self.layout_derecha.addWidget(self.widget_derecha_arriba)
        self.layout_derecha.addWidget(self.widget_derecha_abajo)
        self.main_layout.addLayout(self.layout_derecha)

    def cargar_iconos(self):
        avatar_vacio = "imagenes/ui/perfilRecortadoVacio.png"
        
        while self.layout_derecha_arriba.count():
            widget = self.layout_derecha_arriba.takeAt(0).widget()
            if widget:
                widget.deleteLater()
                
        for i in range(5):
            avatar_label = QLabel(self)
            avatar_label.setStyleSheet("""
                border-bottom: 0;
            """)

            if i < len(self.jugadores):
                avatar = self.jugadores[i]["avatar"].currentData()
            else:
                avatar = avatar_vacio

            pixmap = QPixmap(avatar).scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            avatar_label.setPixmap(pixmap)
            avatar_label.setFixedSize(100, 100)
            self.layout_derecha_arriba.addWidget(avatar_label)
    
    def agregar_jugador(self):
        jugador_row = len(self.jugadores)
        widget_jugador = QWidget()
        widget_jugador.setStyleSheet("""
            color: #FF9A50;
            border-right: 0;
            font-size: 18px;
            padding-top: 4px;
            padding-bottom: 4px;
            background-color: #9C522E;
            outline: none;
            border: 3px solid #9C522E;
            border-radius: 5px;
        """)
        
        layout_jugador = QVBoxLayout(widget_jugador)
        layout_jugador.setContentsMargins(0, 0, 0, 0)
        layout_jugador.setSpacing(0)
        info_jugador_layout = QGridLayout()
        info_jugador_layout.setContentsMargins(0, 0, 5, 0)

        tooltip_text = (
            "1. Puede iniciar sesión y aparecerá con su nombre de cuenta.<br>"
            "2. Si no inicia sesión puede ingresar el nombre que quiera.<br>"
            "3. Si no ingresa nombre aparecerá como anónimo."
        )

        nombre_label = QLabel(f"Jugador {jugador_row + 1}:")
        nombre_label.setToolTip(tooltip_text)
        nombre_label.setStyleSheet("""
            background-color: #78391D;
        """)

        nombre_input = QLineEdit()
        nombre_input.setPlaceholderText("Nombre")
        nombre_input.setToolTip(tooltip_text)
        nombre_input.setStyleSheet("""
            background-color: #78391D;
        """)
        nombre_input.setFixedWidth(200)

        avatar_label = QLabel("Elija su avatar:")
        avatar_combo = QComboBox()
        for i in range(1, 9):
            avatar_combo.addItem(f"Avatar {i}", f"imagenes/ui/perfilRecortado{i}.png")
        avatar_combo.setStyleSheet("""
            background-color: #78391D;
            padding-left: 5px;
        """)

        sesion_label = QLabel("Iniciar sesión:")
        sesion_label.setToolTip(tooltip_text)

        boton_cuenta = QPushButton("Inicie", self)
        boton_cuenta.clicked.connect(self.__controlador.abre_iniciar_sesion)
        boton_cuenta.setToolTip(tooltip_text)
        boton_cuenta.setStyleSheet("""
            QPushButton {
                background-color: #80452B;
                color: #FFC592;
                padding: 4px;
                font-size: 18px;
                border: 2px solid #C77750;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #A16043;
            }
            QPushButton:pressed {
                background-color: #914A27;
            }
        """)

        layout_jugador.addWidget(nombre_label)
        layout_jugador.addLayout(info_jugador_layout)

        info_jugador_layout.addWidget(nombre_input, 0, 0)
        info_jugador_layout.addWidget(avatar_label, 0, 1)
        info_jugador_layout.addWidget(avatar_combo, 0, 2)
        info_jugador_layout.addWidget(sesion_label, 0, 3)
        info_jugador_layout.addWidget(boton_cuenta, 0, 4)

        self.jugadores_layout.addWidget(widget_jugador)

        avatar_combo.currentIndexChanged.connect(self.cargar_iconos)

        self.jugadores.append({
            "widget_jugador": widget_jugador,
            "layout_jugador": layout_jugador,
            "info_jugador_layout": info_jugador_layout,
            "nombre_label": nombre_label,
            "nombre_input": nombre_input,
            "avatar_label": avatar_label,
            "avatar_combo": avatar_combo,
            "sesion_label": sesion_label,
            "boton_cuenta": boton_cuenta,
            
            'nombre': nombre_input,
            'avatar': avatar_combo,
            'dinero': 0,
            'propiedades': [],
            'banco': [],
            'acciones': [],
        })
        
        self.__controlador.cambio_cant_jugadores()
        self.cargar_iconos()