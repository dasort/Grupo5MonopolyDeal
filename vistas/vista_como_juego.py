from PyQt6.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QSpacerItem, QSizePolicy, QFrame, QMessageBox, QScrollArea, QGridLayout
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication

class ComoJuego(QDialog):
    def __init__(self, main_menu, parent=None):
        super().__init__(parent)
        self.main_menu = main_menu
        self.setWindowTitle("¿Cómo Juego?")
        self.setGeometry(340, 130, 900, 600)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))
        self.centrar_ventana()

        # ---
        
        # Main layout:
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)

        # Widgets:
        self.widget_arriba = QWidget()
        self.widget_abajo = QWidget()
        
        # Scroller:
        self.scroll_area_abajo = QScrollArea(self)
        self.scroll_area_abajo.setWidgetResizable(True)
        
        # Estilos de los widgets:
        #self.widget_arriba.setStyleSheet("""
        #    background-color: rgba(89, 45, 22, 1);
        #    border-bottom: 3px solid rgba(72, 26, 11, 1);
        #""")
        self.scroll_area_abajo.setObjectName("scrollerAbajo") # <-- Así lo de adentro no hereda el diseño.
        self.scroll_area_abajo.setStyleSheet("""
            #scrollerAbajo {
                border: 2px solid #444;
                border-radius: 5px;
                background-color: #222;
                font-size: 18px;
                text-align: left;
                padding: 5px;
            }
        """)
        #self.widget_abajo.setFixedHeight(500)
        
        # Layouts (Les paso los Widgets):
        self.layout_arriba = QVBoxLayout(self.widget_arriba)
        self.layout_arriba.setContentsMargins(0, 0, 0, 0)
        self.layout_arriba.setSpacing(0)
        
        self.layout_arriba_arriba = QHBoxLayout()
        self.layout_arriba_arriba.setContentsMargins(10, 10, 0, 0)
        self.layout_arriba_arriba.setSpacing(0)
        self.layout_arriba_arriba.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        
        self.layout_arriba_abajo = QHBoxLayout()
        self.layout_arriba_abajo.setContentsMargins(20, 10, 20, 10)
        self.layout_arriba_abajo.setSpacing(12)
        self.layout_arriba_abajo.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        
        self.layout_abajo = QVBoxLayout(self.widget_abajo)
        self.layout_abajo.setContentsMargins(10, 10, 10, 10)
        self.layout_abajo.setSpacing(5)
        self.layout_abajo.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # El layout_abajo cambia dinámicamente según que botón se seleccione.
        self.mostrar_reglas_generales() # <-- Acá me aseguro que empiece con la de Reglas Generales como predeterminado.
        
        # ---
        
        # Volver:
        self.boton_volver = self.crear_boton_volver("Volver", "imagenes/ui/home.png")
        self.boton_volver.clicked.connect(self.volver)
        self.layout_arriba_arriba.addWidget(self.boton_volver)
        
        # ---
        
        # Botón "Reglas Generales":
        self.boton_reglas_generales = self.crear_boton("Reglas Generales", "imagenes/ui/book_question.png")
        self.boton_reglas_generales.clicked.connect(self.mostrar_reglas_generales)
        self.layout_arriba_abajo.addWidget(self.boton_reglas_generales)
        
        # Botón "Ver las Cartas":
        self.boton_ver_cartas = self.crear_boton("Ver las Cartas", "imagenes/ui/blogs_stack.png")
        self.boton_ver_cartas.clicked.connect(self.mostrar_ver_cartas)
        self.layout_arriba_abajo.addWidget(self.boton_ver_cartas)
        
        # Botón "A cerca de la Interfaz":
        self.boton_a_cerca_interfaz = self.crear_boton("A cerca de la Interfaz", "imagenes/ui/checkerboard.png")
        self.boton_a_cerca_interfaz.clicked.connect(self.mostrar_a_cerca_interfaz)
        self.layout_arriba_abajo.addWidget(self.boton_a_cerca_interfaz)

        # ---
        
        # Lo de arriba:
        self.layout_arriba.addLayout(self.layout_arriba_arriba)
        self.layout_arriba.addLayout(self.layout_arriba_abajo)
        self.main_layout.addWidget(self.widget_arriba)
        
        # Lo de abajo:
        self.scroll_area_abajo.setWidget(self.widget_abajo)
        self.main_layout.addWidget(self.scroll_area_abajo) # <-- Lo dinámico es lo que va adentro, sirve para darle estilo.
    
    def crear_boton(self, texto, icono_ruta):
        """Crea un botón que tiene un ícono (a la izquierda) y texto."""
        boton = QPushButton(self) # <-- Este es el contenedor principal.
        boton.setStyleSheet("""
            QPushButton {
                border: 2px solid #444;
                border-radius: 5px;
                background-color: #222; /* <-- Es perfecto no cambiar */
                font-size: 18px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #333; /* <-- Tampoco */
            }
        """)
        boton.setFixedHeight(50)
        boton.setFixedWidth(250)

        # Layout del ícono y el texto:
        layout = QHBoxLayout(boton)

        # Ícono
        icono_label = QLabel(self)
        pixmap = QPixmap(icono_ruta).scaled(20, 20) # <-- Tamaño de la imagen.
        icono_label.setPixmap(pixmap)
        icono_label.setFixedSize(20, 20)            # <-- Tamaño fijo del contenedor del ícono.
        layout.addWidget(icono_label)

        # Texto
        texto_label = QLabel(texto, self)
        texto_label.setStyleSheet("""
            padding-left: 5px;
            font-size: 18px;
        """)
        layout.addWidget(texto_label)

        return boton
    
    def crear_boton_volver(self, texto, icono_ruta):
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

        # Ícono
        icono_label = QLabel(self)
        pixmap = QPixmap(icono_ruta).scaled(15, 15) # <-- Tamaño de la imagen.
        icono_label.setPixmap(pixmap)
        icono_label.setFixedSize(15, 15)            # <-- Tamaño fijo del contenedor del ícono.
        layout.addWidget(icono_label)

        # Texto
        texto_label = QLabel(texto, self)
        texto_label.setStyleSheet("""
            padding-left: 5px;
            font-size: 16px;
        """)
        layout.addWidget(texto_label)

        return boton
    
    def limpiar_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater() # <-- Borrar el Widget.
            elif item.layout():
                self.limpiar_layout(item.layout()) # <-- (En caso de que hayan Widgets anidados).
    
    def mostrar_reglas_generales(self):
        self.limpiar_layout(self.layout_abajo)
        
        linea1 = QLabel("¡Bienvenido a Monopoly Deal de Escritorio!")
        linea1.setStyleSheet("""
            padding-left: 5px;
            font-size: 22px;
        """)
        
        linea2 = QLabel("En este tutorial aprenderás como jugar y ganar.")
        
        separador1 = QFrame(self)
        separador1.setFrameShape(QFrame.Shape.HLine)
        separador1.setFrameShadow(QFrame.Shadow.Sunken)
        
        linea3 = QLabel("1. Mazo:")
        linea3.setStyleSheet("""
            color: #74F1FF;
            font-size: 18px;
        """)
        
        linea4 = QLabel("Cada jugador comienza la partida con <u>5 cartas aleatorias</u> en su mazo, el mazo puede tener un máximo de 7 cartas.")
        linea5 = QLabel("Cuando sea tu turno <u>agarrá cartas</u> y agregalas a tu mazo:")
        linea6 = QLabel("  -  Caso 1: Agarrá 2 cartas.")
        linea7 = QLabel("  -  Caso 2: No tenés cartas en tu mazo, entonces agarrá 5 en vez de 2.")
        linea8 = QLabel("Cuando sea tu turno <u>podés jugar cartas</u>, te recomendamos este órden:")
        linea9 = QLabel("  -  A. Cartas de Dinero.")
        linea10 = QLabel("  -  B. Cartas de Propiedad.")
        linea11 = QLabel("  -  C. Cartas de Acción (<-- Solo podés jugar 1 carta de acción por turno).")
        
        separador2 = QFrame(self)
        separador2.setFrameShape(QFrame.Shape.HLine)
        separador2.setFrameShadow(QFrame.Shadow.Sunken)
        
        linea12 = QLabel("2. Finalizá tu Turno:")
        linea12.setStyleSheet("""
            color: #E1A3FF;
            font-size: 18px;
        """)
        
        linea13 = QLabel("Una vez termines tus movimientos pasá el turno para que otro juegue.")
        linea14 = QLabel("Si el tiempo supera los 60s se cambiará solo el turno, así que... <b>¡Apurate!</b>")
        
        separador3 = QFrame(self)
        separador3.setFrameShape(QFrame.Shape.HLine)
        separador3.setFrameShadow(QFrame.Shadow.Sunken)
        
        linea15 = QLabel("3. Ganá la Partida:")
        linea15.setStyleSheet("""
            color: #8BFF77;
            font-size: 18px;
        """)
        
        linea16 = QLabel("El jugador que gana la partida es quien consigue <u>3 sets completos de propiedades</u>.")
        linea17 = QLabel("Hay <u>distintos tipos de propiedades</u>, rojas, azules, de ferrocarríl, etc.")
        linea18 = QLabel("Cada tipo de propiedad requiere <u>juntar una cierta cantidad del mismo tipo</u>, esto varía.")
        linea19 = QLabel("Ejemplos:")
        linea20 = QLabel("  -  a. Set de propiedades azul completo requiere <b>2 del mismo tipo</b>.")
        linea21 = QLabel("  -  b. Set de propiedades verde completo requiere <b>3 del mismo tipo</b>.")
        linea22 = QLabel("  -  c. Set de propiedades de ferrocarríl (negro) completo requiere <b>4 del mismo tipo</b>.")
        
        separador4 = QFrame(self)
        separador4.setFrameShape(QFrame.Shape.HLine)
        separador4.setFrameShadow(QFrame.Shadow.Sunken)
        
        linea23 = QLabel("4. ¡No Dejés que te Ganen!:")
        linea23.setStyleSheet("""
            color: #FF4B4B;
            font-size: 18px;
        """)
        
        linea24 = QLabel("Jugá cartas de acción contra otros jugadores estratégicamente <u>para evitar que te ganen</u>.")
        linea25 = QLabel("Hay 8 cartas distintas de acción, te permitirán hacerles la vida imposible a los demás.")
        linea26 = QLabel("Robales, intercambiales propiedades, quitales sets completos, hacé que te paguen, y otras cosas más!")
        linea27 = QLabel("Ahora es el momento de ir al apartado de <Ver las Cartas>, ahí vas a ver cuales usar, cómo usarlas y que hacen.")
        
        # ---
        
        self.layout_abajo.addWidget(linea1)
        self.layout_abajo.addSpacing(8)
        self.layout_abajo.addWidget(linea2)
        self.layout_abajo.addSpacing(15)
        self.layout_abajo.addWidget(separador1)
        self.layout_abajo.addWidget(linea3)
        self.layout_abajo.addWidget(linea4)
        self.layout_abajo.addWidget(linea5)
        self.layout_abajo.addWidget(linea6)
        self.layout_abajo.addWidget(linea7)
        self.layout_abajo.addWidget(linea8)
        self.layout_abajo.addWidget(linea9)
        self.layout_abajo.addWidget(linea10)
        self.layout_abajo.addWidget(linea11)
        self.layout_abajo.addSpacing(15)
        self.layout_abajo.addWidget(separador2)
        self.layout_abajo.addWidget(linea12)
        self.layout_abajo.addWidget(linea13)
        self.layout_abajo.addWidget(linea14)
        self.layout_abajo.addSpacing(15)
        self.layout_abajo.addWidget(separador3)
        self.layout_abajo.addWidget(linea15)
        self.layout_abajo.addWidget(linea16)
        self.layout_abajo.addWidget(linea17)
        self.layout_abajo.addWidget(linea18)
        self.layout_abajo.addWidget(linea19)
        self.layout_abajo.addWidget(linea20)
        self.layout_abajo.addWidget(linea21)
        self.layout_abajo.addWidget(linea22)
        self.layout_abajo.addSpacing(15)
        self.layout_abajo.addWidget(separador4)
        self.layout_abajo.addWidget(linea23)
        self.layout_abajo.addWidget(linea24)
        self.layout_abajo.addWidget(linea25)
        self.layout_abajo.addWidget(linea26)
        self.layout_abajo.addWidget(linea27)
        
    def mostrar_ver_cartas(self):
        self.limpiar_layout(self.layout_abajo)
        
        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(10, 10, 10, 10)
        grid_layout.setSpacing(15)

        cartas = [
            {"ruta": "imagenes/cartas/dinero1.png", "descripcion": "Carta de Dinero: Sirve para pagar deudas, vale 1 millón."},
            {"ruta": "imagenes/cartas/dinero2.png", "descripcion": "Carta de Dinero: Sirve para pagar deudas, vale 2 millones."},
            {"ruta": "imagenes/cartas/dinero3.png", "descripcion": "Carta de Dinero: Sirve para pagar deudas, vale 3 millones."},
            {"ruta": "imagenes/cartas/dinero4.png", "descripcion": "Carta de Dinero: Sirve para pagar deudas, vale 4 millones."},
            {"ruta": "imagenes/cartas/dinero5.png", "descripcion": "Carta de Dinero: Sirve para pagar deudas, vale 5 millones."},
            {"ruta": "imagenes/cartas/dinero10.png", "descripcion": "Carta de Dinero: Sirve para pagar deudas, vale 10 millones."},
            {"ruta": "imagenes/cartas/propiedadAmarillo.png", "descripcion": "Carta de Propiedad: Coleccioná 3 para crear un set completo."},
            {"ruta": "imagenes/cartas/propiedadAzul.png", "descripcion": "Carta de Propiedad: Coleccioná 2 para crear un set completo."},
            {"ruta": "imagenes/cartas/propiedadCeleste.png", "descripcion": "Carta de Propiedad: Coleccioná 3 para crear un set completo."},
            {"ruta": "imagenes/cartas/propiedadFerrocarril.png", "descripcion": "Carta de Propiedad: Coleccioná 4 para crear un set completo."},
            {"ruta": "imagenes/cartas/propiedadMarron.png", "descripcion": "Carta de Propiedad: Coleccioná 2 para crear un set completo."},
            {"ruta": "imagenes/cartas/propiedadNaranja.png", "descripcion": "Carta de Propiedad: Coleccioná 3 para crear un set completo."},
            {"ruta": "imagenes/cartas/propiedadRojo.png", "descripcion": "Carta de Propiedad: Coleccioná 3 para crear un set completo."},
            {"ruta": "imagenes/cartas/propiedadRosa.png", "descripcion": "Carta de Propiedad: Coleccioná 3 para crear un set completo."},
            {"ruta": "imagenes/cartas/propiedadServicio1.png", "descripcion": "Carta de Propiedad: Coleccioná 2 para crear un set completo."},
            {"ruta": "imagenes/cartas/propiedadServicio2.png", "descripcion": "Carta de Propiedad: Coleccioná 2 para crear un set completo."},
            {"ruta": "imagenes/cartas/propiedadVerde.png", "descripcion": "Carta de Propiedad: Coleccioná 3 para crear un set completo."},
            {"ruta": "imagenes/cartas/comodinAmarilloRojo.png", "descripcion": "Carta Comodín: Vale para los dos tipos (Amarillo y Rojo), elegí el que necesites."},
            {"ruta": "imagenes/cartas/comodinAzulVerde.png", "descripcion": "Carta Comodín: Vale para los dos tipos (Azul y Verde), elegí el que necesites."},
            {"ruta": "imagenes/cartas/comodinCelesteFerrocarril.png", "descripcion": "Carta Comodín: Vale para los dos tipos (Celeste y Ferrocarríl), elegí el que necesites."},
            {"ruta": "imagenes/cartas/comodinCelesteMarron.png", "descripcion": "Carta Comodín: Vale para los dos tipos (Celeste y Marrón), elegí el que necesites."},
            {"ruta": "imagenes/cartas/comodinNaranjaRosa.png", "descripcion": "Carta Comodín: Vale para los dos tipos (Naranja y Rosa), elegí el que necesites."},
            {"ruta": "imagenes/cartas/comodinServicioFerrocarril.png", "descripcion": "Carta Comodín: Vale para los dos tipos (Servicio y Ferrocarril), elegí el que necesites."},
            {"ruta": "imagenes/cartas/comodinVerdeFerrocarril.png", "descripcion": "Carta Comodín: Vale para los dos tipos (Verde y Ferrocarril), elegí el que necesites."},
            {"ruta": "imagenes/cartas/comodinMulticolor.png", "descripcion": "Carta Comodín: Vale para cualquier tipo!, elegí el que necesites."},
            {"ruta": "imagenes/cartas/alquilerFerrocarrilServicio.png", "descripcion": "Carta Alquiler: Todos te pagan por ambos colores!"},
            {"ruta": "imagenes/cartas/alquilerMarronCeleste.png", "descripcion": "Carta Alquiler: Todos te pagan por ambos colores!"},
            {"ruta": "imagenes/cartas/alquilerRojoAmarillo.png", "descripcion": "Carta Alquiler: Todos te pagan por ambos colores!"},
            {"ruta": "imagenes/cartas/alquilerRosaNaranja.png", "descripcion": "Carta Alquiler: Todos te pagan por ambos colores!"},
            {"ruta": "imagenes/cartas/alquilerVerdeAzul.png", "descripcion": "Carta Alquiler: Todos te pagan por ambos colores!"},
            {"ruta": "imagenes/cartas/alquilerMulticolor.png", "descripcion": "Carta Alquiler: Elige a un jugador que te pague por un tipo de propiedad específica que quieras!"},
            {"ruta": "imagenes/cartas/alquilerFerrocarrilServicio.png", "descripcion": "Carta Alquiler: Todos te pagan por ambos colores!"},
            {"ruta": "imagenes/cartas/alquilerDoble.png", "descripcion": "Carta de Acción: Jugá esta carta y otra de alquiler para que el alquiler de esa carta sea el doble de costosa."},
            {"ruta": "imagenes/cartas/cobradorDeDeudas.png", "descripcion": "Carta de Acción: El jugador que elijas te va a tener que pagar 5 millones."},
            {"ruta": "imagenes/cartas/esMiCumpleanos.png", "descripcion": "Carta de Acción: Todos los jugadores te tienen que pagar como 'regalo' 2 millones... ¡Feliz cumpleaños!"},
            {"ruta": "imagenes/cartas/negocioFurtivo.png", "descripcion": "Carta de Acción: Sacale la propiedad que quieras a otro jugador (No puede ser de un set completo)."},
            {"ruta": "imagenes/cartas/pasaPorLaSalida.png", "descripcion": "Carta de Acción: Podés agarrar 2 cartas más."},
            {"ruta": "imagenes/cartas/robaNegocios.png", "descripcion": "Carta de Acción: Sacale un set completo a otro jugador!"},
            {"ruta": "imagenes/cartas/tratoForzoso.png", "descripcion": "Carta de Acción: Intercambiá una propiedad tuya con la de otro jugador (No puede ser de un set completo)."}
        ]

        columnas = 5
        fila = 0
        columna = 0

        # Botones para cada carta:
        for carta in cartas:
            boton_carta = QPushButton(self)
            boton_carta.setFixedSize(150, 235)

            pixmap = QPixmap(carta["ruta"]).scaled(150, 235, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            boton_carta.setIcon(QIcon(pixmap))
            boton_carta.setIconSize(pixmap.size()) # <-- Tamaño del ícono.
            boton_carta.setStyleSheet("""
                QPushButton {
                    border: 5px solid #555;
                    border-radius: 5px;
                    background-color: #333;
                }
                QPushButton:hover {
                    border: 5px solid #FFFFFF;
                }
            """)
            
            boton_carta.clicked.connect(lambda checked, descripcion=carta["descripcion"]: self.mostrar_info_carta(descripcion))

            # Agregarlo al boton a la cuadrícula:
            grid_layout.addWidget(boton_carta, fila, columna)

            # Avanzar:
            columna += 1
            if columna >= columnas:
                columna = 0
                fila += 1

        # Widget contenedor para el layout:
        widget_cartas = QWidget()
        widget_cartas.setLayout(grid_layout)

        # Agregarlo:
        self.layout_abajo.addWidget(widget_cartas)
    
    def mostrar_info_carta(self, descripcion):
        QMessageBox.information(self, "Información de la Carta", descripcion)
        
    def mostrar_a_cerca_interfaz(self):
        self.limpiar_layout(self.layout_abajo)

        pixmap = QPixmap("imagenes/ui/interfaz.png").scaled(880, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        label_imagen = QLabel()
        label_imagen.setPixmap(pixmap)
        label_imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)

        linea1 = QLabel("Interfaz General:")
        linea1.setStyleSheet("""
            color: #E1A3FF;
            font-size: 18px;
        """)
        linea2 = QLabel("1. Acá se ven todas las cartas de los jugadores, es esencial tenerlas todas a la vista.")
        linea3 = QLabel("2. Acá se ven tus cartas en grande, para que no tengas que estar acercándote a la pantalla.")
        linea4 = QLabel("3. Al tocar 1 vez la carta se muestra una explicación sobre que hace.")
        linea5 = QLabel("4. Este es tu mazo de cartas, tienes un máximo de 7.")
        linea6 = QLabel("5. Turno del jugador actual.")
        linea7 = QLabel("6. Tiempo restante del turno, el máximo para cada jugador son siempre 60 segundos.")
        linea8 = QLabel("7. Finaliza tu turno manualmente para que otro jugador juegue.")
        linea9 = QLabel("8. Finaliza la partida para todos cuando quieras (que no sea por enojo).")
        
        separador = QFrame(self)
        separador.setFrameShape(QFrame.Shape.HLine)
        separador.setFrameShadow(QFrame.Shadow.Sunken)
        
        linea10 = QLabel("Sección Jugadores:")
        linea10.setStyleSheet("""
            color: #E1A3FF;
            font-size: 18px;
        """)
        linea11 = QLabel("A. Cada jugador tiene su ícono correspondiente que eligió al crear la partida.")
        linea12 = QLabel("B. Acá se muestra el nickname de cada jugador, si inició sesión se mostraría ese.")
        linea13 = QLabel("C. Acá se muestra el dinero de cada jugador, se calcula según las cartas del banco.")
        linea14 = QLabel("D. Acá se muestran las cartas de propiedad de dicho jugador.")
        linea15 = QLabel("E. Acá se muestran las cartas del banco de dicho jugador.")

        # ---

        self.layout_abajo.addWidget(label_imagen)
        self.layout_abajo.addWidget(linea1)
        self.layout_abajo.addWidget(linea2)
        self.layout_abajo.addWidget(linea3)
        self.layout_abajo.addWidget(linea4)
        self.layout_abajo.addWidget(linea5)
        self.layout_abajo.addWidget(linea6)
        self.layout_abajo.addWidget(linea7)
        self.layout_abajo.addWidget(linea8)
        self.layout_abajo.addWidget(linea9)
        self.layout_abajo.addSpacing(15)
        self.layout_abajo.addWidget(separador)
        self.layout_abajo.addWidget(linea10)
        self.layout_abajo.addWidget(linea11)
        self.layout_abajo.addWidget(linea12)
        self.layout_abajo.addWidget(linea13)
        self.layout_abajo.addWidget(linea14)
        self.layout_abajo.addWidget(linea15)

    def volver(self):
        self.hide()
    
    def centrar_ventana(self):
        forma_pantalla = QGuiApplication.primaryScreen().availableGeometry()
        forma_ventana = self.frameGeometry()
        centro_pantalla = forma_pantalla.center()
        forma_ventana.moveCenter(centro_pantalla)
        self.move(forma_ventana.topLeft())