from PyQt6.QtWidgets import QMainWindow, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QGridLayout,QWidget, QRadioButton, QMessageBox
from PyQt6.QtGui import QPixmap, QIntValidator 
from PyQt6.QtCore import Qt
from tablero_pantalla import Tablero

class CrearPartida(QDialog):
    def __init__(self, main_menu, parent=None):
        super().__init__(parent)
        self.main_menu = main_menu  # Referencia MainMenu
        self.setWindowTitle("Crear Partida")
        self.setGeometry(300, 200, 600, 400)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.adjustSize()
        self.setMinimumSize(600, 300)

        
        # Cantidad Jugadores
        self.jugadores_label = QLabel("¿Cuantos Jugaran? (Debe ser entre 2 y 5)", self)
        self.jugadores_iniciales_input = QLineEdit(self)
        self.jugadores_iniciales_input.setText("2")  # Valor inicial
        self.jugadores_iniciales_input.setValidator(QIntValidator(2, 5))  # Validación 
        self.jugadores_iniciales_input.textChanged.connect(self.validar_jugadores)
        self.main_layout.addWidget(self.jugadores_label)
        self.main_layout.addWidget(self.jugadores_iniciales_input)
        
        self.jugadores = []
        
        # Dinero Inicial
        self.dinero_label = QLabel("¿Con cuánto dinero comienzan los jugadores?", self)
        self.dinero_inicial_input = QLineEdit(self)
        self.dinero_inicial_input.setText("1000")  # Valor inicial
        self.dinero_inicial_input.setValidator(QIntValidator(1, 10000))  # Validación 
        self.dinero_inicial_input.textChanged.connect(self.validar_dinero)
        self.main_layout.addWidget(self.dinero_label)
        self.main_layout.addWidget(self.dinero_inicial_input)

        # Botones
        self.jugadores_layout = QGridLayout()
        self.main_layout.addLayout(self.jugadores_layout)

        self.add_jugador_button = QPushButton("Agregar Jugador", self)
        self.add_jugador_button.clicked.connect(self.agregar_jugador)
        self.main_layout.addWidget(self.add_jugador_button)

        self.crear_partida_button = QPushButton("Crear Partida", self)
        self.crear_partida_button.setEnabled(False) 
        self.crear_partida_button.clicked.connect(self.crear_partida)
        self.main_layout.addWidget(self.crear_partida_button)
        
        self.btn_volver = QPushButton("Volver al Menú Principal", self)
        self.btn_volver.clicked.connect(self.volver)
        self.main_layout.addWidget(self.btn_volver)

    def validar_jugadores(self):
        try:
            num_jugadores = int(self.jugadores_iniciales_input.text())
            if 2 <= num_jugadores <= 5:
                self.crear_partida_button.setEnabled(True)
            else:
                self.crear_partida_button.setEnabled(False)
                QMessageBox.warning(self, "Número inválido", "El número de jugadores debe ser entre 2 y 5.")
                self.jugadores_iniciales_input.clear()
        except ValueError:
            self.crear_partida_button.setEnabled(False)
            
    def validar_dinero(self):
        try:
            num_dinero = int(self.dinero_inicial_input.text())
            if num_dinero > 0:
                self.crear_partida_button.setEnabled(True)
            else:
                self.crear_partida_button.setEnabled(False)
                QMessageBox.warning(self, "Número inválido", "Debe ser mayor a 0")
                self.dinero_inicial_input.clear()
        except ValueError:
            self.crear_partida_button.setEnabled(False)

    def volver(self):
        self.hide()
        self.main_menu.show()

    def agregar_jugador(self):
        if len(self.jugadores) < int(self.jugadores_iniciales_input.text()):
            jugador_row = len(self.jugadores)

            # Nombre jugador
            nombre_label = QLabel(f"Jugador {jugador_row + 1}", self)
            nombre_input = QLineEdit(self)
            nombre_input.setPlaceholderText("Ingrese su nombre")
            self.jugadores_layout.addWidget(nombre_label, jugador_row, 0)
            self.jugadores_layout.addWidget(nombre_input, jugador_row, 1)

            # Seleccion Avatar
            avatar_label = QLabel("Elija su avatar:", self)
            self.jugadores_layout.addWidget(avatar_label, jugador_row, 2)

            avatar_combo = QComboBox(self)
            avatar_combo.addItem("Avatar 1", "imagenes/ui/perfilRecortado1.png")
            avatar_combo.addItem("Avatar 2", "imagenes/ui/perfilRecortado2.png")
            avatar_combo.addItem("Avatar 3", "imagenes/ui/perfilRecortado3.png")
            avatar_combo.addItem("Avatar 4", "imagenes/ui/perfilRecortado4.png")
            avatar_combo.addItem("Avatar 5", "imagenes/ui/perfilRecortado5.png")
            avatar_combo.addItem("Avatar 6", "imagenes/ui/perfilRecortado6.png")
            avatar_combo.addItem("Avatar 7", "imagenes/ui/perfilRecortado7.png")
            avatar_combo.addItem("Avatar 8", "imagenes/ui/perfilRecortado8.png")
            self.jugadores_layout.addWidget(avatar_combo, jugador_row, 3)

            # Guardar jugador
            self.jugadores.append({
                'nombre': nombre_input,
                'avatar': avatar_combo,
                'dinero': int(self.dinero_inicial_input.text()) ,
                'propiedades': [],
                'banco': [],
                'acciones': [],
            })
            
            if len(self.jugadores) == int(self.jugadores_iniciales_input.text()):
                self.crear_partida_button.setEnabled(True) 
        else:
            self.add_jugador_button.setDisabled(True) #Si se llega a la cantidad de jugadores, se desahibilita

    def crear_partida(self):
        dinero_inicial = int(self.dinero_inicial_input.text())
        jugadores = []

        # Datos Jugadores
        for jugador in self.jugadores:
            nombre = jugador['nombre'].text()
            avatar = jugador['avatar'].currentData()
            dinero = jugador['dinero']
            propiedades = jugador['propiedades']
            banco = jugador['banco']
            acciones = jugador['acciones']
            jugadores.append({'nombre': nombre, 'avatar': avatar, 'dinero': dinero, 'propiedades': propiedades, 'banco': banco, 'acciones': acciones})

        self.close()
        self.start_game(dinero_inicial, jugadores)

    def start_game(self, dinero_inicial, jugadores):
        self.t = Tablero(self.main_menu, dinero_inicial, jugadores)
        self.t.show()
