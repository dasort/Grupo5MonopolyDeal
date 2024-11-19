import sys
import psycopg2
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFrame
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from crear_partida import CrearPartida

class IniciarSesion(QDialog):
    def __init__(self, main_menu, parent=None):
        super().__init__(parent)
        self.main_menu = main_menu  
        self.setWindowTitle("Iniciar Sesión")
        self.setGeometry(480, 200, 600, 450)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))
        
        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)
        #self.adjustSize()
        #self.setMinimumSize(600, 300)
        
        # ---

        self.username_label = QLabel("Nombre de Usuario:")
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Ingrese su nombre de usuario.")
        
        # ---
        
        self.password_label = QLabel("Contraseña:")
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Ingrese su contraseña.")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        
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
        
        linea1 = QFrame(self)
        linea2 = QFrame(self)
        linea1.setFrameShape(QFrame.Shape.HLine)
        linea2.setFrameShape(QFrame.Shape.HLine)
        linea1.setFrameShadow(QFrame.Shadow.Sunken)
        linea2.setFrameShadow(QFrame.Shadow.Sunken)
        
        # ---

        self.main_layout.addWidget(self.username_label)
        self.main_layout.addWidget(self.username_input)
        self.main_layout.addSpacing(20)
        self.main_layout.addWidget(linea1)
        self.main_layout.addWidget(self.password_label)
        self.main_layout.addWidget(self.password_input)
        self.main_layout.addSpacing(20)
        self.main_layout.addWidget(linea2)
        self.main_layout.addSpacing(20)
        self.main_layout.addWidget(self.login_button)
        self.main_layout.addWidget(self.register_button)
        self.main_layout.addWidget(self.boton_volver)

    def iniciar_sesion(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Campos vacíos", "Por favor, complete todos los campos.")
            return

        try:
            # Conexión BD
            conexion = psycopg2.connect(
                host="localhost",
                database="monopoly_db",
                user="tu_usuario",
                password="tu_contraseña"
            )
            cursor = conexion.cursor()

            # Consulta
            query = "SELECT * FROM usuarios WHERE nombre = %s AND contraseña = %s"
            cursor.execute(query, (username, password))
            resultado = cursor.fetchone()

            if resultado:
                QMessageBox.information(self, "Inicio de Sesión", f"¡Bienvenido, {username}!")
                self.abrir_crear_partida()
            else:
                QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")
            
            cursor.close()
            conexion.close()

        except Exception as e:
            QMessageBox.critical(self, "Error de Conexión", f"No se pudo conectar a la base de datos: {str(e)}")

    def registrar_usuario(self):
        usuario = self.username_input.text()
        contraseña = self.password_input.text()

        if not usuario or not contraseña:
            QMessageBox.warning(self, "Campos vacíos", "Por favor, complete todos los campos.")
            return
        try:
            # Conectar BD
            conexion = psycopg2.connect(
                host="localhost",
                database="monopoly_db",
                user="tu_usuario",
                password="tu_contraseña"
            )
            cursor = conexion.cursor()

            consulta_verificar = "SELECT * FROM usuarios WHERE nombre = %s"
            cursor.execute(consulta_verificar, (usuario,))
            resultado = cursor.fetchone()

            if resultado:
                QMessageBox.warning(self, "Usuario existente", "El nombre de usuario ya está registrado. Elija otro.")
                return

            # Insertar en BD
            consulta_insertar = "INSERT INTO usuarios (nombre, contraseña) VALUES (%s, %s)"
            cursor.execute(consulta_insertar, (usuario, contraseña))
            conexion.commit()

            QMessageBox.information(self, "Registro Exitoso", "Usuario registrado con éxito.")
    
        except Exception as e:
            QMessageBox.critical(self, "Error de Conexión", f"No se pudo conectar a la base de datos: {str(e)}")
    
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def volver(self):
        self.hide()
        self.main_menu.show()

    def abrir_crear_partida(self):
        self.hide()
        self.crear_partida_window = CrearPartida(self)
        self.crear_partida_window.show()
