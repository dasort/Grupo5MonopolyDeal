from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QGridLayout, QMessageBox, QSizePolicy, QSpacerItem
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
        
        self.minimo_jugadores = 2
        self.maximo_jugadores = 5
        self.dinero_inicial = 0 # <-- Temporal, debería ser random.
        self.jugadores = []

        # Botones
        # 1. add_jugador
        # 2. subtract_jugador
        # 3. crear_partida_button
        # 4. boton_volver

        # ---
        
        # Cuadrícula "Agregar Jugador":
        self.jugadores_layout = QGridLayout()
        self.main_layout.addLayout(self.jugadores_layout)

        # ---

        self.main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        
        self.aclaracion_label = QLabel("(Opcional): Iniciar sesión para guardar tus estadísticas.")
        self.main_layout.addWidget(self.aclaracion_label)
        
        # ---
        
        # Botón "Agregar Jugador":
        self.agregar_jugador_boton = QPushButton("Agregar Jugador", self)
        self.agregar_jugador_boton.setStyleSheet("""
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
        self.agregar_jugador_boton.clicked.connect(self.agregar_jugador)
        self.main_layout.addWidget(self.agregar_jugador_boton)
        
        # ---

        # Botón "Quitar Jugador":
        self.quitar_jugador_boton = QPushButton("Quitar Jugador", self)
        self.quitar_jugador_boton.setStyleSheet("""
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
        self.quitar_jugador_boton.setEnabled(False)
        self.quitar_jugador_boton.clicked.connect(self.quitar_jugador)
        self.main_layout.addWidget(self.quitar_jugador_boton)

        # ---

        # Botón "Crear Partida":
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
        self.crear_partida_button.setEnabled(False) # <-- Para evitar que se pueda crear una partida sin jugadores.
        self.crear_partida_button.clicked.connect(self.crear_partida)
        self.main_layout.addWidget(self.crear_partida_button)

        # ---

        # Botón "Volver al Menú Principal":
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

    def volver(self):
        self.hide()
        self.main_menu.show()
        
    def cambio_cant_jugadores(self):
        print(len(self.jugadores))
        try:
            
            # Manejo lo que pasa si tiene lo necesario:
            if len(self.jugadores) >= self.minimo_jugadores:
                
                # Se llegó al máximo:
                if len(self.jugadores) == self.maximo_jugadores:
                    self.agregar_jugador_boton.setEnabled(False)
                
                # Menos que el máximo:
                else:
                    self.agregar_jugador_boton.setEnabled(True)   # <-- Si o si.
                    self.crear_partida_button.setEnabled(True) # <-- Si o si.
            
            # Manejo lo que pasa si no tiene lo necesario:
            else:
                
                if len(self.jugadores) == 2:
                    self.crear_partida_button.setEnabled(True)
                
                # Igual a 1 jugador:
                if len(self.jugadores) == 1:
                    self.quitar_jugador_boton.setEnabled(True)
                    self.crear_partida_button.setEnabled(False)
                
                # 0 jugadores:
                else:
                    self.quitar_jugador_boton.setEnabled(False)
        
        except Exception:
            print("Lista de jugadores vacía!")

    def agregar_jugador(self):
        try:
            jugador_row = len(self.jugadores)

            # El texto del tooltip con CSS (para el <br>):
            tooltip_text = (
                "1. Puede iniciar sesión y aparecerá con su nombre de cuenta.<br>"
                "2. Si no inicia sesión puede ingresar el nombre que quiera.<br>"
                "3. Si no ingresa nombre aparecerá como anónimo."
            )
            
            # Nombre Label:
            nombre_label = QLabel(f"Jugador {jugador_row + 1}:")
            nombre_label.setToolTip(tooltip_text)
            
            # Nombre Insertar texto:
            nombre_input = QLineEdit()
            nombre_input.setPlaceholderText("Nombre")
            nombre_input.setToolTip(tooltip_text)
            
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
            
            # Selección Iniciar sesión Label:
            sesion_label = QLabel("Iniciar sesión:")
            sesion_label.setToolTip(tooltip_text)
            
            # Iniciar sesión botón:
            boton_cuenta = QPushButton("Inicie", self)
            boton_cuenta.clicked.connect(self.volver) # <-- Cambiar
            boton_cuenta.setToolTip(tooltip_text)

            # Añadir al layout
            self.jugadores_layout.addWidget(nombre_label, jugador_row, 0)
            self.jugadores_layout.addWidget(nombre_input, jugador_row, 1)
            self.jugadores_layout.addWidget(avatar_label, jugador_row, 2)
            self.jugadores_layout.addWidget(avatar_combo, jugador_row, 3)
            self.jugadores_layout.addWidget(sesion_label, jugador_row, 4)
            self.jugadores_layout.addWidget(boton_cuenta, jugador_row, 5)

            # Almacenar referencias de los widgets:
            # (Almaceno una referencia de los widgets de cada uno para que se puedan borrar).
            self.jugadores.append({
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

            # Asegurarme que los botones se activen o desactiven cuando deban:
            self.cambio_cant_jugadores() # <-- Es clave que esto se ejecute al final de cuando se agrega el jugador.
                
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
            jugador["sesion_label"].deleteLater()
            jugador["boton_cuenta"].deleteLater()

            # Habilito el botón de agregar si es que estaba deshabilitado:
            self.cambio_cant_jugadores()

    def crear_partida(self):
        dinero_inicial = self.dinero_inicial
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
        self.start_game(jugadores)

    def start_game(self, jugadores):
        self.t = Tablero(self.main_menu, jugadores)
        self.t.show()