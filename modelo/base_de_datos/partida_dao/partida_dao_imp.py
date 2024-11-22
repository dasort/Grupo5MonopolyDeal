import psycopg2 as psy #motor base datos
from partida_dao.parida_bdd import 
from partida_dao import PartidaDao


class PartidaDaoImpl(PartidaDao):
    def __init__(self, conexion: psy.extensions.connection):
        self.__conexion = conexion
    
    def agregar_partida(self, partida: Partida) -> None:
        partida = None
        query = "INSERT INTO partida (id_partida, id_ganador) VALUES (%s, %s)"
        try:
            cursor= self.__conexion.cursor()
            cursor.execute( query, (str(partida.id_partida), str(partida.id_ganador)) ) 
            self.__conexion.commit()
        except (Exception, psy.DatabaseError) as e:
            print(f"Error al guardar partida: {e}")
        
    def obtener_partida(self, id_partida: int) -> Partida:
        query="SELECT id_partida, id_ganador FROM partida WHERE id_partida = %s"
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(query, (str(id_partida),))
            row = cursor.fetchone()
            if row:
                return Partida(row[0], row[1])
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
        
    def actualizar_ganador_partida(self, partida: Partida) -> None: 
        query = "UPDATE partida SET id_ganador = %s WHERE id_partida = %s"
        try:
            cursor=self.__conexion.cursor()
            cursor.execute(query, (str(partida.id_ganador), str(partida.id_partida)))
            self.__conexion.commit()
        except (Exception, psy.DatabaseError) as e:
            print(f"Error al acyualizar ganador: {e}")
        