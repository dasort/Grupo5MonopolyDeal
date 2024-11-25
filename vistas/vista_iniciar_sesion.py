import sys
import psycopg2
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFrame, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon, QPixmap, QGuiApplication
from PyQt6.QtCore import Qt, QTimer
from crear_partida import CrearPartida
from modelo.base_de_datos.jugador_dao import jugador_dao_impl
from modelo.base_de_datos.jugador_dao import jugador_bdd
from modelo.base_de_datos.jugador_dao import jugador_dao


class IniciarSesion(QDialog):
    def __init__(self, main_menu,controlador ,parent=None):
        super().__init__(parent)
        self.main_menu = main_menu  
        self.controlador = controlador
        self.setWindowTitle("Iniciar Sesión")
        self.setGeometry(480, 200, 600, 450)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))
        self.centrar_ventana()
        
        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)
        #self.adjustSize()
        #self.setMinimumSize(600, 300)
        
        # ---
        
        # Imagen encabezado:
        self.imagen_label = QLabel(self)
        pixmap = QPixmap("imagenes/ui/headerLogo.png").scaled(
            400, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
        )
        self.imagen_label.setPixmap(pixmap)
        self.imagen_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # ---

        # Label "Nombre de Usuario":
        self.username_label = QLabel("Nombre de Usuario:")
        self.username_label.setStyleSheet("""
            /*padding: 6px;*/
            font-size: 20px;
        """)
        
        # LineEdit del nombre de usuario:
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Ingrese su nombre de usuario.")
        self.username_input.setFixedHeight(33)
        self.username_input.setStyleSheet("""
            font-size: 20px;
        """)
        
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
        
        # Botones
        self.login_button = QPushButton("Iniciar Sesión", self)
        self.login_button.setStyleSheet("""
            QPushButton {
                padding: 6px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #4D4D4D;
            }
        """)
        self.login_button.clicked.connect(self.iniciar_sesion)
        
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
        #self.register_button.clicked.connect(self.registrar_usuario) no hace falta porque esto lo hace el vista_crear_cuenta
        
        
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
        
        #linea1 = QFrame(self)
        #linea2 = QFrame(self)
        #linea1.setFrameShape(QFrame.Shape.HLine)
        #linea2.setFrameShape(QFrame.Shape.HLine)
        #linea1.setFrameShadow(QFrame.Shadow.Sunken)
        #linea2.setFrameShadow(QFrame.Shadow.Sunken)
        
        # ---

        self.main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        self.main_layout.addWidget(self.imagen_label)
        self.main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        
        self.main_layout.addWidget(self.username_label)
        self.main_layout.addWidget(self.username_input)
        self.main_layout.addSpacing(15)
        #self.main_layout.addWidget(linea1)
        self.main_layout.addWidget(self.password_label)
        self.main_layout.addLayout(self.layout_contrasenia)
        #self.main_layout.addWidget(self.password_input) <-- En caso de sacar el layout_contrasenia.
        self.main_layout.addSpacing(25)
        #self.main_layout.addWidget(linea2)
        #self.main_layout.addSpacing(20)
        self.main_layout.addWidget(self.login_button)
        self.main_layout.addWidget(self.register_button)
        self.main_layout.addWidget(self.boton_volver)

    

    def iniciar_sesion(self):
        usuario = self.username_input.text()
        contraseña = self.password_input.text()
        jugador = jugador_bdd()
        jugador.datos_bdd= self.ob

        if not usuario or not contraseña:
            QMessageBox.warning(self, "Campos vacíos", "Por favor, complete todos los campos.")
            return
        try:
            # Conectar BD
            conexion = psycopg2.connect(
                host="localhost",
                database="monopoly",
                user="postgres",
                password="1234"
            )
            cursor = conexion.cursor()
            
            bd=None
            bd.obtener_jugador(usuario)

            #consulta_verificar = "SELECT * FROM jugador WHERE nickname = %s"
            #cursor.execute(consulta_verificar, (usuario,))
            #resultado = cursor.fetchone()

            if bd.obtener_jugador():
                QMessageBox.warning(self, "Usuario existente", "El nombre de usuario ya está registrado. Elija otro.")
                return

    
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
                
    def obtener_datos_del_usuario(self,jugador):
        try:
            # Conectar a la base de datos 
            conn = psycopg2.connect( 
                host="localhost",
                database="monopoly",
                user="postgres",
                password="1234" ) 
            cursor = conn.cursor() 
            # Ejecutar la consulta para obtener los datos del usuario 
            query = "SELECT contrasenia, salt FROM usuarios WHERE nombre_usuario = %s" 
            cursor.execute(query, [jugador]) 
            result = cursor.fetchone()
            # Cerrar la conexión 
            cursor.close() 
            conn.close()
            if result: 
                return { 'contrasenia': result[0], 'salt': result[1] } 
            else: 
                return None 
        except Exception as e: 
            print(f"Error al conectarse a la base de datos: {e}")
            return None
        
        

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