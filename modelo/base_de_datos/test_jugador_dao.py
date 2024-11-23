from jugador_dao.jugador_dao import JugadorBDD
from conexion.monopoly_db import Database
from jugador_dao.jugador_dao_impl import JugadorDAOImpl
from jugador_dao.hash_contrasenia import compara_contrasenia

db = Database()
conn = JugadorDAOImpl(db.conexion())

cristian_en_bdd = conn.obtener_jugador('c_torres')
# conn.eliminar_jugador(cristian_en_bdd)
    
if cristian_en_bdd is None:
    cristian = JugadorBDD.constructor_reducido(
        'Cristian',
        'Torres',
        'c_torres',
        'contrasenia_segura'
    )
    conn.crear_jugador(cristian)
    print('Jugador Registrado')
else:
    if compara_contrasenia('contrasenia_segura', cristian_en_bdd.get_contrasenia(), cristian_en_bdd.get_salt()):
        print('Son iguales')
    else:
        print('No son iguales')
