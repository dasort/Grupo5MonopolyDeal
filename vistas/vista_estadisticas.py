from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtGui import QIcon, QPixmap, QGuiApplication
from PyQt6.QtCore import Qt

class Estadisticas(QDialog):
    def __init__(self, controlador, parent=None):
        super().__init__(parent)

        self.__controlador = controlador

        self.setWindowTitle("Estadísticas")
        self.setGeometry(570, 240, 400, 300)
        self.setWindowIcon(QIcon("multimedia/ui/icono.png"))
        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)

        # Título aclarativo:
        self.titulo_label = QLabel(self)
        self.titulo_label.setText("Estas son tus Estadísticas")
        self.titulo_label.setFixedHeight(33)
        self.titulo_label.setStyleSheet("""
            font-size: 20px;
        """)
        self.titulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Línea:
        self.linea = QFrame(self)
        self.linea.setFrameShape(QFrame.Shape.HLine)
        self.linea.setFrameShadow(QFrame.Shadow.Sunken)


        # Layout horizontal del Nombre de Pila:
        self.layout_nombre = QHBoxLayout()

        # (1/2) Ícono del Nombre de Pila:
        self.nombre_icono_label = QLabel(self)
        pixmap = QPixmap("multimedia/ui/silueta.png").scaled(25, 25)
        self.nombre_icono_label.setPixmap(pixmap)
        self.nombre_icono_label.setFixedSize(25, 25)

        self.layout_nombre.addWidget(self.nombre_icono_label) # <-- Agrego 1/2 (El Ícono).

        # (2/2) Label del Nombre de Pila:
        self.nombre_label = QLabel(self)
        self.nombre_label.setText("Nombre de Pila: ")
        self.nombre_label.setFixedHeight(33)
        self.nombre_label.setStyleSheet("""
            font-size: 20px;
        """)
        self.layout_nombre.addWidget(self.nombre_label) # <-- Agrego 2/2 (El Label).

        # Layout horizontal del Apellido:
        self.layout_apellido = QHBoxLayout()

        # (1/2) Ícono del Apellido:
        self.apellido_icono_label = QLabel(self)
        pixmap = QPixmap("multimedia/ui/silueta.png").scaled(25, 25)
        self.apellido_icono_label.setPixmap(pixmap)
        self.apellido_icono_label.setFixedSize(25, 25)

        self.layout_apellido.addWidget(self.apellido_icono_label) # <-- Agrego 1/2 (El Ícono).

        # (2/2) Label del Apellido:
        self.apellido_label = QLabel(self)
        self.apellido_label.setText("Apellido: ")
        self.apellido_label.setFixedHeight(33)
        self.apellido_label.setStyleSheet("""
            font-size: 20px;
        """)
        self.layout_apellido.addWidget(self.apellido_label) # <-- Agrego 2/2 (El Label).

        # Layout horizontal del Nickname:
        self.layout_nickname = QHBoxLayout()

        # (1/2) Ícono del Nickname:
        self.nickname_icono_label = QLabel(self)
        pixmap = QPixmap("multimedia/ui/silueta_pregunta.png").scaled(25, 25)
        self.nickname_icono_label.setPixmap(pixmap)
        self.nickname_icono_label.setFixedSize(25, 25)

        self.layout_nickname.addWidget(self.nickname_icono_label) # <-- Agrego 1/2 (El Ícono).

        # (2/2) Label del Nickname:
        self.nickname_label = QLabel(self)
        self.nickname_label.setText("Nickname: ")
        self.nickname_label.setFixedHeight(33)
        self.nickname_label.setStyleSheet("""
            font-size: 20px;
        """)
        self.layout_nickname.addWidget(self.nickname_label) # <-- Agrego 2/2 (El Label).

        # Tooltip del Nickname:
        tooltip_nickname = (
            "Este es su nickname, el nombre que aparecerá<br>"
            "para los demás, debe ser único."
        )
        self.nickname_icono_label.setToolTip(tooltip_nickname)
        self.nickname_label.setToolTip(tooltip_nickname)

        # Layout horizontal de Partidas Jugadas:
        self.layout_partidas_jugadas = QHBoxLayout()

        # (1/2) Ícono de Partidas Jugadas:
        self.partidas_jugadas_icono_label = QLabel(self)
        pixmap = QPixmap("multimedia/ui/pelota.png").scaled(25, 25)
        self.partidas_jugadas_icono_label.setPixmap(pixmap)
        self.partidas_jugadas_icono_label.setFixedSize(25, 25)

        self.layout_partidas_jugadas.addWidget(self.partidas_jugadas_icono_label) # <-- Agrego 1/2 (El Ícono).

        # (2/2) Label de Partidas Jugadas:
        self.partidas_jugadas_label = QLabel(self)
        self.partidas_jugadas_label.setText("Partidas Jugadas: ")
        self.partidas_jugadas_label.setFixedHeight(33)
        self.partidas_jugadas_label.setStyleSheet("""
            font-size: 20px;
        """)
        self.layout_partidas_jugadas.addWidget(self.partidas_jugadas_label) # <-- Agrego 2/2 (El Label).

        # ---

        # Layout horizontal de Partidas Ganadas:
        self.layout_partidas_ganadas = QHBoxLayout()

        # (1/2) Ícono de Partidas Ganadas:
        self.partidas_ganadas_icono_label = QLabel(self)
        pixmap = QPixmap("multimedia/ui/trofeo.png").scaled(25, 25)
        self.partidas_ganadas_icono_label.setPixmap(pixmap)
        self.partidas_ganadas_icono_label.setFixedSize(25, 25)

        self.layout_partidas_ganadas.addWidget(self.partidas_ganadas_icono_label) # <-- Agrego 1/2 (El Ícono).

        # (2/2) Label de Partidas Ganadas:
        self.partidas_ganadas_label = QLabel(self)
        self.partidas_ganadas_label.setText("Partidas Ganadas: ")
        self.partidas_ganadas_label.setFixedHeight(33)
        self.partidas_ganadas_label.setStyleSheet("""
            font-size: 20px;
        """)
        self.layout_partidas_ganadas.addWidget(self.partidas_ganadas_label) # <-- Agrego 2/2 (El Label).

        # ---

        # Botón Volver:
        self.boton_volver = QPushButton("Volver al Menú Principal", self)
        self.boton_volver.setStyleSheet("""
            QPushButton {
                padding: 6px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #4D4D4D;
            }
        """)
        self.boton_volver.clicked.connect(self.__controlador.volver)

        # Agregar widgets al layout principal
        self.main_layout.addWidget(self.titulo_label)
        self.main_layout.addWidget(self.linea)
        self.main_layout.addLayout(self.layout_nombre)
        self.main_layout.addLayout(self.layout_apellido)
        self.main_layout.addLayout(self.layout_nickname)
        self.main_layout.addLayout(self.layout_partidas_jugadas)
        self.main_layout.addLayout(self.layout_partidas_ganadas)
        self.main_layout.addWidget(self.boton_volver)

        self.__controlador.datos()        
        
        # Actualizar los datos en la vista
        self.nombre_label.setText(self.nombre_label.text() + self.__controlador.get_nombre())
        self.apellido_label.setText(self.apellido_label.text() + self.__controlador.get_apellido())
        self.nickname_label.setText(self.nickname_label.text() + self.__controlador.get_nickname())
        self.partidas_jugadas_label.setText(self.partidas_jugadas_label.text() + self.__controlador.get_partidas_jugadas())
        self.partidas_ganadas_label.setText(self.partidas_ganadas_label.text() + self.__controlador.get_partidas_ganadas())

    def centrar_ventana(self):
        forma_pantalla = QGuiApplication.primaryScreen().availableGeometry()
        forma_ventana = self.frameGeometry()
        centro_pantalla = forma_pantalla.center()
        forma_ventana.moveCenter(centro_pantalla)
        self.move(forma_ventana.topLeft())