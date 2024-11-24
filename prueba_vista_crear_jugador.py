import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout 
from PyQt6.QtGui import QPixmap, QPalette, QBrush 
from PyQt6.QtCore import Qt
from vista_crear_jugador import Vista_crear_jugador


app = QApplication(sys.argv) 
form = vista_crear_partida() 
form.show() 
sys.exit(app.exec())