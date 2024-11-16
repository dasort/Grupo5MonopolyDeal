'''
    configparser permite acceder a las secciones de un archivo ini, elegir una de las secciones y obtener los valores key=value de
    la sección para arreglarlos como diccionario y devolverlos.
'''
from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    '''
        filename es el nombre del archivo ini y section es la sección con la configuración que se busca.
        .read(filename) obtiene todas las [secciones] en el ini.
        .has_section() chequea que la sección que se busca esté en el ini y devuelve un boolean.
        .items(section) devuelve los valores de la sección en forma de lista[tupla(str,str)]. Luego se itera sobre esta lista para
        arreglar estos valores en forma de diccionario.
    '''
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} is not found in {filename}.')
    return db

if __name__ == '__main__':
    print(config())
