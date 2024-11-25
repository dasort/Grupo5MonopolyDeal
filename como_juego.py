












# No le den bola todavía, lo estoy haciendo (boni)











from PyQt6.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QSpacerItem, QSizePolicy, QFrame, QMessageBox
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
        
        # Estilos de los widgets:
        #self.widget_arriba.setStyleSheet("""
        #    background-color: rgba(89, 45, 22, 1);
        #    border-bottom: 3px solid rgba(72, 26, 11, 1);
        #""")
        #self.widget_abajo.setStyleSheet("""
        #    background-color: rgba(89, 45, 22, 1);
        #""")
        
        # Layouts (Les paso los Widgets):
        self.layout_arriba = QVBoxLayout(self.widget_arriba)
        self.layout_arriba.setContentsMargins(0, 0, 0, 0)
        self.layout_arriba.setSpacing(0)
        
        self.layout_arriba_arriba = QHBoxLayout()
        self.layout_arriba_arriba.setContentsMargins(10, 10, 0, 0)
        self.layout_arriba_arriba.setSpacing(0)
        self.layout_arriba_arriba.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        
        self.layout_arriba_abajo = QHBoxLayout()
        self.layout_arriba_abajo.setContentsMargins(20, 5, 20, 10)
        self.layout_arriba_abajo.setSpacing(12)
        self.layout_arriba_abajo.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        
        # El layout_abajo cambia dinámicamente.
        #self.mostrar_reglas_generales() # <-- Acá me aseguro que empiece con la de Reglas Generales como predeterminado.
        
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
        
        self.layout_arriba.addLayout(self.layout_arriba_arriba)
        self.layout_arriba.addLayout(self.layout_arriba_abajo)
        
        self.main_layout.addWidget(self.widget_arriba)
        #self.main_layout.addWidget(self.layout_arriba_abajo) <-- No porque es dinámico.
    
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
    
    def mostrar_reglas_generales(self):
        pass
    
        # Una línea:
        linea = QFrame(self)
        linea.setFrameShape(QFrame.Shape.HLine)
        linea.setFrameShadow(QFrame.Shadow.Sunken)
        self.layout.addWidget(linea)
        
    def mostrar_ver_cartas(self):
        pass
        
    def mostrar_a_cerca_interfaz(self):
        pass

    def volver(self):
        self.hide()
        self.main_menu.show()
    
    def centrar_ventana(self):
        """Método para centrar la ventana en el centro de la pantalla."""
        forma_pantalla = QGuiApplication.primaryScreen().availableGeometry()
        forma_ventana = self.frameGeometry()
        centro_pantalla = forma_pantalla.center()
        forma_ventana.moveCenter(centro_pantalla)
        self.move(forma_ventana.topLeft())