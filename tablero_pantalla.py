from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QScrollArea, QGridLayout
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QIcon
#from carta_boton import CartaBoton

class Tablero(QMainWindow):
    def __init__(self, main_menu, dinero_inicial, jugadores, parent=None):
        super().__init__(parent)
        self.main_menu = main_menu
        self.setWindowTitle("Tablero de Juego")
        self.setGeometry(80, 50, 1400, 750)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))

        self.dinero_inicial = dinero_inicial
        self.jugadores = jugadores
        self.turno_actual = 0
        self.tiempo_restante = 60
        
        # Configuración del temporizador:
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_tiempo)
        self.tiempo_restante = 60
        self.timer.start(1000)
        
        # Widget principal:
        self.main_widget = QWidget(self)
        self.main_widget.setObjectName("MainWidget") # <-- Le doy el ID "MainWidget" para que funcione el CSS de abajo.
        self.setCentralWidget(self.main_widget)
        
        # Imagen de fondo usando CSS:
        self.main_widget.setStyleSheet("""

        """)
        
        # Esto va arriba, es el diseño, no lo pongo para poder probar los layouts sin imágenes o sin formatos:
        #self.main_widget.setStyleSheet("""
        #    QWidget#MainWidget {
        #        background-image: url("imagenes/ui/fondo_tablero.jpg");
        #        background-repeat: no-repeat;
        #        background-position: center;
        #        background-size: cover;
        #    }
        #    QLabel, QPushButton {
        #        background: none;
        #        border: none;
        #    }
        #""")

        # Layout principal (zona superior e inferior):
        # Instanciación y seteo de su layout.
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        
        # ---
        
        # Zona superior:
        self.zona_superior_layout = QHBoxLayout()
        self.main_layout.addLayout(self.zona_superior_layout, 2)
        
        # Espacio en el medio de ambas zonas:
        #self.espacio_vacio_layout = QHBoxLayout()
        #self.main_layout.addLayout(self.espacio_vacio_layout, 1)
        
        # Zona inferior:
        self.zona_inferior_layout = QHBoxLayout()
        self.main_layout.addLayout(self.zona_inferior_layout, 2)

        # ---
        
        # Zona superior izquierda:
        self.zona_superior_izquierda_layout = QVBoxLayout()
        self.zona_superior_layout.addLayout(self.zona_superior_izquierda_layout, 1) # <-- El 1 es que tiene proporción 1.
        self.mostrar_jugadores(jugadores)                                           # Si tienen ambos el mismo, van a
        #                                                                             ocupar el mismo ancho.
        # Zona superior derecha:
        self.zona_superior_derecha_layout = QVBoxLayout()
        self.zona_superior_layout.addLayout(self.zona_superior_derecha_layout, 1) # <-- (El comentario de arriba)
        #self.mostrar_tus_cartas()
        
        # ---
        
        # Zona inferior izquierda:
        self.zona_inferior_izquierda_layout = QVBoxLayout()
        self.zona_inferior_layout.addLayout(self.zona_inferior_izquierda_layout)
        
        # Zona inferior central:
        self.zona_inferior_central_layout = QVBoxLayout()
        self.zona_inferior_layout.addLayout(self.zona_inferior_central_layout)
        
        
        # Zona inferior derecha:
        self.zona_inferior_derecha_layout = QVBoxLayout()
        self.zona_inferior_layout.addLayout(self.zona_inferior_derecha_layout)

        # ---
        
        # Turno, reloj, finalizar turno, finalizar partida (Zona inferior izquierda)
        self.turno_label = QLabel(f"Turno de: {self.jugadores[self.turno_actual]['nombre']}", self)
        self.zona_inferior_izquierda_layout.addWidget(self.turno_label)

        self.timer_label = QLabel(f"Tiempo restante: {self.tiempo_restante}s", self)
        self.zona_inferior_izquierda_layout.addWidget(self.timer_label)
        
        self.espacio_vacio_label = QLabel("") # <-- Un espacio vacío.
        self.zona_inferior_izquierda_layout.addWidget(self.espacio_vacio_label)
        
        self.btn_finalizar_turno = QPushButton("Finalizar Turno", self)
        self.btn_finalizar_turno.clicked.connect(self.finalizar_turno)
        self.zona_inferior_izquierda_layout.addWidget(self.btn_finalizar_turno)
        
        self.btn_finalizar_partida = QPushButton("Finalizar Partida", self)
        self.btn_finalizar_partida.clicked.connect(self.finalizar_partida)
        self.zona_inferior_izquierda_layout.addWidget(self.btn_finalizar_partida)
        
        # Espacio en blanco, cartas (Zona inferior central)
        self.zona_inferior_central_layout.addWidget(self.espacio_vacio_label)
        
        self.cartas_layout = QHBoxLayout()
        self.zona_inferior_central_layout.addLayout(self.cartas_layout)
        
        self.ejemplo_de_mostrar_cartas_temporal()
        
        # Descripción carta (Zona inferior derecha)
        # self.descripcion_carta_layout = QVBoxLayout()
        # Este label en realidad debería ser una imagen (cuadroQueHaceLaCarta.png), sin borde, ni texto ni nada,
        #  y por arriba un label que ocupe el mismo tamaño y que se actualice con la descripción que corresponde.
        self.descripcion_carta_label = QLabel("Que hace la carta seleccionada:", self)
        self.descripcion_carta_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.descripcion_carta_label.setStyleSheet("border: 1px solid black;")
        self.zona_inferior_derecha_layout.addWidget(self.descripcion_carta_label)

    def mostrar_jugadores(self, jugadores):
        """Muestra la información de los jugadores."""
        for jugador in jugadores:
            jugador_layout = QHBoxLayout()                 # <-- Perfil | Propiedades | Banco | Acciones
            jugador_perfil_layout = QHBoxLayout()          # <-- Perfil: Avatar (izquierda) e info (derecha)
            jugador_nombre_y_dinero_layout = QVBoxLayout() # <-- Info: Nombre (arriba) y dinero (abajo)
            propiedades_layout = QGridLayout()
            banco_layout = QGridLayout()
            acciones_layout = QGridLayout()

            # --- Perfil ---
            
            # Avatar
            avatar = QPixmap(jugador["avatar"]).scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio)
            if avatar.isNull():
                print(f"Error! No se pudo cargar este avatar: {jugador['avatar']}")
            avatar_label = QLabel(self)
            avatar_label.setPixmap(avatar)
            jugador_perfil_layout.addWidget(avatar_label)
            
            # Nombre y dinero
            nombre_label = QLabel(f"{jugador['nombre']}")
            nombre_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            dinero_label = QLabel(f"${jugador['dinero']}")
            dinero_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            jugador_nombre_y_dinero_layout.addWidget(nombre_label)
            jugador_nombre_y_dinero_layout.addWidget(dinero_label)
            jugador_perfil_layout.addLayout(jugador_nombre_y_dinero_layout)
            
            # Agregar perfil al layout completo del jugador:
            jugador_layout.addLayout(jugador_perfil_layout, 1)
            
            # --- Propiedades ---
            propiedades_widget = QWidget(self)
            propiedades_widget.setLayout(propiedades_layout)
            propiedades_widget.setFixedSize(200, 150)  # Tamaño fijo para la cuadrícula
            self.mostrar_cartas_en_cuadricula(propiedades_layout, jugador["propiedades"], "propiedades")
            jugador_layout.addWidget(propiedades_widget, 1)
            
            # --- Banco ---
            banco_widget = QWidget(self)
            banco_widget.setLayout(banco_layout)
            banco_widget.setFixedSize(200, 150)  # Tamaño fijo para la cuadrícula
            self.mostrar_cartas_en_cuadricula(banco_layout, jugador["banco"], "banco")
            jugador_layout.addWidget(banco_widget, 1)
            
            # --- Acciones ---
            acciones_widget = QWidget(self)
            acciones_widget.setLayout(acciones_layout)
            acciones_widget.setFixedSize(100, 150)  # Tamaño fijo para la cuadrícula
            self.mostrar_cartas_en_cuadricula(acciones_layout, jugador["acciones"], "acciones")
            jugador_layout.addWidget(acciones_widget, 1)
            
            # Versión antigua:
            #self.mostrar_cartas_en_cuadricula(acciones_layout, jugador["acciones"])
            #jugador_layout.addLayout(acciones_layout, 1)
            
            # Agregar layout jugador al layout de la zona superior izquierda: <-- (Este es el paso final de cada uno)
            self.zona_superior_izquierda_layout.addLayout(jugador_layout)
    
    def mostrar_cartas_en_cuadricula(self, grid_layout, cartas, tipo=None):
        """
        Rellena la cuadrícula con las imágenes de las cartas que tiene
        y asegura que todas las celdas estén presentes, incluso si están vacías.
        """
        
        if tipo != "acciones":
            columnas = 6  # z-- Número fijo de columnas.
            filas = 3     # <-- Número fijo de filas.
        else:
            columnas = 3
            filas = 2
        total_celdas = filas * columnas

        cartas = cartas if cartas else []

        for index in range(total_celdas):
            fila = index // columnas
            columna = index % columnas

            if index < len(cartas):
                # Si hay una carta en esta posición, mostrar la carta
                carta = cartas[index]
                carta_label = QLabel(self)
                pixmap = QPixmap(carta["imagen"]).scaled(25, 40, Qt.AspectRatioMode.KeepAspectRatio)
                carta_label.setPixmap(pixmap)
                grid_layout.addWidget(carta_label, fila, columna)
            else:
                # Si no hay carta, agregar un QLabel vacío como placeholder
                placeholder = QLabel(self)
                placeholder.setFixedSize(25, 40)  # Tamaño fijo para las celdas vacías
                placeholder.setStyleSheet("background-color: transparent; border: 1px solid gray;")
                grid_layout.addWidget(placeholder, fila, columna)

    # (!!!) Este método está causando problemas, mueve el mazo hacia arriba cuando se resetea el timer.
    # Cuando modifica algo que no se que cosa es, causa problemas.
    # Para mi que no hay que borrar las cartas, sinó mantener los widgets, y en donde no haya una carta
    #  poner un rectángulo vacío o una imágen o algo que muestre que no hay una carta ahí.
    def mostrar_mano_jugador(self):
        """Muestra las cartas del jugador actual."""
        for i in reversed(range(self.zona_inferior_central_layout.count())):
            widget = self.zona_inferior_central_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        jugador = self.jugadores[self.turno_actual]
        #for carta in jugador["mano"]:
            #carta_boton = CartaBoton(carta, f"Efecto de {carta}", self)
            #self.mano_layout.addWidget(carta_boton)

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
        # self.timer.stop() <-- Da delay
        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)
        self.turno_label.setText(f"Turno de: {self.jugadores[self.turno_actual]['nombre']}")
        self.tiempo_restante = 60
        self.timer_label.setText(f"Tiempo restante: {self.tiempo_restante}s")

        self.mostrar_mano_jugador()
    
    def finalizar_partida(self):
        self.close()
        self.main_menu.show()
    
    # Este es un ejemplo, esto es algo que debería estar en el método de arriba "mostrar_mano_jugador"
    def ejemplo_de_mostrar_cartas_temporal(self):
        """Muestra las cartas activas."""
        for _ in range(7):
            carta_label = QLabel("Carta")
            carta_label.setFixedSize(100, 150)
            carta_label.setStyleSheet("border: 1px solid black;")
            self.cartas_layout.addWidget(carta_label)