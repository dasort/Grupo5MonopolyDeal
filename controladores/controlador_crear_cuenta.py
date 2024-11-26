from modelo.base_de_datos.jugador_dao.jugador_dao_impl import JugadorDAOImpl
from modelo.base_de_datos.jugador_dao.jugador_bdd import JugadorBDD
from modelo.base_de_datos.jugador_dao.jugador_dao import JugadorDAO
from modelo.base_de_datos.conexion.monopoly_db import Database
from controladores.controlador_crear_partida import ControladorCrearPartida
from vistas.vista_crear_cuenta import CrearCuenta


class Controlador_crear_cuenta:
    def __init__(self, main_menu):
        self.__main_menu = main_menu
        self.__vista = CrearCuenta(self)
        self.__vista.show()
        
    def volver(self):
        self.__vista.hide()
        self.__main_menu.get_vista().show()

    # def abrir_crear_partida(self):
    #     self.__vista.hide()
    #     self.crear_partida_window = CrearPartida(self)
    #     self.crear_partida_window.show()
        
    def registrar_usuario(self):
        usuario = self.__vista.get_usuario()
        nombre  = self.__vista.get_nombre()
        apellido = self.__vista.get_apellido()
        contrasenia = self.__vista.get_contrasenia()
        jugador = JugadorBDD.constructor_reducido(nombre,apellido,usuario,contrasenia)

        if not usuario or not contrasenia or not nombre or not apellido:
            self.__vista.campos_vacios_dialog()
            return
        else:
            conn = JugadorDAOImpl(Database.conexion())
            if self.usuario_repetido(usuario, conn):
                self.__vista.usuario_ya_existe_dialog()
            else:
                conn.crear_jugador(jugador)
                self.__vista.usuario_registrado_dialog()
            conn.terminar_conexión()

    def usuario_repetido(self, usuario: str, conn: JugadorDAOImpl) -> bool:
        busca = conn.obtener_jugador(usuario)
        if busca is None:
            return False
        return True
