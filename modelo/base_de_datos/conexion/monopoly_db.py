import psycopg2
from conexion.singleton import SingletonMeta
from conexion.config import config


class Database(metaclass=SingletonMeta):
    
    def conexion(self) -> psycopg2.extensions.connection:
        '''Devuelve un objeto de conexión a la base de datos.'''
        params = config()
        conn = psycopg2.connect(**params)
        return conn

if __name__ == '__main__':
    # probando que funcione el singleton
    db1 = Database()
    db2 = Database()
    print("ID db1:", str(id(db1)))
    print("ID db2:", str(id(db2)))
