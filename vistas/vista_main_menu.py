from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy, QHBoxLayout
from PyQt6.QtGui import QIcon, QPixmap, QGuiApplication, QShortcut, QKeySequence
from PyQt6.QtCore import Qt


class MainMenu(QMainWindow):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador
        self.setWindowTitle("Monopoly Deal")
        self.setGeometry(480, 200, 600, 450)
        self.setWindowIcon(QIcon("multimedia/ui/icono.png"))
        self.centrar_ventana()
        
        # Widget principal y layout:
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)
        
        # Shortcuts:
        shortcut1 = QShortcut(QKeySequence("1"), self)
        shortcut1.activated.connect(self.__controlador.mostrar_crear_partida)
        
        shortcut2 = QShortcut(QKeySequence("2"), self)
        shortcut2.activated.connect(self.__controlador.mostrar_opciones)
        
        shortcut3 = QShortcut(QKeySequence("3"), self)
        shortcut3.activated.connect(self.__controlador.mostrar_como_juego)
        
        shortcut4 = QShortcut(QKeySequence("4"), self)
        shortcut4.activated.connect(self.__controlador.mostrar_estadisticas_inicio_sesion)

        # (1):
        # Espaciador superior:
        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # (2):
        # Imagen encabezado:
        self.imagen_label = QLabel(self)
        pixmap = QPixmap("multimedia/ui/headerLogo.png").scaled(
            500, 130, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
        )
        self.imagen_label.setPixmap(pixmap)
        self.imagen_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.imagen_label)

        # (3):
        # Espaciador inferior:
        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # (4):
        # Botones:
        botones_layout = QVBoxLayout()
        botones_layout.setContentsMargins(30, 0, 30, 20) # <-- Márgenes!!!

        # (4.1):
        # Botón "Crear una Partida":
        self.boton_crear_partida = self.crear_boton("Crear una Partida", "multimedia/ui/menu_boton_1.png")
        self.boton_crear_partida.clicked.connect(self.__controlador.mostrar_crear_partida)
        botones_layout.addWidget(self.boton_crear_partida)

        botones_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # (4.2):
        # Botón "Opciones":
        self.boton_opciones = self.crear_boton("Opciones", "multimedia/ui/menu_boton_2.png")
        self.boton_opciones.clicked.connect(self.__controlador.mostrar_opciones)
        botones_layout.addWidget(self.boton_opciones)

        botones_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # (4.3):
        # Botón "Mostrar Como Juego":
        self.boton_mostrar_como_juego = self.crear_boton("¿Cómo Juego?", "multimedia/ui/emoji.png")
        self.boton_mostrar_como_juego.clicked.connect(self.__controlador.mostrar_como_juego)
        botones_layout.addWidget(self.boton_mostrar_como_juego)

        # Agregar los 3 botones al layout principal:
        self.layout.addLayout(botones_layout)
        
        # ---
        
        layout_footer = QHBoxLayout()
        
        # Botón estadísticas en el footer:
        self.estadisticas_boton = self.crear_boton_estadisticas("Ver mis Estadísticas", "multimedia/ui/grafico.png")
        self.estadisticas_boton.clicked.connect(self.__controlador.mostrar_estadisticas_inicio_sesion)
        tooltip_estadisticas = ("Iniciá sesión para ver tus Estadísticas.")
        self.estadisticas_boton.setToolTip(tooltip_estadisticas)
        layout_footer.addWidget(self.estadisticas_boton)
        
        # Versión en el footer:
        self.version_label = QLabel("v1.0 ", self)
        self.version_label.setStyleSheet("""
            color: #888;
            font-size: 16px;
        """)
        self.version_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        layout_footer.addWidget(self.version_label)
        
        # Agrego el footer al layout principal:
        self.layout.addLayout(layout_footer)

    def crear_boton(self, texto, icono_ruta):
        """Crea un botón que tiene un ícono (a la izquierda) y texto."""
        boton = QPushButton(self) # <-- Este es el contenedor principal.
        boton.setStyleSheet("""
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
        boton.setMinimumWidth(400)
        boton.setFixedHeight(60)

        # Layout del ícono y el texto:
        layout = QHBoxLayout(boton)

        # Ícono
        icono_label = QLabel(self)
        pixmap = QPixmap(icono_ruta).scaled(30, 30) # <-- Tamaño de la imagen.
        icono_label.setPixmap(pixmap)
        icono_label.setFixedSize(100, 40)           # <-- Tamaño fijo del contenedor del ícono.
        layout.addWidget(icono_label)

        # Texto
        texto_label = QLabel(texto, self)
        texto_label.setStyleSheet("""
            font-size: 20px;        /* <-- Hace una re diferencia */
        """)
        layout.addWidget(texto_label)

        return boton
    
    def crear_boton_estadisticas(self, texto, icono_ruta):
        """Crea un botón que tiene un ícono (a la izquierda) y texto."""
        boton = QPushButton(self) # <-- Este es el contenedor principal.
        boton.setStyleSheet("""
            QPushButton {
                border: 2px solid #444;
                border-radius: 3px;
                background-color: #222; /* <-- Es perfecto no cambiar */
                font-size: 10px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #333; /* <-- Tampoco */
            }
        """)
        boton.setFixedHeight(30)
        boton.setFixedWidth(175)

        # Layout del ícono y el texto:
        layout = QHBoxLayout(boton)

        # Ícono:
        icono_label = QLabel(self)
        pixmap = QPixmap(icono_ruta).scaled(15, 15) # <-- Tamaño de la imagen.
        icono_label.setPixmap(pixmap)
        icono_label.setFixedSize(15, 15)           # <-- Tamaño fijo del contenedor del ícono.
        layout.addWidget(icono_label)

        # Texto:
        texto_label = QLabel(texto, self)
        texto_label.setStyleSheet("""
            padding-left: 5px;
            font-size: 14px;
        """)
        layout.addWidget(texto_label)

        return boton

    def centrar_ventana(self):
        """Método para centrar la ventana en el centro de la pantalla."""
        forma_pantalla = QGuiApplication.primaryScreen().availableGeometry()
        forma_ventana = self.frameGeometry()
        centro_pantalla = forma_pantalla.center()
        forma_ventana.moveCenter(centro_pantalla)
        self.move(forma_ventana.topLeft())