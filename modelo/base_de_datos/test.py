from jugador.jugador import Jugador
from conexion.monopoly_db import Database
from jugador.monopoly_dao_impl import Monopoly_dao_imp
from jugador.hash_contrasenia import hash_contrasenia

db = Database()
conn = Monopoly_dao_imp(db.conexion())

lucas = conn.obtener_jugador('lv')
print(lucas.get_contrasenia())
print(hash_contrasenia('123456')[0])