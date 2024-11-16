import psycopg2 as psy
from jugador.jugador import Jugador


class Monopoly_dao_imp:
    
    def __init__(self, conexion: psy.extensions.connection) -> None:
        self.__conexion = conexion

    def obtener_jugador(self, nickname: str) -> Jugador:
        jugador= None
        query = "SELECT * FROM jugador WHERE nickname = %s"
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(query, (nickname, ))
            row = cursor.fetchone()
            if row:
                jugador = Jugador(row[0], row[1], row[2], row[3], row[4], row[5])
        except (Exception, psy.DatabaseError) as e: #excepcion dependiendo el motor
            print(f"Error al obtener usuario por ID: {e}")
        return jugador
    
    def crear_jugador(self, jugador: Jugador) -> None:
        query = "INSERT INTO jugador (nombre, apellido, nickname, contrasenia, salt) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(
                query,
                (
                    jugador.get_nombre(),
                    jugador.get_apellido(),
                    jugador.get_nickname(),
                    jugador.get_contrasenia(),
                    jugador.get_salt()
                )
            )     
            self.__conexion.commit()
        except (Exception, psy.DatabaseError)as e:
            print(f"Error al insertar usuario: {e}")
    
    def eliminar_jugador(self, jugador: Jugador) -> None:
        query = "DELETE FROM jugador WHERE id_jugador = %s"
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(query, (str(jugador.get_id_jugador()), ))
            self.__conexion.commit()
        except (Exception, psy.DatabaseError)as e:
            print(f"Error al eliminar usuario: {e}")
            
    def actulizar_jugador(self, jugador: Jugador) -> None:
        query = """
                UPDATE jugador
                SET nombre = %s, apellido = %s, nickname = %s, contrasenia = %s, salt = %s
                WHERE id_jugador = %s;
                """
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(
                query,
                (
                    jugador.get_nombre(),
                    jugador.get_apellido(),
                    jugador.get_nickname(),
                    jugador.get_contrasenia(),
                    jugador.get_salt(),
                    jugador.get_id_jugador()
                )
            )
            self.__conexion.commit()
        except (Exception, psy.DatabaseError)as e:
            print(f"Error al actualizar usuario: {e}")
