from vistas.vista_iniciar_sesion import IniciarSesion
from vistas.vista_main_menu import MainMenu
from controladores.controlador_crear_cuenta import Controlador_crear_cuenta
from modelo.base_de_datos.jugador_dao.hash_contrasenia import hash_contrasenia, compara_contrasenia
from PyQt6.QtWidgets import QMessageBox
from modelo import jugador
from modelo.base_de_datos.jugador_dao import jugador_dao_impl
from modelo.base_de_datos.jugador_dao import jugador_bdd
from modelo.base_de_datos.jugador_dao import jugador_dao




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
        
    def iniciar_sesion(self):
        usuario = self.usuario_input.text()
        contraseña = self.password_input.text()
        jugador = jugador_bdd()
        jugador.datos_bdd= self.obtener_datos_del_usuario(self)

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
            query = "SELECT contrasenia, salt FROM jugador WHERE nickname = %s" 
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
        
    def verificar_nickname(jugadores, nickname_ingresado): 
        for jugador in jugadores: 
            if jugador.datos_bdd is not None: 
                if jugador.nickname == nickname_ingresado: 
                # Mostrar mensaje de error 
                    msg_box = QMessageBox() 
                    msg_box.setIcon(QMessageBox.Icon.Critical) 
                    msg_box.setText("El nickname ya está registrado.") 
                    msg_box.setWindowTitle("Error de inicio de sesión") 
                    msg_box.exec() 
                    return False 
        return  True  
        
    def buscando_usuario(self): 
        contrasena_ingresada = self.password_input.text() 
        jugador = jugador_bdd() 
        jugador.datos_bdd = self.obtener_datos_del_usuario("nombre_de_usuario") 
        self._controlador.verificar_usuari(jugador, contrasena_ingresada) 
        
    def inicio_de_sesion(jugadores, nickname_ingresado, contrasena_ingresada):
        if  verificar_nickname(jugadores, nickname_ingresado): 
            jugador =Jugador(nickname_ingresado) 
            # Aquí deberías obtener los datos del jugador desde la base de datos 
            jugador.datos_bdd = obtener_datos_del_usuario(nickname_ingresado) 
            if jugador.datos_bdd is None: 
                mostrar_mensaje_error("Usuario no encontrado.") 
            else: 
                if  verificar_contrasena(jugador, contrasena_ingresada): 
                    mostrar_mensaje_info("Inicio de sesión exitoso.") 
                else: 
                    jugador.datos_bdd = None 
                    mostrar_mensaje_error("Contraseña incorrecta.")
        
        
    def abrirSegunda(self):
        self._var = Controlador_crear_cuenta()
        self._vista.close()
