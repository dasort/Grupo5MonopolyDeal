import psycopg2 as psy #motor base datos
from partida_dao.partida_bdd import PartidaBDD
from partida_dao.partida_dao import PartidaDAO
if __name__ != '__main__':
    from jugador_dao.jugador_bdd import JugadorBDD


class PartidaDaoImpl(PartidaDAO):
    def __init__(self, conexion: psy.extensions.connection):
        self.__conexion = conexion
    
    def agregar_partida(self, partida: PartidaBDD) -> None:
        query = "INSERT INTO partida (ganador) VALUES (%s)"
        try:
            cursor= self.__conexion.cursor()
            cursor.execute(query, (str(partida.id_ganador), )) 
            self.__conexion.commit()
        except (Exception, psy.DatabaseError) as e:
            print(f"Error al guardar partida: {e}")
        
    def obtener_partida(self, id_partida: int) -> PartidaBDD:
        query="SELECT id_partida, ganador FROM partida WHERE id_partida = %s"
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(query, (str(id_partida),))
            row = cursor.fetchone()
            if row:
                return PartidaBDD(row[0], row[1])
        except (Exception, psy.DatabaseError) as e:
            print(f"Error al obtener partida: {e}")
        
    def eliminar_partida(self, id_partida: int) -> None:
        query = "DELETE FROM partida WHERE id_partida = %s"
        try:
            cursor=self.__conexion.cursor()
            cursor.execute(query, (str(id_partida),))
            self.__conexion.commit()
        except (Exception, psy.DatabaseError) as e:
            print(f"Error al eliminar partida: {e}")
        
    def actualizar_ganador_partida(self, partida: PartidaBDD) -> None: 
        query = "UPDATE partida SET ganador = %s WHERE id_partida = %s"
        try:
            cursor=self.__conexion.cursor()
            cursor.execute(query, (str(partida.id_ganador), str(partida.id_partida)))
            self.__conexion.commit()
        except (Exception, psy.DatabaseError) as e:
            print(f"Error al acyualizar ganador: {e}")
    
    def registrar_jugadores_en_partida(self, partida: PartidaBDD, jugadores: list[JugadorBDD]):
        query = "INSERT INTO juega (id_partida, id_jugador) VALUES (%s, %s)"
        try:
            cursor= self.__conexion.cursor()
            for jugador in jugadores:
                cursor.execute(query, (str(partida.id_partida), str(jugador.get_id_jugador()))) 
            self.__conexion.commit()
        except (Exception, psy.DatabaseError) as e:
            print(f"Error al guardar partida: {e}")
