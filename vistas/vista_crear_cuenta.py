import sys
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFrame, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon, QPixmap, QGuiApplication
from PyQt6.QtCore import Qt, QTimer
from vistas.vista_crear_partida import CrearPartida


class CrearCuenta(QDialog):
    def __init__(self, main_menu, parent=None):
        super().__init__(parent)
        self.main_menu = main_menu  
        self.setWindowTitle("Crear Cuenta")
        self.setGeometry(480, 200, 600, 450)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))
        self.centrar_ventana()
        
        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)
        
        # ---
        
        # Imagen encabezado:
        self.imagen_label = QLabel(self)
        pixmap = QPixmap("imagenes/ui/headerLogo.png").scaled(
            400, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
        )
        self.imagen_label.setPixmap(pixmap)
        self.imagen_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # ---

        # Label "Nombre":
        self.nombre_label = QLabel("Nombre de Pila:")
        self.nombre_label.setStyleSheet("""
            /*padding: 6px;*/
            font-size: 20px;
        """)
        
        # LineEdit del nombre de pila:
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText("Ingrese su nombre de pila.")
        self.nombre_input.setFixedHeight(33)
        self.nombre_input.setStyleSheet("""
            font-size: 20px;
        """)
        
        # ---
        
        # Label "Apellido":
        self.apellido_label = QLabel("Apellido:")
        self.apellido_label.setStyleSheet("""
            /*padding: 6px;*/
            font-size: 20px;
        """)
        
        # LineEdit del apellido:
        self.apellido_input = QLineEdit(self)
        self.apellido_input.setPlaceholderText("Ingrese su apellido.")
        self.apellido_input.setFixedHeight(33)
        self.apellido_input.setStyleSheet("""
            font-size: 20px;
        """)
        
        # ---
        
        tooltip_nickname = (
            "Este es su nickname, el nombre que aparecerá<br>"
            "para los demás, debe ser único."
        )
        
        # Label "Nombre de Usuario":
        self.username_label = QLabel("Nombre de Usuario:")
        self.username_label.setStyleSheet("""
            /*padding: 6px;*/
            font-size: 20px;
        """)
        self.username_label.setToolTip(tooltip_nickname)
        
        # LineEdit del nombre de usuario:
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Ingrese su nombre de usuario.")
        self.username_input.setFixedHeight(33)
        self.username_input.setStyleSheet("""
            font-size: 20px;
        """)
        self.username_input.setToolTip(tooltip_nickname)
        
        # ---
        
        # Label "Contraseña":
        self.password_label = QLabel("Contraseña:")
        self.password_label.setStyleSheet("""
            /*padding: 6px;*/
            font-size: 20px;
        """)
        
        # Layout horizontal de la contraseña:
        
        self.layout_contrasenia = QHBoxLayout()
        
        # (1/2) LineEdit de la contraseña:
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Ingrese su contraseña.")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setFixedHeight(33)
        self.password_input.setStyleSheet("""
            font-size: 20px;
        """)
        self.layout_contrasenia.addWidget(self.password_input) # <-- Agrego 1/2 (El LineEdit).
        
        # (2/2) Botón de la contraseña:
        self.boton_ojo = QPushButton(self) # <-- Este es el contenedor principal.
        self.boton_ojo.setStyleSheet("""
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
        self.boton_ojo.clicked.connect(self.alternar_modo_echo)
        self.boton_ojo.setFixedHeight(30)
        self.boton_ojo.setFixedWidth(60)
        tooltip_text = (
            "Es realmente muy recomendable que<br>"
            "priorice su privacidad."
        )
        self.boton_ojo.setToolTip(tooltip_text)

        # Layout del ícono (y el texto por si queremos agregarle "Ver contraseña"):
        self.layout_interno_ojo = QHBoxLayout(self.boton_ojo)

        # Ícono:
        self.icono_label = QLabel(self)
        pixmap = QPixmap("imagenes/ui/ojo_cerrado.png").scaled(25, 25)
        self.icono_label.setPixmap(pixmap)
        self.icono_label.setFixedSize(25, 15)
        self.layout_interno_ojo.addWidget(self.icono_label)
        
        self.layout_contrasenia.addWidget(self.boton_ojo) # <-- Agrego 2/2 (El botón).
        
        # ---

        self.register_button = QPushButton("Crear Cuenta", self)
        self.register_button.setStyleSheet("""
            QPushButton {
                padding: 6px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #4D4D4D;
            }
        """)
        self.register_button.clicked.connect(self.registrar_usuario)
        
        # ---

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
        
        # ---

        self.main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        self.main_layout.addWidget(self.imagen_label)
        self.main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        
        self.main_layout.addWidget(self.nombre_label)
        self.main_layout.addWidget(self.nombre_input)
        self.main_layout.addWidget(self.apellido_label)
        self.main_layout.addWidget(self.apellido_input)
        self.main_layout.addWidget(self.username_label)
        self.main_layout.addWidget(self.username_input)
        #self.main_layout.addSpacing(15)
        self.main_layout.addWidget(self.password_label)
        self.main_layout.addLayout(self.layout_contrasenia)
        self.main_layout.addSpacing(15)
        self.main_layout.addWidget(self.register_button)
        self.main_layout.addWidget(self.boton_volver)



    
    def volver(self):
        self.hide()
        self.main_menu.show()

    def abrir_crear_partida(self):
        self.hide()
        self.crear_partida_window = CrearPartida(self)
        self.crear_partida_window.show()
        
    def alternar_modo_echo(self):
        # Estado anterior antes de cambiarlo:
        estado_anterior = self.password_input.echoMode()

        if estado_anterior == QLineEdit.EchoMode.Password:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal) # <-- Modo normal.
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password) # <-- Modo echo (oculto).
        
        def terminar_cambio_ojo():
            if estado_anterior == QLineEdit.EchoMode.Password:
                pixmap = QPixmap("imagenes/ui/ojo.png").scaled(25, 25)
            else:
                pixmap = QPixmap("imagenes/ui/ojo_cerrado.png").scaled(25, 25)
            self.icono_label.setPixmap(pixmap)
            
        pixmap_ojo_medio = QPixmap("imagenes/ui/ojo_medio.png").scaled(25, 25)
        self.icono_label.setPixmap(pixmap_ojo_medio)

        QTimer.singleShot(150, terminar_cambio_ojo) # <-- 150 ms de transición.

    def centrar_ventana(self):
        """Método para centrar la ventana en el centro de la pantalla."""
        forma_pantalla = QGuiApplication.primaryScreen().availableGeometry()
        forma_ventana = self.frameGeometry()
        centro_pantalla = forma_pantalla.center()
        forma_ventana.moveCenter(centro_pantalla)
        self.move(forma_ventana.topLeft())
