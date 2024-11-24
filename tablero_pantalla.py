from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QScrollArea, QGridLayout, QSizePolicy, QFrame, QSpacerItem, QMessageBox
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QIcon
from datetime import datetime
#from carta_boton import CartaBoton <-- (Yo no lo puse, tampoco se que haría)

class Tablero(QMainWindow):
    def __init__(self, main_menu, jugadores, parent=None):
        super().__init__(parent)
        self.main_menu = main_menu
        self.setWindowTitle("Tablero de Juego")
        self.setGeometry(20, 30, 1500, 750)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))

        self.dinero_inicial = 0 # <-- No le veo mucho sentido a esto así.
        self.jugadores = jugadores
        self.turno_actual = 0
        self.tiempo_restante = 60
        
        self.carta_seleccionada = None
        
        # Registro del tiempo de inicio de la partida:
        self.tiempo_inicio = datetime.now()
        
        # Configuración del temporizador:
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_tiempo)
        self.timer.start(1000)
        
        # Configuración para el titileo del reloj:
        self.titileo_timer = QTimer(self)
        self.titileo_timer.timeout.connect(self.titilar_reloj)
        self.reloj_titilando = False
        
        # Widget principal:
        self.main_widget = QWidget(self)
        self.main_widget.setObjectName("MainWidget") # <-- Le doy el ID "MainWidget" para que funcione el CSS de abajo.
        self.setCentralWidget(self.main_widget)
        
        # Imagen de fondo usando CSS:
        self.main_widget.setStyleSheet("""
            QWidget#MainWidget {
                background-image: url("imagenes/ui/fondo_tablero_1650x820.jpg");
                background-repeat: no-repeat;
                background-position: center;
            }
            QLabel, QPushButton {
                background: none;
                border: none;
            }
        """)
        
        # background-size: contain; <-- No funciona (funcionaba)

        # Layout principal (zona superior e inferior):
        # Instanciación y seteo de su layout.
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        
        # ---
        
        # Zona superior:
        self.zona_superior_layout = QHBoxLayout()
        self.main_layout.addLayout(self.zona_superior_layout, 2)
        
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

        # ----------------------------------------------------------------------
        # (Zona inferior izquierda):
        # (1) Empuje hacia abajo <-- Fijense, pruebenlo si les gusta empujado hacia abajo o sin eso, se ven distinto.
        # (2) Turno
        # (3) reloj
        # (Opcional): Espacio en blanco
        # (4) finalizar turno
        # (5) finalizar partida

        # (1):
        spacer_superior = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.zona_inferior_izquierda_layout.addItem(spacer_superior)
        
        # (2):
        turno_layout = QHBoxLayout()

        turno_icon = QLabel(self)
        turno_pixmap = QPixmap("imagenes/ui/turn.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        turno_icon.setPixmap(turno_pixmap)
        turno_icon.setFixedSize(50, 50) # <-- Hace que QLabel sea del mismo tamaño para que coincida con el del QPixmap.
        turno_layout.addWidget(turno_icon)

        self.turno_label = QLabel(f"Turno de: {self.jugadores[self.turno_actual]['nombre']}", self)
        turno_layout.addWidget(self.turno_label)

        self.zona_inferior_izquierda_layout.addLayout(turno_layout)

        # (3):
        tiempo_layout = QHBoxLayout()

        self.reloj_icon = QLabel(self)
        self.reloj_pixmap = QPixmap("imagenes/ui/fixedClock.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.reloj_rojo_pixmap = QPixmap("imagenes/ui/fixedClockRojo.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.reloj_icon.setPixmap(self.reloj_pixmap)
        self.reloj_icon.setFixedSize(50, 50) # <-- Hace que QLabel sea del mismo tamaño para que coincida con el del QPixmap.
        tiempo_layout.addWidget(self.reloj_icon)

        self.timer_label = QLabel(f"Tiempo restante: {self.tiempo_restante}s", self)
        tiempo_layout.addWidget(self.timer_label)

        self.zona_inferior_izquierda_layout.addLayout(tiempo_layout)
        
        # (Espacio vacío opcional entre medio):
        self.espacio_vacio_label = QLabel("") # <-- Un espacio vacío.
        self.zona_inferior_izquierda_layout.addWidget(self.espacio_vacio_label)
        
        # (4):
        self.btn_finalizar_turno = QPushButton("Finalizar Turno", self)
        self.btn_finalizar_turno.clicked.connect(self.finalizar_turno)
        self.zona_inferior_izquierda_layout.addWidget(self.btn_finalizar_turno)
        self.btn_finalizar_turno.setStyleSheet("""
            QPushButton {
                background-color: rgba(194, 78, 27, 0.2);
                color: white;
                border: 2px solid rgba(43, 22, 11, 1);
                border-radius: 10px;
                padding: 8px;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(194, 137, 48, 0.9);
            }
            QPushButton:pressed {
                background-color: rgba(125, 72, 34, 1);
            }
        """)
        
        # (5):
        self.btn_finalizar_partida = QPushButton("Finalizar Partida", self)
        self.btn_finalizar_partida.clicked.connect(self.finalizar_partida)
        self.zona_inferior_izquierda_layout.addWidget(self.btn_finalizar_partida)
        self.btn_finalizar_partida.setStyleSheet("""
            QPushButton {
                background-color: rgba(194, 78, 27, 0.2);
                color: white;
                border: 2px solid rgba(43, 22, 11, 1);
                border-radius: 10px;
                padding: 8px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(194, 137, 48, 0.9);
            }
            QPushButton:pressed {
                background-color: rgba(125, 72, 34, 1);
            }
        """)
        
        # ----------------------------------------------------------------------
        # Espacio en blanco, cartas (Zona inferior central)
        self.zona_inferior_central_layout.addWidget(self.espacio_vacio_label)
        
        self.cartas_layout = QHBoxLayout()
        self.zona_inferior_central_layout.addLayout(self.cartas_layout)
        
        self.mostrar_mano_jugador()
        
        # ----------------------------------------------------------------------
        # Descripción carta (Zona inferior derecha)
        descripcion_carta_layout = QVBoxLayout()

        # Descripción de carta
        self.descripcion_carta_label = QLabel(self)
        pixmap_fondo = QPixmap("imagenes/ui/queHaceVacio.png").scaled(400, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.descripcion_carta_label.setPixmap(pixmap_fondo) #                  |                                   | Estos dos dos Qt solucionan la vida.
        self.descripcion_carta_label.setFixedSize(400, 300)

        # Agregar el QLabel al layout:
        descripcion_carta_layout.addWidget(self.descripcion_carta_label)

        # Agregar el layout al área de la zona inferior derecha:
        self.zona_inferior_derecha_layout.addLayout(descripcion_carta_layout)

        # --- Versión antigua con marco negro: ---
        # self.descripcion_carta_layout = QVBoxLayout()
        # Este label en realidad debería ser una imagen (cuadroQueHaceLaCarta.png), sin borde, ni texto ni nada,
        #  y por arriba un label que ocupe el mismo tamaño y que se actualice con la descripción que corresponde.
        #self.descripcion_carta_label = QLabel("Que hace la carta seleccionada:", self)
        #self.descripcion_carta_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #self.descripcion_carta_label.setStyleSheet("border: 1px solid black;")
        #self.zona_inferior_derecha_layout.addWidget(self.descripcion_carta_label)

    def mostrar_jugadores(self, jugadores):
        """Muestra la información de los jugadores."""
        for jugador in jugadores:
            jugador_layout = QHBoxLayout()                 # Perfil | Propiedades | Banco | Acciones
            propiedades_layout = QGridLayout()
            banco_layout = QGridLayout()
            acciones_layout = QGridLayout()

            # --- Perfil ---

            # Crear un contenedor para todo el conjunto de avatar, nombre y dinero:
            perfil_contenedor = QWidget(self)
            perfil_contenedor.setStyleSheet("""
                QWidget {
                    background-color: rgba(207, 106, 39, 0.2);
                    border: 2px solid rgba(43, 22, 11, 1);
                    border-radius: 10px;
                    padding: 10px;         /*<-- Padding es un espaciado interno, super útil. */
                }
            """)

            # Layout del contenedor:
            perfil_layout = QHBoxLayout(perfil_contenedor)
            perfil_layout.setContentsMargins(10, 10, 10, 10) # <-- Márgenes internos del contenedor
            perfil_layout.setSpacing(15)                     # <-- Espaciado entre el avatar y el texto

            # Avatar:
            avatar = QPixmap(jugador["avatar"]) # <-- (No escalar acá)
            if avatar.isNull():
                print(f"Error! No se pudo cargar este avatar: {jugador['avatar']}")
            avatar_label = QLabel(self)
            avatar_label.setPixmap(avatar)

            # Configuración para escalar el avatar adentro del espacio disponible:
            avatar_label.setScaledContents(True)   # <-- (Muy opcional) Permite que la imagen se escale dentro del QLabel.
            avatar_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

            # Definir un tamaño máximo y mínimo para evitar que ocupe toda la pantalla:
            avatar_label.setMaximumSize(100, 100)
            avatar_label.setMinimumSize(50, 50)    # <-- (Opcional)

            # Agregar el avatar al layout del contenedor:
            perfil_layout.addWidget(avatar_label) #, alignment=Qt.AlignmentFlag.AlignLeft)

            # Contenedor para el texto (nombre y dinero):
            texto_layout = QVBoxLayout()
            texto_layout.setSpacing(5)   # <-- Espaciado entre el nombre y el dinero.

            # Nombre:
            nombre_label = QLabel(f"{jugador['nombre']}")
            nombre_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            nombre_label.setStyleSheet("""
                font-size: 14px; 
                font-weight: bold;
                color: white;
                background-color: rgba(46, 21, 8, 0.7);
                padding: 5px;
                border-radius: 5px;
            """)
            texto_layout.addWidget(nombre_label)

            # Dinero:
            dinero_label = QLabel(f"${jugador['dinero']}")
            dinero_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            dinero_label.setStyleSheet("""
                font-size: 14px;
                font-weight: bold;
                color: white;
                background-color: rgba(46, 21, 8, 0.7);
                padding: 5px;
                border-radius: 5px;
            """)
            texto_layout.addWidget(dinero_label)

            # Agregar el layout del texto al perfil:
            perfil_layout.addLayout(texto_layout)
            dinero_label.setFixedSize(100, 50)

            # Agregar el contenedor al layout del jugador:
            jugador_layout.addWidget(perfil_contenedor)
            
            # --- Propiedades ---
            propiedades_widget = QWidget(self)
            propiedades_widget.setLayout(propiedades_layout)
            propiedades_widget.setFixedSize(250, 100) # <-- Tamaño fijo para la cuadrícula.
            self.mostrar_cartas_en_cuadricula(propiedades_layout, jugador["propiedades"], "propiedades")
            jugador_layout.addWidget(propiedades_widget, 2)
            
            # --- Banco ---
            banco_widget = QWidget(self)
            banco_widget.setLayout(banco_layout)
            banco_widget.setFixedSize(250, 100)       # <-- Tamaño fijo para la cuadrícula.
            self.mostrar_cartas_en_cuadricula(banco_layout, jugador["banco"], "banco")
            jugador_layout.addWidget(banco_widget, 2)
            
            # Agregar el layout jugador al layout de la zona superior izquierda:
            self.zona_superior_izquierda_layout.addLayout(jugador_layout)
    
    def mostrar_cartas_en_cuadricula(self, grid_layout, cartas, tipo=None):
        """
        Rellena la cuadrícula indicada con las imágenes de las cartas que tiene
        y se asegura de que todas las celdas estén presentes, incluso si están vacías.
        """
        columnas = 9
        filas = 2
        total_celdas = filas * columnas

        cartas = cartas if cartas else []

        for index in range(total_celdas):
            fila = index // columnas
            columna = index % columnas

            if index < len(cartas):
                # Si hay una carta en esta posición, muestra la carta:
                carta = cartas[index]
                carta_label = QLabel(self)
                pixmap = QPixmap(carta["imagen"]).scaled(23, 40, Qt.AspectRatioMode.KeepAspectRatio)
                carta_label.setPixmap(pixmap)
                grid_layout.addWidget(carta_label, fila, columna)
            else:
                # Si no hay carta, agrega un QLabel vacío como placeholder:
                placeholder = QLabel(self)
                placeholder.setFixedSize(25, 40) # <-- Tamaño fijo para las celdas vacías.
                placeholder.setStyleSheet("background-color: transparent; border: 1px solid gray;")
                grid_layout.addWidget(placeholder, fila, columna)

    def mostrar_mano_jugador(self):
        """Muestra las cartas en la mano del jugador actual y actualiza la descripción."""
        
        # Limpiar el área de las cartas antes de agregar otras nuevas:
        while self.cartas_layout.count():
            widget = self.cartas_layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

        jugador_actual = self.jugadores[self.turno_actual]
        cartas = jugador_actual.get("mano", [])
        
        imagen_vacia = "imagenes/cartas/cartaVacia.png"

        # Lógica para mostrar hasta 7 cartas:
        for i in range(7):      # <-- (No se va a exceder, pero igual tengo que usarlo).
            # Creación del widget de cada carta:
            carta_label = QLabel(self)
            
            # Esta disposición del código es perfecta, hace que al seleccionar una carta vacía no se actualice la imagen de descripció:
            if i < len(cartas):
                carta = cartas[i]
                carta_imagen = carta["imagen"]
                # Actualizar al clickear:
                carta_label.mousePressEvent = self.evento_click_carta(carta)
            else:
                carta_imagen = imagen_vacia
                descripcion_imagen = None # <-- Ya no es necesario.
            pixmap = QPixmap(carta_imagen).scaled(100, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            carta_label.setPixmap(pixmap)
            carta_label.setFixedSize(100, 150)
            #carta_label.setStyleSheet("border: 1px solid black;") <-- Opcional

            # Agregar carta al layout:
            self.cartas_layout.addWidget(carta_label)

    def evento_click_carta(self, carta):
        """Actualizar la imagen de descripción al haber hecho click, por la imagen que se indica."""
        def evento(_):
            descripcion_imagen = carta["descripcion_imagen"]
            if carta == self.carta_seleccionada:
                #print("Doble click detectado.")
                print("Estás tratando de usar la carta.")
            else:
                #print("Un solo click.")
                self.carta_seleccionada = carta # <-- Almacena primer click.
                if descripcion_imagen: # <-- En caso de que si tenga contenido descripcion_imagen.
                    pixmap_descripcion = QPixmap(descripcion_imagen).scaled(400, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    self.descripcion_carta_label.setPixmap(pixmap_descripcion)
                else:                  # <-- En caso de que sea Null porque no hay carta, usa la imagen vacía. (Igual ya no va a pasar)
                    pixmap_descripcion = QPixmap("imagenes/ui/queHaceVacio.png").scaled(400, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    self.descripcion_carta_label.setPixmap(pixmap_descripcion)
        return evento

    def titilar_reloj(self):
        """Alterna entre las dos imágenes del reloj para crear el efecto del titileo."""
        if self.reloj_titilando:
            self.reloj_icon.setPixmap(self.reloj_pixmap)
        else:
            self.reloj_icon.setPixmap(self.reloj_rojo_pixmap)
        self.reloj_titilando = not self.reloj_titilando

    def actualizar_tiempo(self):
        """Actualiza el temporizador."""
        if self.tiempo_restante > 0:
            self.tiempo_restante -= 1
            self.timer_label.setText(f"Tiempo restante: {self.tiempo_restante}s")
        # Iniciar el titileo cuando queden 5, o 10, o 15, segundos. <-- (A gusto como quieran, me parece que 15 está bien)
            if self.tiempo_restante <= 15:
                if not self.titileo_timer.isActive():
                    self.titileo_timer.start(500)     # <-- Esto cambia la imagen cada 500 ms.
        else:
            self.titileo_timer.stop() # <-- Detiene el titileo cuando el tiempo termine.
            self.finalizar_turno()

    def finalizar_turno(self):
        """
        Finaliza el turno y pasa al siguiente jugador.
        Acá va la lógica que se maneja cuando finaliza el tiempo.
        """
        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)
        self.turno_label.setText(f"Turno de: {self.jugadores[self.turno_actual]['nombre']}")
        self.tiempo_restante = 60
        self.timer_label.setText(f"Tiempo restante: {self.tiempo_restante}s")

        self.reloj_icon.setPixmap(self.reloj_pixmap)
        self.titileo_timer.stop()
        
        self.carta_seleccionada = None
        
        self.mostrar_mano_jugador()
    
    def finalizar_partida(self):
        """Pregunta al usuario si está seguro de que la quiere finalizar."""
        respuesta = QMessageBox.question(
            self,
            "Confirmar finalización",
            "¿Estás seguro de que querés finalizar la partida?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if respuesta == QMessageBox.StandardButton.Yes:

            # Cálculo del tiempo:
            tiempo_fin = datetime.now()
            tiempo_total = tiempo_fin - self.tiempo_inicio # <-- Diferencia entre el inicio y el final.
            minutos, segundos = divmod(tiempo_total.total_seconds(), 60)
            tiempo_formateado = f"{int(minutos)} minutos y {int(segundos)} segundos"
            
            # Cálculo del resumen de la partida:
            resumen = "Resumen de la partida jugada:\n\n"
            resumen += f"Tiempo total jugado: {tiempo_formateado}\n\n"
            for jugador in self.jugadores:
                resumen += (
                    f"Jugador: {jugador['nombre']}\n"
                    f"Dinero final: ${jugador['dinero']}\n"
                    f"Propiedades adquiridas: {len(jugador.get('propiedades', []))}\n"
                    f"Cartas de acción usadas: {len(jugador.get('acciones', []))}\n\n"
                )
            resumen += "Muchas gracias por jugar!"
            
            # Mostrar el cuadro con la información de la partida:
            QMessageBox.information(
                self,
                "Resumen de la Partida",
                resumen,
                QMessageBox.StandardButton.Ok
        )
            
            self.close()
            self.main_menu.show()
        else:
            pass
    
    # ----------------------------------------------------------------------------------------------------
    # Cosas a implementar:
    #
    # 1. (listo) Se debería poder seleccionar la carta y que la imagen "queHace" cambie a su respectivo queHace.
    #
    # 2. (listo) Cuando hay menos de 7 cartas no modificar los widget o esas cosas porque rompe los layout,
    #     sinó más bien reemplazar la imagen de la carta por una imagen transparente vacía (cartaVacia.png).
    #
    # 3. Cuando se seleccione la carta que salga un cuadro de diálogo con las opciones que correspondan a
    #     esa carta, porque si se fijan literalmente cada carta hace cosas re distintas y algunas son muchísimo
    #     más complejas que otras. (Ej: Alquiler doble, léanla, van a verlo)
    #
    # 4. Cuando se juegue la carta que se cambie el turno.