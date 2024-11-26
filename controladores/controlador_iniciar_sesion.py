from vistas.vista_iniciar_sesion import IniciarSesion
from vistas.vista_main_menu import MainMenu
from controladores.controlador_crear_cuenta import Controlador_crear_cuenta
from modelo.base_de_datos.jugador_dao.hash_contrasenia import hash_contrasenia, compara_contrasenia
from PyQt6.QtWidgets import QMessageBox
from modelo.base_de_datos.jugador_dao.jugador_bdd import JugadorBDD


class Controlador_iniciar_sesion():
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self._vista = IniciarSesion(self)  
        self._vista.show()
        
    def verificar_usuario(self, jugador, contrasena_ingresada):
        if jugador.datos_bdd is None: 
            self.show_error_dialog("Usuario no encontrado.")
            return 
        contrasena_guardada = jugador.datos_bdd['contrasenia']
        salt = jugador.datos_bdd['salt'] 
        
        if compara_contrasenia(contrasena_ingresada, contrasena_guardada, salt): 
            self.show_info_dialog("Inicio de sesión exitoso.") 
        else: 
            jugador.datos_bdd = None 
            self.show_error_dialog("Contraseña incorrecta.")

    def show_error_dialog(self, message): 
        msg_box = QMessageBox() 
        msg_box.setIcon(QMessageBox.Icon.Critical) 
        msg_box.setText(message) 
        msg_box.setWindowTitle("Error")
        msg_box.exec()
        
    def show_info_dialog(self, message): 
        msg_box = QMessageBox() 
        msg_box.setIcon(QMessageBox.Icon.Information) 
        msg_box.setText(message) 
        msg_box.setWindowTitle("Información") 
        msg_box.exec()   
        
    def abrirSegunda(self):
        self._var = Controlador_crear_cuenta()
        self._vista.close()
