'''
    Ejemplo de conexión a PostgreSQL en Python. Hecho sin implementar el patrón de diseño DAO o Singleton.
    psycopg2 provee la interfaz para establecer la conexión y acceder a las tablas.
    config permite recibir los parámetros de conexión a la BD en el formato correcto para su utilización.
    La utilización de un archivo .ini permite abstraer los datos necesarios para acceder a una BD del mecanismo por el cuál se
    accede.
    A esto habría que aplicarle DAO y/o Singleton pero se pueden usar los dos patrones con el archivo .ini y config al mismo tiempo
    para abstrar bien el acceso a la BD, las consultas y obtención de datos; y el acceso a la instancia de la conexión.
'''
import psycopg2 as psy
from config import config

def connect():
    '''
        Este método conecta el script con la base de datos llamando al método config.
        Los parámetros de la conexión se guardan en params y se usan en psy.connect para guardar la conexión en la variable
        connection.
        conection.cursor crrea un objeto cursor que permite ejecutar comandos SQL, guardar las tablas resultado de consultas
        y devolver los resultados del query. Cada fila de la tabla resultado se devuelve como tupla y el conjunto de filas se
        devuelve como una lista de tuplas.
        El cursor y la conexión se tienen que cerrar cuando se terminen de usar para liberar el acceso a la base de datos a
        otros hilos.
    '''
    try:
        connection = None
        params = config()
        print('Connecting to postgreSQL database...')
        connection = psy.connect(**params)
        crsr = connection.cursor()
        # Query del ejercicio 9.B. del TP5 de Base de Datos.
        # Cambié el año de 2015 a 2013 porque no hay turnos en el año 2015 en la BD.
        # Los queries se pueden escribir en una sola linea, en múltiples líneas con un espacio al final de la linea o en múltiples
        # líneas con un salto de linea al final de cada una (como hice acá).
        crsr.execute('select descripcion_especialidad, genero_persona, count(tu.codigo_especialidad) as cantidad_turnos, anio_turno\n'
                    'from turnos as tu\n'
                    'join especialidades as esp on tu.codigo_especialidad = esp.codigo_especialidad\n'
                    'join personas as pe on tu.dni_persona = pe.dni_persona,\n'
                    'extract(year from tu.fecha_turno) as anio_turno\n'
                    'where anio_turno = 2013 and genero_persona is not null\n'
                    'group by descripcion_especialidad, genero_persona, anio_turno\n'
                    'order by descripcion_especialidad asc, genero_persona asc')
        profesionales = crsr.fetchall()
        for profesional in profesionales:
            print(profesional)
        crsr.close()
    except (Exception, psy.DatabaseError) as error: # psy.DatabaseError ocurre cuando falla el método psy.connect()
        print(error)
    finally:
        if connection is not None: # connection no es None cuando no falla la conexión a DB
            connection.close()

connect()
