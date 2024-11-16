import psycopg2  as psy #motor base datos

from jugador import Jugador


class Monopoly_dao_imp:
    def __init__(self, conexion:psy._T_conn):
        self.__conexion = conexion

    def obtener_jugador(self,nickname):
        jugador= None
        query = "SELECT * FROM usuarios WHERE id = %s"
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(query, (nickname,))
            row = cursor.fetchone()
            if row:
                usuario = Jugador(row[0], row[1], row[2], row[3], row[4], row[5])
        except (Exception,psy.DatabaseError) as e: #exepcion dependiendo el motor
            print(f"Error al obtener usuario por ID: {e}")
        return usuario
    
    def crear_jugador(self,jugador:Jugador):
        
        query = "INSERT INTO jugador (nombre, apellido, nickname, contrasenia) VALUES (%s, %s)"
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(query, (jugador.get_nombre(), jugador.get_apellido(), jugador.get_nickname, jugador.get_contrasenia()))     
            self.__conexion.commit()
        except (Exception,psy.DatabaseError)as e:
            print(f"Error al insertar usuario: {e}")
    
    def eliminar_jugador(self, id_jugador):
        query = "DELETE FROM jugador WHERE id = %s"
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(query, (id_jugador,))
            self.__conexion.commit()
        except (Exception,psy.DatabaseError)as e:
            print(f"Error al eliminar usuario: {e}")
            
    def actulizar_jugador(self,jugador: Jugador):
        query = "UPDATE jugador sET nombre = %s, apellido = %s nickname =  %s contrasenia =  %s WHERE id = %s"
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(query, (jugador.get_nombre(), jugador.get_apellido(), jugador.get_id_jugador(), jugador.get_nickname(), jugador.get_contrasenia()))
            self.__conexion.commit()
        except (Exception,psy.DatabaseError)as e:
            print(f"Error al actualizar usuario: {e}")
    
        
    