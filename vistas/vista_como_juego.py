from PyQt6.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from controladores.controlador_como_juego import controlador_como_juego
class ComoJuego(QDialog):
    def __init__(self, main_menu, parent=None):
        super().__init__(parent)
        self.main_menu = main_menu
        self.setWindowTitle("¿Cómo Juego?")
        self.setGeometry(340, 130, 900, 600)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))

        # Controlador de como juego:
        self.controlador_juego=controlador_como_juego(self)
        
        # Main layout:
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)

        # Widgets:
        self.widget_arriba = QWidget()
        #self.widget_abajo = QWidget()
        
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
        
        # El layout_abajo cambia dinámicamente según que botón se seleccione.
        self.controlador_juego.mostrar_reglas_generales() # <-- Acá me aseguro que empiece con la de Reglas Generales como predeterminado.
        
        # ---
        
        # Volver:
        self.boton_volver = self.crear_boton_volver("Volver", "imagenes/ui/casa.png")
        self.boton_volver.clicked.connect(self.controlador_juego.volver)
        tooltip_volver = ("Volvé al Menú Principal.")
        self.boton_volver.setToolTip(tooltip_volver)
        self.layout_arriba_arriba.addWidget(self.boton_volver)
        
        # ---
        
        # Botón "Reglas Generales":
        self.boton_reglas_generales = self.crear_boton("Reglas Generales", "imagenes/ui/libro.png")
        self.boton_reglas_generales.clicked.connect(self.controlador_juego.mostrar_reglas_generales)
        tooltip_reglas = ("Ver las Reglas Generales.")
        self.boton_reglas_generales.setToolTip(tooltip_reglas)
        self.layout_arriba_abajo.addWidget(self.boton_reglas_generales)
        
        # Botón "Ver las Cartas":
        self.boton_ver_cartas = self.crear_boton("Ver las Cartas", "imagenes/ui/pila_cartas.png")
        self.boton_ver_cartas.clicked.connect(self.controlador_juego.mostrar_ver_cartas)
        tooltip_cartas = ("Ver las Cartas.")
        self.boton_ver_cartas.setToolTip(tooltip_cartas)
        self.layout_arriba_abajo.addWidget(self.boton_ver_cartas)
        
        # Botón "A cerca de la Interfaz":
        self.boton_a_cerca_interfaz = self.crear_boton("A cerca de la Interfaz", "imagenes/ui/tablero.png")
        self.boton_a_cerca_interfaz.clicked.connect(self.controlador_juego.mostrar_a_cerca_interfaz)
        tooltip_interfaz = ("Ver cómo funciona la Interfaz.")
        self.boton_a_cerca_interfaz.setToolTip(tooltip_interfaz)
        self.layout_arriba_abajo.addWidget(self.boton_a_cerca_interfaz)

        # ---
        
        # Lo de arriba:
        self.layout_arriba.addLayout(self.layout_arriba_arriba)
        self.layout_arriba.addLayout(self.layout_arriba_abajo)
        self.main_layout.addWidget(self.widget_arriba)
        
        # Lo de abajo:
        self.scroll_area_abajo.setWidget(self.controlador_juego.widget_abajo)
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