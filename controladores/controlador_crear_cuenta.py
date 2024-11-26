import psycopg2
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFrame, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon, QPixmap, QGuiApplication
from PyQt6.QtCore import Qt, QTimer
from vistas.vista_crear_cuenta import CrearCuenta
from modelo.base_de_datos.jugador_dao import jugador_dao_impl
from modelo.base_de_datos.jugador_dao.jugador_bdd import JugadorBDD
from modelo.base_de_datos.jugador_dao.jugador_dao import JugadorDAO


class Controlador_crear_cuenta:
    def __init__(self):
        self._var= CrearCuenta()
        self._var.show()
        
    def registrar_usuario(self):
        usuario = self.username_input.text()
        nombre  = self.nombre_input.text()
        apellido = self.apellido_input.text()
        contraseña = self.password_input.text()
        jugador= JugadorBDD(None,nombre,apellido,usuario,contraseña)

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

            # Insertar en BD
            #insertar_jugador=None
            #insertar_jugador.crear_jugador()
            consulta_insertar = "INSERT INTO jugador (nombre, apellido, nickname, contraseña,) VALUES (%s, %s)"
            cursor.execute(consulta_insertar, (nombre, apellido, usuario, contraseña))
            conexion.commit()

            QMessageBox.information(self, "Registro Exitoso", "Usuario registrado con éxito.")
    
        except Exception as e:
            QMessageBox.critical(self, "Error de Conexión", f"No se pudo conectar a la base de datos: {str(e)}")
    
    
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()



