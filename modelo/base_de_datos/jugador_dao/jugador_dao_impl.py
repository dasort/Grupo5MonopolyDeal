import psycopg2 as psy
from modelo.base_de_datos.jugador_dao.jugador_bdd import JugadorBDD
from modelo.base_de_datos.jugador_dao.jugador_dao import JugadorDAO


class JugadorDAOImpl(JugadorDAO):
    
    def __init__(self, conexion: psy.extensions.connection) -> None:
        self.__conexion = conexion

    def obtener_jugador(self, nickname: str) -> JugadorBDD:
        jugador= None
        query = "SELECT * FROM jugador WHERE nickname = %s"
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(query, (nickname, ))
            row = cursor.fetchone()
            if row:
                jugador = JugadorBDD(row[0], row[1], row[2], row[3], row[4], row[5])
        except (Exception, psy.DatabaseError) as e: #excepcion dependiendo el motor
            print(f"Error al obtener usuario: {e}")
        cursor.close()
        return jugador
    
    def crear_jugador(self, jugador: JugadorBDD) -> None:
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
            cursor.close()
        except (Exception, psy.DatabaseError)as e:
            print(f"Error al insertar usuario: {e}")
    
    def eliminar_jugador(self, jugador: JugadorBDD) -> None:
        query = "DELETE FROM jugador WHERE id_jugador = %s"
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(query, (str(jugador.get_id_jugador()), ))
            self.__conexion.commit()
            cursor.close()
        except (Exception, psy.DatabaseError)as e:
            print(f"Error al eliminar usuario: {e}")
            
    def actulizar_jugador(self, jugador: JugadorBDD) -> None:
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
            cursor.close()
        except (Exception, psy.DatabaseError)as e:
            print(f"Error al actualizar usuario: {e}")

    def obtener_historial(self, jugador: JugadorBDD) -> tuple[int, int]:
        '''Devuelve la cantidad de partidas jugadas y partidas ganadas por el jugador pasado como parámetro.'''
        query_jugados = '''
                select j.id_jugador, count(*)
                from jugador as j
                natural join juega
                where j.nickname = %s
                group by j.id_jugador
                '''
        query_ganados = '''
                select j.id_jugador, count(p.ganador)
                from jugador as j
                natural join juega
                natural join partida as p
                where j.nickname = %s
                group by j.id_jugador
                '''
        partidas_jugadas = 0
        partidas_ganadas = 0
        try:
            cursor = self.__conexion.cursor()
            cursor.execute(query_jugados, (str(jugador.get_id_jugador()), ))
            partidas_jugadas = cursor.fetchone()
            if partidas_jugadas is not None:
                cursor.execute(query_ganados, (jugador.get_nickname(), ))
                partidas_ganadas = cursor.fetchone()
                if partidas_ganadas is None:
                    partidas_ganadas = 0
            else:
                partidas_jugadas = 0
                partidas_ganadas = 0
        except (Exception, psy.DatabaseError)as e:
            print(f"Error al obtener el historial: {e}")
        cursor.close()
        if isinstance(partidas_jugadas, tuple):
            partidas_jugadas = partidas_jugadas[1]
        if isinstance(partidas_ganadas, tuple):
            partidas_ganadas = partidas_ganadas[1]
        return partidas_jugadas, partidas_ganadas

    def terminar_conexión(self):
        self.__conexion.close()
