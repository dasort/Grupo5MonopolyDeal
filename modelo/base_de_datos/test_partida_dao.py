from partida_dao.partida_bdd import PartidaBDD
from partida_dao.partida_dao_imp import PartidaDaoImpl
from jugador_dao.jugador_bdd import JugadorBDD
from conexion.monopoly_db import Database
from jugador_dao.jugador_dao_impl import JugadorDAOImpl

# partida = PartidaBDD.constructor(3)

conn = Database().conexion()

dao = PartidaDaoImpl(conn)
dao2 = JugadorDAOImpl(conn)

partida = dao.obtener_partida(2)
jugador = dao2.obtener_jugador('c_torres')

dao.registrar_jugadores_en_partida(partida, [jugador])