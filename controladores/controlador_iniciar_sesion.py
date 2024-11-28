from vistas.vista_iniciar_sesion import IniciarSesion
from controladores.controlador_crear_cuenta import Controlador_crear_cuenta
from controladores.controlador_estadisticas import ControladorEstadisticas
from modelo.base_de_datos.jugador_dao.hash_contrasenia import compara_contrasenia
from modelo.jugador import Jugador
from modelo.base_de_datos.jugador_dao.jugador_dao_impl import JugadorDAOImpl
from modelo.base_de_datos.conexion.monopoly_db import Database

class Controlador_iniciar_sesion:
    def __init__(self, main_menu, jugador: Jugador = None, jugadores: list[Jugador] = None, crear_partida = None, busca_historial: bool = False):
        self.__jugador = jugador
        self.__jugadores = jugadores
        self.__main_menu = main_menu
        self.__crear_partida = crear_partida
        self.__buscar_historial = busca_historial
        self.__vista = IniciarSesion(self)
        self.__vista.show()
    
    def get_vista(self):
        return self.__vista  

    def volver(self):
        self.__vista.hide()
        self.__main_menu.get_vista().show()

    def volver_partida(self):
        self.__vista.hide()
        self.__crear_partida.set_nombre_usuario(self.__jugador)
        var = self.__crear_partida.get_vista().show()

    def abrir_crear_cuenta(self):
        self.__vista.hide()
        var = Controlador_crear_cuenta(self.__main_menu)
        
    def iniciar_sesion(self):
        usuario = self.__vista.username_input.text()
        contrasenia = self.__vista.password_input.text()
        
        if not usuario or not contrasenia:
            self.__vista.show_error_dialog('Tiene que llenar los dos campos para iniciar sesión.')
        else:
            if self.__buscar_historial:
                self.historial(usuario, contrasenia)
            else:
                db = Database()
                conn = JugadorDAOImpl(db.conexion())
                if self.check_ya_registrado(usuario):
                    self.__vista.show_ya_ingresado_dialog()
                else:
                    jugador_en_base = conn.obtener_jugador(usuario)
                    if jugador_en_base is not None:
                        if compara_contrasenia(contrasenia, jugador_en_base.get_contrasenia(), jugador_en_base.get_salt()):
                            self.__jugador.datos_bdd = jugador_en_base
                            self.__vista.show_info_dialog("Inicio de sesión exitoso.")
                        else:
                            self.__vista.show_error_dialog("Contraseña incorrecta.")
                    else:
                        self.__vista.show_error_dialog("Usuario no encontrado.")
                conn.terminar_conexión()
        
    def check_ya_registrado(self, usuario) -> bool:
        for jugador in self.__jugadores:
            if jugador.datos_bdd is not None:
                if jugador.datos_bdd.get_nickname() == usuario:
                    return True
        return False

    def historial(self, usuario, contrasenia):
        conn = JugadorDAOImpl(Database().conexion())
        jugador_en_base = conn.obtener_jugador(usuario)
        if jugador_en_base is not None:
            if compara_contrasenia(contrasenia, jugador_en_base.get_contrasenia(), jugador_en_base.get_salt()):
                conn.terminar_conexión()
                self.__vista.hide()
                controlador_estadisticas = ControladorEstadisticas(self.__main_menu, jugador_en_base)
            else:
                self.__vista.show_error_dialog("Contraseña incorrecta.")
        else:
            self.__vista.show_error_dialog("Usuario no encontrado.")

    def get_buscar_historial(self):
        return self.__buscar_historial
