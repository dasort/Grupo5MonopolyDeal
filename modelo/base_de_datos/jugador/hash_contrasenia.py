'''Este módulo tiene funciones para realizar el hasheado de una cadena agregándole un salteado y para visualizar la contraseña y el salt
guardados en la base de datos como cadena de caracteres en hexadecimal.
'''
from hashlib import sha256
from secrets import token_bytes

def hash_contrasenia(contrasenia: str) -> tuple[str, str]:
    '''Hashea una contraseña y le agrega un salteado.
    
    Devuelve la contraseña hasheada y la cadena que se usó como salteado, ambos en hexadecimal.
    '''
    hash_object = sha256()
    hash_object.update(contrasenia.encode()) # se pasa la contraseña al objeto hash como cadena de bytes
    salt = token_bytes(32) # se genera un salteado aleatorio de 32 bytes
    hash_object.update(salt) # se agrega el salteado al final de la contraseña
    contrasenia_hexa = hash_object.hexdigest() # contraseña+salteado hasheados en hexa
    return contrasenia_hexa, salt.hex() # se devuelven los dos en hexadecimal

def a_hexa(cadena_encriptada: memoryview) -> str:
    '''Recibe un objeto memoryview (bytea en la base de datos) y lo devuelve como string de caracteres en hexadecimal.\n
    Usar cuando se necesita comparar una contraseña ingresada por el usuario con la contraseña guardada en la bdd.
    '''
    return cadena_encriptada.tobytes().decode()
