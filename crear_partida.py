from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QGridLayout, QMessageBox
from PyQt6.QtGui import QIcon, QPixmap, QIntValidator 
from PyQt6.QtCore import Qt
from tablero_pantalla import Tablero

class CrearPartida(QDialog):
    def __init__(self, main_menu, parent=None):
        super().__init__(parent)
        self.main_menu = main_menu # <-- Una referencia a MainMenu.
        self.setWindowTitle("Crear Partida")
        self.setGeometry(480, 200, 600, 450)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.adjustSize()
        self.setMinimumSize(600, 450)
        
        # Cantidad Jugadores
        self.jugadores_label = QLabel("¿Cuantos Jugaran? (Deben ser entre 2 y 5)", self)
        self.jugadores_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.jugadores_iniciales_input = QLineEdit(self)
        self.jugadores_iniciales_input.setText("2")
        self.jugadores_iniciales_input.setValidator(QIntValidator(2, 5))
        self.jugadores_iniciales_input.setPlaceholderText("Si o si debes mencionar un valor.")
        self.jugadores_iniciales_input.textChanged.connect(self.cambio_cant_jugadores)
        #self.jugadores_iniciales_input.textChanged.connect(self.validar_jugadores)
        
        self.main_layout.addWidget(self.jugadores_label)
        self.main_layout.addWidget(self.jugadores_iniciales_input)
        
        self.jugadores = []
        
        # Dinero Inicial
        self.dinero_label = QLabel("¿Con cuánto dinero comienzan los jugadores?", self)
        self.dinero_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dinero_inicial_input = QLineEdit(self)
        self.dinero_inicial_input.setText("1000")
        self.dinero_inicial_input.setValidator(QIntValidator(1, 10000))
        self.dinero_inicial_input.setPlaceholderText("Si o si debes mencionar un valor.")
        self.dinero_inicial_input.textChanged.connect(self.validar_dinero)
        self.main_layout.addWidget(self.dinero_label)
        self.main_layout.addWidget(self.dinero_inicial_input)

        # Botones
        # 1. add_jugador
        # 2. subtract_jugador
        # 3. crear_partida_button
        # 4. boton_volver

        self.jugadores_layout = QGridLayout()
        self.main_layout.addLayout(self.jugadores_layout)

        self.add_jugador_button = QPushButton("Agregar Jugador", self)
        self.add_jugador_button.setStyleSheet("""
            QPushButton {
                background-color: #479C36;
                color: white;
                padding: 6px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #7FD46E;
            }
        """)
        self.add_jugador_button.clicked.connect(self.agregar_jugador)
        self.main_layout.addWidget(self.add_jugador_button)
        
        self.subtract_jugador_button = QPushButton("Quitar Jugador", self)
        self.subtract_jugador_button.setStyleSheet("""
            QPushButton {
                background-color: #D96372;
                color: white;
                padding: 6px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #FFAAAA;
            }
        """)
        self.subtract_jugador_button.clicked.connect(self.quitar_jugador)
        self.main_layout.addWidget(self.subtract_jugador_button)

        self.crear_partida_button = QPushButton("Crear Partida", self)
        self.crear_partida_button.setStyleSheet("""
            QPushButton {
                padding: 6px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #4D4D4D;
            }
        """)
        self.crear_partida_button.setEnabled(False) 
        self.crear_partida_button.clicked.connect(self.crear_partida)
        self.main_layout.addWidget(self.crear_partida_button)
        
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
        self.boton_volver.clicked.connect(self.volver)
        self.main_layout.addWidget(self.boton_volver)

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
        
    def cambio_cant_jugadores(self):
        try:
            if 2 <= int(self.jugadores_iniciales_input.text()) <= 5:
                if int(self.jugadores_iniciales_input.text()) < len(self.jugadores):
                    self.add_jugador_button.setEnabled(False)
                    self.crear_partida_button.setEnabled(False)
                elif int(self.jugadores_iniciales_input.text()) > len(self.jugadores):
                    self.add_jugador_button.setEnabled(True)
                    self.crear_partida_button.setEnabled(False)
                else:
                    self.add_jugador_button.setEnabled(False)
                    self.crear_partida_button.setEnabled(True) 
            else:
                self.crear_partida_button.setEnabled(False)
                QMessageBox.warning(self, "Número inválido", "El número de jugadores debe ser entre 2 y 5.")
                self.jugadores_iniciales_input.setText("2")
        except Exception:
            print("Lista de jugadores vacía!")

    def agregar_jugador(self):
        # Limita el número de jugadores según el valor ingresado
        try:
            if len(self.jugadores) < int(self.jugadores_iniciales_input.text()):
                jugador_row = len(self.jugadores)

                # Nombre Label:
                nombre_label = QLabel(f"Jugador {jugador_row + 1}:")
                
                # Nombre Insertar texto:
                nombre_input = QLineEdit()
                nombre_input.setPlaceholderText("Nombre")
                
                # Selección Avatar Label:
                avatar_label = QLabel("Elija su avatar:")
                
                # Selección Avatar seleccionador:
                avatar_combo = QComboBox()
                avatar_combo.addItem("Avatar 1", "imagenes/ui/perfilRecortado1.png")
                avatar_combo.addItem("Avatar 2", "imagenes/ui/perfilRecortado2.png")
                avatar_combo.addItem("Avatar 3", "imagenes/ui/perfilRecortado3.png")
                avatar_combo.addItem("Avatar 4", "imagenes/ui/perfilRecortado4.png")
                avatar_combo.addItem("Avatar 5", "imagenes/ui/perfilRecortado5.png")
                avatar_combo.addItem("Avatar 6", "imagenes/ui/perfilRecortado6.png")
                avatar_combo.addItem("Avatar 7", "imagenes/ui/perfilRecortado7.png")
                avatar_combo.addItem("Avatar 8", "imagenes/ui/perfilRecortado8.png")

                # Añadir al layout
                self.jugadores_layout.addWidget(nombre_label, jugador_row, 0)
                self.jugadores_layout.addWidget(nombre_input, jugador_row, 1)
                self.jugadores_layout.addWidget(avatar_label, jugador_row, 2)
                self.jugadores_layout.addWidget(avatar_combo, jugador_row, 3)

                # Almacenar referencias de los widgets:
                # (Almaceno una referencia de los widgets de cada uno para que se puedan borrar).
                self.jugadores.append({
                    "nombre_label": nombre_label,
                    "nombre_input": nombre_input,
                    "avatar_label": avatar_label,
                    "avatar_combo": avatar_combo,
                    
                    'nombre': nombre_input,
                    'avatar': avatar_combo,
                    'dinero': int(self.dinero_inicial_input.text()) ,
                    'propiedades': [],
                    'banco': [],
                    'acciones': [],
                })

                # Deshabilitar botón agregar jugadores, y habilitar crear partida si es que se alcanza el límite:
                if len(self.jugadores) == int(self.jugadores_iniciales_input.text()):
                    self.add_jugador_button.setEnabled(False)
                    self.crear_partida_button.setEnabled(True) 
                
        except Exception:
            print("Hubo un error, seguramente no había valor en la caja.")
            self.jugadores_iniciales_input.setText("2") # <-- Para que vuelva a haber algo.
    
    def quitar_jugador(self):
        if self.jugadores:
            # Saca el último jugador que se agregó:
            jugador = self.jugadores.pop()

            # Elimino los widgets asociados a ese jugador:
            jugador["nombre_label"].deleteLater()
            jugador["nombre_input"].deleteLater()
            jugador["avatar_label"].deleteLater()
            jugador["avatar_combo"].deleteLater()

            # Habilito el botón de agregar si es que estaba deshabilitado:
            self.cambio_cant_jugadores()

    def crear_partida(self):
        if len(self.jugadores) == int(self.jugadores_iniciales_input.text()):
            dinero_inicial = int(self.dinero_inicial_input.text())
            jugadores = []

            # Datos Jugadores: (y así también se evita llevarse las 4 referencias de los widgets)
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
        else:
            print("La cantidad de jugadores indicados no coincide con los creados.")

    def start_game(self, dinero_inicial, jugadores):
        self.t = Tablero(self.main_menu, dinero_inicial, jugadores)
        self.t.show()
