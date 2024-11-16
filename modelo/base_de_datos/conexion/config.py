import os
from configparser import ConfigParser

def config(filename='database.ini', section='postgresql') -> dict:
    '''Transforma una sección de un archivo de configuración a un diccionario.
    
    El archivo debe tener al menos una sección de la forma:
    
    [Sección]\n
    Llave = Valor
    
    Se levanta una excepción si la sección pasada no se encuentra en el archivo.
    '''
    dirname = os.path.dirname(__file__) # obtiene el directorio de config
    filename = os.path.join(dirname, filename) # forma la ruta de acceso a filename, tiene que estar en la misma carpeta que config
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
    # debería imprimir los datos de la sección postgresql en database.ini como diccionario
    print(config())
