import psycopg2  as psy #motor base datos
from partida import Partida

class partida_dao_imp:
    def __init__(self, conexion:psy._T_conn):
        self.__conexion = conexion
    
    def agregar_partida(self,partida):
        partida = None
        query = "INSERT INTO partidas (id_partida, id_ganador) VALUES (%s, %s)"
        cursor= self.__conexion.cursor()
        cursor.execute( query, (partida.id_partida, partida.id_ganador) ) 
        self.__conexion.commit()
        
    def obtener_partida(self, id_partida):
        query="SELECT id_partida, id_ganador FROM partida WHERE id_partida = %s"
        cursor=self.__conexion.cursor()
        cursor.execute(query, (id_partida,))
        row = cursor.fetchone()
        if row:
            return Partida(row[0], row[1])
        
    def eliminar_partida(self, id_partida):
        query= "DELETE FROM partida WHERE id_partida = %s"
        cursor=self.__conexion.cursor()
        cursor.execute(query, (id_partida,))
        self.__conexion.commit()
        
    def actualizar_ganador_partida(self, id_partida, id_ganador): 
        query="UPDATE partida SET id_ganador = %s WHERE id_partida = %s"
        cursor=self.__conexion.cursor()
        cursor.execute(query, (id_ganador, id_partida))
        self.__conexion.commit()
        
        