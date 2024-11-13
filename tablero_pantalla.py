from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QScrollArea
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QIcon
from carta_boton import CartaBoton

class Tablero(QMainWindow):
    def __init__(self, dinero_inicial, jugadores, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tablero de Juego")
        self.setGeometry(200, 100, 1000, 700)

        self.dinero_inicial = dinero_inicial
        self.jugadores = jugadores
        self.turno_actual = 0
        self.tiempo_restante = 60

        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget(self)
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        # Cuadro de jugadores
        self.jugadores_layout = QHBoxLayout()
        self.main_layout.addLayout(self.jugadores_layout)
        self.mostrar_jugadores()

        # Zona de turno actual y temporizador
        self.turno_label = QLabel(f"Turno de: {self.jugadores[self.turno_actual]['nombre']}", self)
        self.main_layout.addWidget(self.turno_label)

        self.timer_label = QLabel(f"Tiempo restante: {self.tiempo_restante}s", self)
        self.main_layout.addWidget(self.timer_label)

        # Configuración del temporizador
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_tiempo)
        self.tiempo_restante = 60
        self.timer.start(1000)

        # Mano del jugador actual
        self.mano_layout = QHBoxLayout()
        self.main_layout.addLayout(self.mano_layout)
        self.mostrar_mano_jugador()

        # Cuadro de acción de carta
        self.accion_label = QLabel("Acción de la carta seleccionada:", self)
        self.main_layout.addWidget(self.accion_label)

        # Detalles de la carta seleccionada
        self.detalle_label = QLabel("Detalles de la carta:", self)
        self.main_layout.addWidget(self.detalle_label)

        # Botón para finalizar turno
        self.btn_finalizar_turno = QPushButton("Finalizar Turno", self)
        self.btn_finalizar_turno.clicked.connect(self.finalizar_turno)
        self.main_layout.addWidget(self.btn_finalizar_turno)

    def mostrar_jugadores(self):
        """Muestra los jugadores en la parte superior de la pantalla."""
        for i in reversed(range(self.jugadores_layout.count())): 
            widget = self.jugadores_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        for jugador in self.jugadores:
            avatar = QPixmap(jugador["avatar"]).scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio)
            avatar_label = QLabel(self)
            avatar_label.setPixmap(avatar)
            nombre_label = QLabel(f"{jugador['nombre']} - Dinero: ${jugador['dinero']}", self)

            jugador_layout = QVBoxLayout()
            jugador_layout.addWidget(avatar_label)
            jugador_layout.addWidget(nombre_label)

            self.jugadores_layout.addLayout(jugador_layout)

    def mostrar_mano_jugador(self):
        """Muestra las cartas del jugador actual."""
        for i in reversed(range(self.mano_layout.count())):
            widget = self.mano_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        jugador = self.jugadores[self.turno_actual]
        for carta in jugador["mano"]:
            carta_boton = CartaBoton(carta, f"Efecto de {carta}", self)
            self.mano_layout.addWidget(carta_boton)

    def mostrar_detalles_carta(self, nombre, efecto):
        """Muestra los detalles de la carta seleccionada."""
        self.detalle_label.setText(f"Nombre: {nombre}\nEfecto: {efecto}")

    def actualizar_tiempo(self):
        """Actualiza el temporizador."""
        if self.tiempo_restante > 0:
            self.tiempo_restante -= 1
            self.timer_label.setText(f"Tiempo restante: {self.tiempo_restante}s")
        else:
            self.finalizar_turno()

    def finalizar_turno(self):
        """Finaliza el turno y pasa al siguiente jugador."""
        self.timer.stop()
        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)
        self.turno_label.setText(f"Turno de: {self.jugadores[self.turno_actual]['nombre']}")
        self.tiempo_restante = 60
        self.timer.start(1000)

        self.mostrar_mano_jugador()
