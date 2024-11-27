from vistas.vista_estadisticas import Estadisticas
from modelo.base_de_datos.conexion.monopoly_db import Database
from modelo.base_de_datos.jugador_dao.jugador_dao_impl import JugadorDAOImpl
from modelo.base_de_datos.jugador_dao.jugador_bdd import JugadorBDD

class ControladorEstadisticas:
    def __init__(self, main_menu, jugador: JugadorBDD):
        self.__main_menu = main_menu
        self.__jugador = jugador
        self.__vista = Estadisticas(self)
        self.__vista.show()
    
    def volver(self): #ocultar la vista de estadisticas
        self.__vista.hide()
        self.__main_menu.get_vista().show()

    def datos(self):
        self.__nombre = self.__jugador.get_nombre()
        self.__apellido = self.__jugador.get_apellido()
        self.__nickname = self.__jugador.get_nickname()
        
        db = Database()
        conn = JugadorDAOImpl(db.conexion())
        
        partidas_jugadas, partidas_ganadas = conn.obtener_historial(self.__jugador)
        
        self.__partidas_jugadas = partidas_jugadas
        self.__partidas_ganadas = partidas_ganadas
        
        conn.terminar_conexión()
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_nickname(self):
        return self.__nickname
    
    def get_partidas_jugadas(self):
        return str(self.__partidas_jugadas)
    
    def get_partidas_ganadas(self):
        return str(self.__partidas_ganadas)
