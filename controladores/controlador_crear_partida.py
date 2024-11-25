from PyQt6.QtWidgets import QMessageBox, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QGridLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from tablero_pantalla import Tablero

class ControladorCrearPartida:
    def __init__(self, partida):
        self.partida = partida

    def volver(self):
        self.partida.hide()
#        self.partida.main_menu.show()

    def cargar_iconos(self):
        avatar_vacio = "imagenes/ui/perfilRecortadoVacio.png"
        
        while self.partida.layout_derecha_arriba.count():
            widget = self.partida.layout_derecha_arriba.takeAt(0).widget()
            if widget:
                widget.deleteLater()
                
        for i in range(5):
            avatar_label = QLabel(self.partida)
            avatar_label.setStyleSheet("""
                border-bottom: 0;
            """)

            if i < len(self.partida.jugadores):
                avatar = self.partida.jugadores[i]["avatar"].currentData()
            else:
                avatar = avatar_vacio

            pixmap = QPixmap(avatar).scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            avatar_label.setPixmap(pixmap)
            avatar_label.setFixedSize(100, 100)
            self.partida.layout_derecha_arriba.addWidget(avatar_label)

    def cambio_cant_jugadores(self):
        if len(self.partida.jugadores) >= self.partida.minimo_jugadores:
            if len(self.partida.jugadores) == self.partida.maximo_jugadores:
                self.partida.agregar_jugador_boton.setEnabled(False)
            else:
                self.partida.agregar_jugador_boton.setEnabled(True)
                self.partida.crear_partida_boton.setEnabled(True)
                self.partida.aviso_label.hide()
        else:
            if len(self.partida.jugadores) == 1:
                self.partida.quitar_jugador_boton.setEnabled(True)
                self.partida.crear_partida_boton.setEnabled(False)
                self.partida.aviso_label.show()
            else:
                self.partida.quitar_jugador_boton.setEnabled(False)

    def agregar_jugador(self):
        jugador_row = len(self.partida.jugadores)
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

        boton_cuenta = QPushButton("Inicie", self.partida)
        boton_cuenta.clicked.connect(self.volver)
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

        self.partida.jugadores_layout.addWidget(widget_jugador)

        avatar_combo.currentIndexChanged.connect(self.cargar_iconos)

        self.partida.jugadores.append({
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
        
        self.cambio_cant_jugadores()
        self.cargar_iconos()

    def quitar_jugador(self):
        if self.partida.jugadores:
            jugador = self.partida.jugadores.pop()
            jugador["widget_jugador"].deleteLater()
            jugador["layout_jugador"].deleteLater()
            jugador["info_jugador_layout"].deleteLater()
            jugador["nombre_label"].deleteLater()
            jugador["nombre_input"].deleteLater()
            jugador["avatar_label"].deleteLater()
            jugador["avatar_combo"].deleteLater()
            jugador["sesion_label"].deleteLater()
            jugador["boton_cuenta"].deleteLater()

            self.cambio_cant_jugadores()
            self.cargar_iconos()

    def crear_partida(self):
        jugadores = []
        for jugador in self.partida.jugadores:
            nombre = jugador['nombre'].text()
            avatar = jugador['avatar'].currentData()
            dinero = jugador['dinero']
            propiedades = jugador['propiedades']
            banco = jugador['banco']
            acciones = jugador['acciones']
            jugadores.append({'nombre': nombre, 'avatar': avatar, 'dinero': dinero, 'propiedades': propiedades, 'banco': banco, 'acciones': acciones})

        self.partida.close()
        self.start_game(jugadores)

    def start_game(self, jugadores):
        self.partida.t = Tablero(self.partida.main_menu, jugadores)
        self.partida.t.show()
