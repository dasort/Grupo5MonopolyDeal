from PyQt6.QtWidgets import QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QGridLayout, QMessageBox, QSizePolicy, QSpacerItem
from PyQt6.QtGui import QIcon, QPixmap, QIntValidator 
from PyQt6.QtCore import Qt
from tablero_pantalla import Tablero

class CrearPartida(QDialog):
    def __init__(self, main_menu, parent=None):
        super().__init__(parent)
        self.main_menu = main_menu # <-- Una referencia a MainMenu.
        self.setWindowTitle("Crear Partida")
        self.setGeometry(370, 185, 875, 517)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))
        
        self.adjustSize()
        self.setMinimumSize(875, 500)

        self.minimo_jugadores = 2
        self.maximo_jugadores = 5
        self.dinero_inicial = 0 # <-- Temporal, debería ser random.
        self.jugadores = []

        # ---
        
        # Main layout:
        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)  # Sin espacios
        self.setLayout(self.main_layout)

        # Layout derecha:
        self.layout_derecha = QVBoxLayout()
        self.layout_derecha.setContentsMargins(0, 0, 0, 0)
        self.layout_derecha.setSpacing(0)

        # Widgets:
        self.widget_izquierda = QWidget()
        self.widget_derecha_arriba = QWidget()
        self.widget_derecha_abajo = QWidget()

        # Colores de Widgets y bordes ajustados:
        self.widget_izquierda.setStyleSheet("""
            /* background-color: rgba(127, 127, 127, 1); */
            background-color: rgba(89, 45, 22, 1);
            border-right: 4px solid rgba(72, 26, 11, 1);
        """)
        self.widget_derecha_arriba.setStyleSheet("""
            /* background-color: rgba(255, 201, 14, 1); */
            background-color: rgba(196, 114, 48, 1);
            border-bottom: 4px solid rgba(72, 26, 11, 1);
        """)
        self.widget_derecha_abajo.setStyleSheet("""
            /* background-color: rgba(148, 114, 84, 1); */
            background-color: rgba(209, 154, 101, 1);
            border-top: 0; /* <-- No debe tener borde arriba (con no poner esto es lo mismo). */
        """)
        
        # Configurar políticas de tamaño:
        self.widget_derecha_arriba.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.widget_derecha_abajo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        # Layouts internos (Están adentro de los widgets):
        self.layout_izquierda = QVBoxLayout(self.widget_izquierda)
        self.layout_izquierda.setContentsMargins(8, 8, 12, 8) # <-- Márgenes de adentro.
        self.layout_izquierda.setSpacing(8)                   # <-- Entre botones.

        self.layout_derecha_arriba = QHBoxLayout(self.widget_derecha_arriba)
        self.layout_derecha_arriba.setContentsMargins(20, 10, 20, 12) # <-- Márgenes internos del contenedor
        self.layout_derecha_arriba.setSpacing(12)                     # <-- Espaciado entre el avatar y el texto

        self.layout_derecha_abajo = QVBoxLayout(self.widget_derecha_abajo)
        self.layout_derecha_abajo.setContentsMargins(5, 5, 5, 5)
        self.layout_derecha_abajo.setSpacing(10)

        # Cargar iconos inicialmente:
        self.cargar_iconos()
        
        # ---
        
        # Cuadrícula "Agregar Jugador":
        self.jugadores_layout = QVBoxLayout()
        self.jugadores_layout.setSpacing(5)
        self.layout_derecha_abajo.addLayout(self.jugadores_layout)
        
        self.layout_derecha_abajo.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # ---
        
        # Botón "Agregar Jugador":
        self.agregar_jugador_boton = QPushButton("Agregar Jugador", self)
        self.agregar_jugador_boton.setStyleSheet("""
            QPushButton {
                background-color: #25B31D; /*#479C36;*/
                color: white;
                padding: 6px;
                font-size: 20px;
                outline: none;
                border: 3px solid #9AF593;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #4FD947; /*#7FD46E;*/
                outline: none;
            }
            QPushButton:disabled {
                background-color: #208521;
                color: #B5B5B5;
                border: 3px solid #59B358;
            }
        """)
        self.agregar_jugador_boton.setFixedSize(230, 60)
        self.agregar_jugador_boton.clicked.connect(self.agregar_jugador)
        self.layout_izquierda.addWidget(self.agregar_jugador_boton)
        
        # ---

        # Botón "Quitar Jugador":
        self.quitar_jugador_boton = QPushButton("Quitar Jugador", self)
        self.quitar_jugador_boton.setStyleSheet("""
            QPushButton {
                background-color: #E64444; /*#D96372;*/
                color: white;
                padding: 6px;
                font-size: 20px;
                outline: none;
                border: 3px solid #F79090;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #F06262; /*#FFAAAA;*/
            }
            QPushButton:disabled {
                background-color: #B53636;
                color: #949494;
                border: 3px solid #BF6666;
            }
        """)
        self.quitar_jugador_boton.setFixedSize(230, 60)
        self.quitar_jugador_boton.setEnabled(False)
        self.quitar_jugador_boton.clicked.connect(self.quitar_jugador)
        self.layout_izquierda.addWidget(self.quitar_jugador_boton)

        # ---
        
        # css (qss) para el <br>:
        texto_en_qss = (
                "(Opcional): Inicia sesión para<br>"
                "guardar tus estadísticas."
            )
        self.aclaracion_label = QLabel(texto_en_qss)
        self.aclaracion_label.setStyleSheet("""
            /* color: black; */
            color: #FFC592;
            border-right: 0; /* <-- Soluciona problemas de herencha. */
            font-size: 18px;
            /*padding-left: 10px;*/
            /*padding-right: 10px;*/
        """)
        self.layout_izquierda.addWidget(self.aclaracion_label)
        
        self.layout_izquierda.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        
        # ---

        # css (qss) para el <br>:
        self.aviso_qcc = (
                "(Agrega 2 o más jugadores<br>"
                "para crear una partida)."
            )
        self.aviso_label = QLabel(self.aviso_qcc)
        self.aviso_label.setStyleSheet("""
            color: #D47034;
            border-right: 0; /* <-- Soluciona problemas de herencha. */
            font-size: 18px;
            padding-top: 4px;
            padding-bottom: 4px;
            background-color: #78391D;
            outline: none;
            border: 2px solid #914A27;
            border-radius: 5px;
        """)
        self.layout_izquierda.addWidget(self.aviso_label)
        
        # Botón "Crear Partida":
        self.crear_partida_boton = QPushButton("Crear Partida", self)
        self.crear_partida_boton.setStyleSheet("""
            QPushButton {
                background-color: #80452B;
                padding: 6px;
                font-size: 20px;
                outline: none;
                border: 3px solid #C77750;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #A16043;
            }
            QPushButton:disabled {
                background-color: #693A24;
                color: #949494;
                border: 3px solid #8A5135;
            }
        """)
        self.crear_partida_boton.setFixedSize(230, 60)
        self.crear_partida_boton.setEnabled(False) # <-- Para evitar que se pueda crear una partida sin jugadores.
        self.crear_partida_boton.clicked.connect(self.crear_partida)
        self.layout_izquierda.addWidget(self.crear_partida_boton)

        # ---

        # Botón "Volver al Menú Principal":
        self.boton_volver = QPushButton("Volver al Menú Principal", self)
        self.boton_volver.setStyleSheet("""
            QPushButton {
                background-color: #80452B;
                padding: 6px;
                font-size: 20px;
                outline: none;
                border: 3px solid #C77750;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #A16043;
            }
        """)
        self.boton_volver.setFixedSize(230, 60)
        self.boton_volver.clicked.connect(self.volver)
        self.layout_izquierda.addWidget(self.boton_volver)

        # Agregar widgets al layout principal:
        self.main_layout.addWidget(self.widget_izquierda)
        self.layout_derecha.addWidget(self.widget_derecha_arriba)
        self.layout_derecha.addWidget(self.widget_derecha_abajo)
        self.main_layout.addLayout(self.layout_derecha)














    def volver(self):
        self.hide()
        self.main_menu.show()
        
    def cargar_iconos(self):
        # Limpiar el área de los iconos antes de agregar otros nuevos:
        while self.layout_derecha_arriba.count():
            widget = self.layout_derecha_arriba.takeAt(0).widget()
            if widget:
                widget.deleteLater()

        avatar_vacio = "imagenes/ui/perfilRecortadoVacio.png"

        # Lógica para mostrar hasta 5 iconos:
        for i in range(5):
            # Creación del widget de cada icono:
            avatar_label = QLabel(self)
            avatar_label.setStyleSheet("""
                border-bottom: 0; /* <-- Soluciona un problema de herencia. */
            """)
            
            if i < len(self.jugadores):
                avatar = self.jugadores[i]["avatar"].currentData()
            else:
                avatar = avatar_vacio
            pixmap = QPixmap(avatar).scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            avatar_label.setPixmap(pixmap)
            avatar_label.setFixedSize(100, 100)
            #avatar_label.setStyleSheet("border: 1px solid black;") <-- Opcional

            # Agregar carta al layout:
            self.layout_derecha_arriba.addWidget(avatar_label)
        
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
                    self.crear_partida_boton.setEnabled(True) # <-- Si o si.
                    self.aviso_label.hide()
            
            # Manejo lo que pasa si no tiene lo necesario:
            else:
                
                if len(self.jugadores) == 2:
                    self.crear_partida_boton.setEnabled(True)
                
                # Igual a 1 jugador:
                if len(self.jugadores) == 1:
                    self.quitar_jugador_boton.setEnabled(True)
                    self.crear_partida_boton.setEnabled(False)
                    self.aviso_label.show()
                
                # 0 jugadores:
                else:
                    self.quitar_jugador_boton.setEnabled(False)
        
        except Exception:
            print("Lista de jugadores vacía!")

    def agregar_jugador(self):
        jugador_row = len(self.jugadores)
        
        # Widget jugador (completo):
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
        
        # Layout jugador (completo):
        layout_jugador = QVBoxLayout(widget_jugador)
        layout_jugador.setContentsMargins(0, 0, 0, 0)
        layout_jugador.setSpacing(0)
        
        # Layout jugador (info):
        info_jugador_layout = QGridLayout()
        info_jugador_layout.setContentsMargins(0, 0, 5, 0)
        
        # ---
        
        # El texto del tooltip con CSS (para el <br>):
        tooltip_text = (
            "1. Puede iniciar sesión y aparecerá con su nombre de cuenta.<br>"
            "2. Si no inicia sesión puede ingresar el nombre que quiera.<br>"
            "3. Si no ingresa nombre aparecerá como anónimo."
        )
        
        # Nombre Label:
        nombre_label = QLabel(f"Jugador {jugador_row + 1}:")
        nombre_label.setToolTip(tooltip_text)
        nombre_label.setStyleSheet("""
            background-color: #78391D;
        """)
        
        # Nombre Insertar texto:
        nombre_input = QLineEdit()
        nombre_input.setPlaceholderText("Nombre")
        nombre_input.setToolTip(tooltip_text)
        nombre_input.setStyleSheet("""
            background-color: #78391D;
        """)
        nombre_input.setFixedWidth(200)
        
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
        avatar_combo.setStyleSheet("""
            background-color: #78391D;
            padding-left: 5px;
        """)
        
        # Selección Iniciar sesión Label:
        sesion_label = QLabel("Iniciar sesión:")
        sesion_label.setToolTip(tooltip_text)
        
        # Iniciar sesión botón:
        boton_cuenta = QPushButton("Inicie", self)
        boton_cuenta.clicked.connect(self.volver) # <-- Cambiar
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

        # Añadir al layout:
        layout_jugador.addWidget(nombre_label)
        layout_jugador.addLayout(info_jugador_layout)
        
        info_jugador_layout.addWidget(nombre_input, 0, 0)
        info_jugador_layout.addWidget(avatar_label, 0, 1)
        info_jugador_layout.addWidget(avatar_combo, 0, 2)
        info_jugador_layout.addWidget(sesion_label, 0, 3)
        info_jugador_layout.addWidget(boton_cuenta, 0, 4)
        
        self.jugadores_layout.addWidget(widget_jugador)
        
        # Para que se actualice al cambiar alguno:
        avatar_combo.currentIndexChanged.connect(self.cargar_iconos)

        # Almacenar referencias de los widgets:
        # (Almaceno una referencia de los widgets de cada uno para que se puedan borrar).
        self.jugadores.append({
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

        # Asegurarme que los botones se activen o desactiven cuando deban:
        self.cambio_cant_jugadores() # <-- Es clave que esto se ejecute al final de cuando se agrega el jugador.
        self.cargar_iconos()
    
    def quitar_jugador(self):
        if self.jugadores:
            # Saca el último jugador que se agregó:
            jugador = self.jugadores.pop()

            # Elimino los widgets asociados a ese jugador:
            jugador["widget_jugador"].deleteLater()
            jugador["layout_jugador"].deleteLater()
            jugador["info_jugador_layout"].deleteLater()
            jugador["nombre_label"].deleteLater()
            jugador["nombre_input"].deleteLater()
            jugador["avatar_label"].deleteLater()
            jugador["avatar_combo"].deleteLater()
            jugador["sesion_label"].deleteLater()
            jugador["boton_cuenta"].deleteLater()

            # Habilito el botón de agregar si es que estaba deshabilitado:
            self.cambio_cant_jugadores()
            self.cargar_iconos()

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