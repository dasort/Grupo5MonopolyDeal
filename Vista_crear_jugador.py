import sys 
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout 
from PyQt6.QtGui import QPixmap, QPalette, QBrush 
from PyQt6.QtCore import Qt

class vista_crear_partida(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
    def initUI(self):
        #titulo
        self.setWindowTitle('crear usuario')
        #fondo 
        self.setAutoFillBackground(True)
        palette = self.palette() 
        background = QPixmap('C:\Users\carlo\Downloads\imagenes\monopoly-removebg-preview.png') 
        palette.setBrush(QPalette.ColorRole.Window, QBrush(background))
        self.setPalette(palette)
        # Crear el gestor de diseño vertical 
        main_layout = QVBoxLayout() 
        # Crear los widgets del formulario 
        nombre_name_label = QLabel('NOMBRE') 
        self.nombre_name_input = QLineEdit() 
        apellido_name_label = QLabel('APELLIDO') 
        self.apellido_name_input = QLineEdit() 
        nickname_label = QLabel('NICKNAME O APODO') 
        self.nickname_input = QLineEdit() 
        CONTRASENIA_label = QLabel('CONTRASEÑA') 
        self.CONTRASENIA_input = QLineEdit() 
        self.CONTRASENIA_input.setEchoMode(QLineEdit.EchoMode.Password) 
        crear_jugador_button = QPushButton('CREAR JUGADOR') 
        crear_jugador_button.clicked.connect(self.crear_jugador) # Agregar widgets al gestor de diseño main_layout.addWidget(first_name_label) main_layout.addWidget(self.first_name_input) main_layout.addWidget(last_name_label) main_layout.addWidget(self.last_name_input) main_layout.addWidget(email_label) main_layout.addWidget(self.email_input) main_layout.addWidget(password_label) main_layout.addWidget(self
        
        self.setLayout(main_layout)
        
    def crear_jugador(self): 
        nombre = self.nombre_name_input.text() 
        apellido= self.apellido_name_input.text() 
        nickname = self.nickname_input.text() 
        contrasenia= self.CONTRASENIA_input.text() 
        print(f'Cuenta creada para {nombre} {apellido} nickname o apodo {nickname}')
        
    
    
    
    
    
        
        
        
        