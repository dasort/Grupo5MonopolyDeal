import psycopg2 as psy #motor base datos
from partida_dao.partida_bdd import PartidaBDD
from partida_dao.partida_dao import PartidaDAO
if __name__ != '__main__':
    from jugador_dao.jugador_bdd import JugadorBDD


class PartidaDaoImpl(PartidaDAO):
    def __init__(self, conexion: psy.extensions.connection):
        self.__conexion = conexion
    
    def agregar_partida(self, partida: PartidaBDD) -> None:
        query = "INSERT INTO partida (id_partida, ganador) VALUES (%s, %s)"
        try:
            cursor= self.__conexion.cursor()
            if partida.id_ganador is None:
                cursor.execute(query, (str(partida.id_partida), 'null')) 
            else:
                cursor.execute(query, (str(partida.id_partida), str(partida.id_ganador))) 
            self.__conexion.commit()
            cursor.close()
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
            cursor.close()
        except (Exception, psy.DatabaseError) as e:
            print(f"Error al obtener partida: {e}")
        
    def eliminar_partida(self, id_partida: int) -> None:
        query = "DELETE FROM partida WHERE id_partida = %s"
        try:
            cursor=self.__conexion.cursor()
            cursor.execute(query, (str(id_partida),))
            self.__conexion.commit()
            cursor.close()
        except (Exception, psy.DatabaseError) as e:
            print(f"Error al eliminar partida: {e}")
        
    def actualizar_ganador_partida(self, partida: PartidaBDD) -> None: 
        query = "UPDATE partida SET ganador = %s WHERE id_partida = %s"
        try:
            cursor=self.__conexion.cursor()
            cursor.execute(query, (str(partida.id_ganador), str(partida.id_partida)))
            self.__conexion.commit()
            cursor.close()
        except (Exception, psy.DatabaseError) as e:
            print(f"Error al actualizar ganador: {e}")
    
    def registrar_jugador_en_partida(self, partida: PartidaBDD, jugador: JugadorBDD):
        query = "INSERT INTO juega (id_partida, id_jugador) VALUES (%s, %s)"
        try:
            cursor= self.__conexion.cursor()
            cursor.execute(query, (str(partida.id_partida), str(jugador.get_id_jugador()))) 
            self.__conexion.commit()
            cursor.close()
        except (Exception, psy.DatabaseError) as e:
            print(f"Error al guardar partida: {e}")

    def obtener_id_partida(self) -> int:
        query = '''select id_partida
        from partida
        order by id_partida desc'''
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(query)
            row = cursor.fetchone()
            cursor.close()
            if row:
                return row[0]
            else:
                return 1
        except (Exception, psy.DatabaseError) as e:
            print(f"Error al obtener partida: {e}")