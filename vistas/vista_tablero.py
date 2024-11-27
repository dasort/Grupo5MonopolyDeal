from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QScrollArea, QGridLayout, QSizePolicy, QFrame, QSpacerItem, QMessageBox
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QIcon
from datetime import datetime
from pathlib import Path


class Tablero(QMainWindow):
    def __init__(self, controlador, parent=None):
        super().__init__()
        self.__controlador = controlador
        
        self.setWindowTitle("Tablero de Juego")
        self.setGeometry(20, 30, 1500, 750)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))

        path_script = Path(__file__).resolve()
        self.path_proyecto = path_script.parent.parent
        
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
        # Layout principal (zona superior e inferior):
        #region Instanciación y seteo de su layout.
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
        self.mostrar_jugadores(self.__controlador.get_jugadores())                                           # Si tienen ambos el mismo, van a
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
        #endregion
        # ----------------------------------------------------------------------
        #region ZONA DE BOTONES Y TURNOS
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

        self.turno_label = QLabel(f"Turno de: {self.__controlador.get_jugador_actual().nombre}", self)
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
        self.btn_finalizar_turno.clicked.connect(self.__controlador.terminar_turno)
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
        self.btn_finalizar_partida.clicked.connect(self.__controlador.terminar_partida)
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
        #endregion
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
        
        self.path_queHaceVacio = self.path_proyecto / "imagenes/ui/queHaceVacio.png"
        self.path_queHaceVacio = self.path_queHaceVacio.as_posix()

        pixmap_fondo = QPixmap(self.path_queHaceVacio).scaled(400, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.descripcion_carta_label.setPixmap(pixmap_fondo) #                  |                                   | Estos dos dos Qt solucionan la vida.
        self.descripcion_carta_label.setFixedSize(400, 300)
        # Agregar el QLabel al layout:
        descripcion_carta_layout.addWidget(self.descripcion_carta_label)
        # Agregar el layout al área de la zona inferior derecha:
        self.zona_inferior_derecha_layout.addLayout(descripcion_carta_layout)
    #region -------------------  MINI ZOOM  ------------------------
        # Agregar el Mini menu
        ventana = QWidget()
        
        ventana.setStyleSheet("""
            QWidget {
                border: 3px solid red; /* Borde rojo */
                border-radius: 5px; /* Esquinas redondeadas */
                padding: 10px; /* Espaciado interno */
                background-color: transparent; /* Color de fondo */
            }
        """)
        # Layout principal
        contenedor = QVBoxLayout()
        contenedor.setContentsMargins(0, 0, 0, 0)
        # Crear el primer widget (cartas)
        cartas_ = QWidget()
        #cartas.setFixedSize(100, 150)
        self.cartas_layouts = QGridLayout(cartas_)  # Layout interno de "cartas"
        self.cartas_layouts.setContentsMargins(0, 0, 0, 0)
        # .setStyleSheet("background-color: transparent;")
    

        

        
        #self.cartas_layout.addWidget(QLabel("a"), 0, 3)
        # Crear el widget con los botones
        botones = QWidget()
        self.botones_layout = QHBoxLayout(botones)  # Layout interno de "botones"
        cartas_ = QWidget()
        self.cartas_layouts = QGridLayout(cartas_)
        self.pestaña_cartas()
        
        
        botones.setStyleSheet("""
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
        # Añadir los widgets al layout principal
        contenedor.addWidget(cartas_)  # Primera fila
        contenedor.addWidget(botones)  # Segunda fila # Segunda fila
        contenedor.setStretch(0, 8)  # El primer widget (cartas) ocupa el 80% del espacio
        contenedor.setStretch(1, 2)  # El segundo widget (botones) ocupa el 20% del espacio

        ventana.setLayout(contenedor)
        ventana.setFixedSize(700, 400)
        self.zona_superior_derecha_layout.addWidget(ventana)
        
        #self.agregar_cartas()
        
        
        
        #endregion update
    
    def cargar_cartas(self,tipo,jugador):
        self.limpiar_layout(self.cartas_layouts)
        filas = 0
        columnas = 0
        maximo = filas * columnas
        if tipo == "propiedad":
            cantidad = self.contar_propiedades(jugador.get_propiedades)
            clase = jugador.propiedades
            listas =  clase.lista_grupos()
            if len(listas) < 11:
                for diccionarios in listas:
                    if isinstance(diccionarios, dict):
                        columnas += 1
                        grupo =  self.agregar_cartas(diccionarios["sublista"])
                        self.cartas_layouts.addWidget(grupo, filas, columnas)
                        if columnas == 5:
                            filas +=1
                            columnas = 0
                            print("llego al for de diccionarios")
                    else:
                        print("No es un diccionario")
        elif tipo == "dinero":
            
            lista = jugador.get_banco  # Llamas al método para obtener la lista
            sublistas = [lista[i:i + 5] for i in range(0, len(lista), 5)]
            if len(sublistas) < 11:
                for cartas in sublistas:
                    
                    columnas += 1
                    grupo =  self.agregar_cartas(cartas)
                    self.cartas_layouts.addWidget(grupo, filas, columnas)
                    if columnas == 5:
                        filas +=1
                        columnas = 0
                
                
    def agregar_cartas(self, sublista):
        grupos = QWidget()
        for index, lista in enumerate(sublista):
            print("llego al for de sublistas")
            #propiedad = lista[index]
            carta = QLabel(self)
            #carta.mousePressEvent = self.evento_click_carta(carta)# Crea un QLabel para cada carta
            carta.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            carta.setScaledContents(True)
            carta.setMinimumSize(60, 100)  # Tamaño mínimo de la carta
            carta.setMaximumSize(80, 120)  # Tamaño máximo de la carta
            pixmap = QPixmap(lista.path_a_imagen)
            carta.setPixmap(pixmap)  # Establece la imagen en el QLabel
            self.agregar_carta(carta, grupos, offset=index * 20)
        return grupos
    def agregar_carta(self, carta, padre, offset):
        """
        Agrega una carta al widget `mano_contenedora` con un desplazamiento para simular superposición.
        """
        max_width = padre.width()  # Obtiene el ancho máximo del contenedor
        if offset < max_width:  # Si el desplazamiento está dentro de los límites del contenedor
            carta.setParent(padre)  # Establecer el padre
            carta.move(offset, 20)  # Posicionar con superposición (offset horizontal)
            carta.show()
        else:
            print("No hay suficiente espacio para mover la carta.")
    #endregion
    def limpiar_layout(self, layout):
        """Elimina todos los widgets de un layout."""
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            elif item.layout():
                self.limpiar_layout(item.layout())
    def update_interfaz(self):
        self.pestaña_cartas()
        self.mostrar_jugadores(self.__controlador.get_jugadores())
        self.mostrar_mano_jugador()
        self.repaint()
    def pestaña_cartas(self):
        self.limpiar_layout(self.botones_layout)
        self.limpiar_layout(self.cartas_layouts)
        propiedades_button = QPushButton("Propiedades")
        dinero_button = QPushButton("Dinero")
        descarte_button = QPushButton("Descarte")
        propiedades_button.clicked.connect(lambda:self.cargar_cartas("propiedad", self.__controlador.get_jugador_actual()))
        dinero_button.clicked.connect(lambda:self.cargar_cartas("dinero", self.__controlador.get_jugador_actual()))
        # descarte_button.clicked.connect(self.elejir_color)
        self.botones_layout.addWidget(propiedades_button)
        self.botones_layout.addWidget(dinero_button)
        self.botones_layout.addWidget(descarte_button)    
    def limpiar_layout(self, layout):
        """Elimina todos los widgets de un layout."""
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            elif item.layout():
                self.limpiar_layout(item.layout())
                
    def mostrar_jugadores(self, jugadores):
        """Muestra la información de los jugadores."""
        self.limpiar_layout(self.zona_superior_izquierda_layout)
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
            avatar = QPixmap(jugador.avatar) # <-- (No escalar acá)
            if avatar.isNull():
                print(f"Error! No se pudo cargar este avatar: {jugador.avatar}")
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
            nombre_label = QLabel(f"{jugador.nombre}")
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
            dinero_label = QLabel(f"Son pobres")
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
            # Dinero:
            grupos_label = QLabel(f"No hay aun")
            grupos_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            grupos_label.setStyleSheet("""
                font-size: 14px;
                font-weight: bold;
                color: white;
                background-color: rgba(46, 21, 8, 0.7);
                padding: 5px;
                border-radius: 5px;
            """)
            texto_layout.addWidget(grupos_label)
            # Agregar el layout del texto al perfil:
            perfil_layout.addLayout(texto_layout)
            dinero_label.setFixedSize(100, 50)

            # Agregar el contenedor al layout del jugador:
            jugador_layout.addWidget(perfil_contenedor)
            
            # --- Propiedades ---
            propiedades_widget = QWidget(self)
            propiedades_widget.setLayout(propiedades_layout)
            propiedades_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            propiedades_layout.setSpacing(5)
            self.mostrar_cartas_en_cuadricula(propiedades_layout, jugador.get_propiedades(), "propiedad")
            jugador_layout.addWidget(propiedades_widget, 2)
            
            # --- Banco ---
            banco_widget = QWidget(self)
            banco_widget.setLayout(banco_layout)
            banco_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            propiedades_layout.setSpacing(5) 
            self.mostrar_cartas_en_cuadricula(banco_layout, jugador.get_banco(), "banco")
            jugador_layout.addWidget(banco_widget, 2)
            
            # Agregar el layout jugador al layout de la zona superior izquierda:
            self.zona_superior_izquierda_layout.addLayout(jugador_layout)
            
    def contar_propiedades(self, propiedades: dict):
        contador = 0
        for color, propiedad in propiedades.items():
            # Accedemos a la lista dentro del diccionario para este color
            lista_propiedades = propiedad["lista"]
            # Sumamos la cantidad de elementos en la lista
            contador += len(lista_propiedades)

        return contador
    
    def mostrar_cartas_en_cuadricula(self, grid_layout, cartas, tipo=None):
        
        """
        Rellena la cuadrícula indicada con las imágenes de las cartas que tiene
        y se asegura de que todas las celdas estén presentes, incluso si están vacías.
        """
        self.limpiar_layout(grid_layout)
        columnas = 9
        filas = 2
        total_celdas = filas * columnas
        if tipo == "propiedad":
            
            #cant_cartas = self.contar_propiedades(cartas)
            
            #print("Recorrido")
            listas = []
            for color,lista in cartas.items():
                        for cartas in lista["lista"]:
                            listas.extend(cartas["sublista"])
            cant_cartas = min(len(listas), total_celdas)
            for index in range(total_celdas):
                
                
                fila = index // columnas
                columna = index % columnas
                if index < cant_cartas :
                    print(f"Index: {index}")
                    print(f"Cartas: {cant_cartas}")
                    
                    # Si hay una carta en esta posición, muestra la carta:
                    
                    carta = listas[index]
                    carta_label = QLabel(self)
                    #carta_label.setFixedSize(25, 40)
                    carta_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                    carta_label.setScaledContents(True)
                    carta_label.setMinimumSize(35, 60)  # Puedes ajustar el tamaño mínimo según el diseño
                    carta_label.setMaximumSize(35, 65)
                    pixmap = QPixmap(carta.path_a_imagen)#.scaled(23, 40, Qt.AspectRatioMode.KeepAspectRatio)
                    #carta.mostrar_carta()
                    carta_label.setPixmap(pixmap)
                    grid_layout.addWidget(carta_label, fila, columna)
                else:
                    
                    # Si no hay carta, agrega un QLabel vacío como placeholder:
                    #print("Entro al else")
                    placeholder = QLabel(self)
                    placeholder.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                    placeholder.setScaledContents(True)
                    placeholder.setMinimumSize(35, 60)  # Puedes ajustar el tamaño mínimo según el diseño
                    placeholder.setMaximumSize(35, 65)
                    placeholder.setStyleSheet("background-color: transparent; border: 1px solid gray;")
                    grid_layout.addWidget(placeholder, fila, columna)
        else:
            
            for index in range(total_celdas):
                fila = index // columnas
                columna = index % columnas
                if index < len(cartas) :
                    # Si hay una carta en esta posición, muestra la carta:
                    carta = cartas[index]
                    carta_label = QLabel(self)
                    carta_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                    carta_label.setScaledContents(True)
                    carta_label.setMinimumSize(35, 60)  # Puedes ajustar el tamaño mínimo según el diseño
                    carta_label.setMaximumSize(35, 65)
                    pixmap = QPixmap(carta.path_a_imagen) #.scaled(23, 40, Qt.AspectRatioMode.KeepAspectRatio)
                    carta_label.setPixmap(pixmap)
                    grid_layout.addWidget(carta_label, fila, columna)
                else:
                    # Si no hay carta, agrega un QLabel vacío como placeholder:
                    placeholder = QLabel(self)
                    placeholder.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                    placeholder.setScaledContents(True)
                    placeholder.setMinimumSize(35, 60)  # Puedes ajustar el tamaño mínimo según el diseño
                    placeholder.setMaximumSize(35, 65)
                    placeholder.setStyleSheet("background-color: transparent; border: 1px solid gray;")
                    grid_layout.addWidget(placeholder, fila, columna)

    def mostrar_mano_jugador(self):
        """Muestra las cartas en la mano del jugador actual y actualiza la descripción."""
        
        # Limpiar el área de las cartas antes de agregar otras nuevas:
        while self.cartas_layout.count():
            widget = self.cartas_layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

        jugador_actual = self.__controlador.get_jugador_actual()
        cartas = jugador_actual.get_mano()
        
        imagen_vacia = self.path_proyecto / "imagenes/cartas/cartaVacia.png"
        imagen_vacia = imagen_vacia.as_posix()

        # Lógica para mostrar hasta 7 cartas:
        for i in range(7):      # <-- (No se va a exceder, pero igual tengo que usarlo).
            # Creación del widget de cada carta:
            carta_label = QLabel(self)
            
            # Esta disposición del código es perfecta, hace que al seleccionar una carta vacía no se actualice la imagen de descripció:
            if i < len(cartas):
                carta = cartas[i]
                carta_imagen = carta.path_a_imagen
                # Actualizar al clickear:
                carta_label.mousePressEvent = self.evento_click_carta(carta)
            else:
                carta_imagen = imagen_vacia
            pixmap = QPixmap(carta_imagen).scaled(100, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            carta_label.setPixmap(pixmap)
            carta_label.setFixedSize(100, 150)
            #carta_label.setStyleSheet("border: 1px solid black;") <-- Opcional

            # Agregar carta al layout:
            self.cartas_layout.addWidget(carta_label)

    def evento_click_carta(self, carta):
        """Actualizar la imagen de descripción al haber hecho click, por la imagen que se indica."""
        def evento(_):
            descripcion_imagen = carta.path_a_queHace
            if carta == self.carta_seleccionada:
                #print("Doble click detectado.")
                
                self.__controlador.jugar_carta(carta)
                
                
                self.carta_seleccionada = None
                self.update_interfaz()
            else:
                self.carta_seleccionada = carta # <-- Almacena primer click.
                
                if descripcion_imagen: # <-- En caso de que si tenga contenido descripcion_imagen.
                    pixmap_descripcion = QPixmap(descripcion_imagen).scaled(400, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    self.descripcion_carta_label.setPixmap(pixmap_descripcion)
                else:                  # <-- En caso de que sea Null porque no hay carta, usa la imagen vacía. (Igual ya no va a pasar)
                    pixmap_descripcion = QPixmap(self.path_queHaceVacio).scaled(400, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    self.descripcion_carta_label.setPixmap(pixmap_descripcion)
                #self.update_interfaz()    
                
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
            self.__controlador.terminar_turno()

    def finalizar_turno(self):
        """
        Finaliza el turno y pasa al siguiente jugador.
        Acá va la lógica que se maneja cuando finaliza el tiempo.
        """
        pro2 = self.__controlador.get_jugador_actual().get_propiedades
        self.turno_actual = (self.turno_actual + 1) % len(self.__controlador.get_jugadores())
        self.turno_label.setText(f"Turno de: {self.__controlador.get_jugador_actual().nombre}")
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
            for jugador in self.__controlador.get_jugadores():
                resumen += (
                    f"Jugador: {jugador['nombre']}\n"
                    f"Dinero final: $Son pobres\n"
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
            
            self.__controlador.volver_al_menu_principal()
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
