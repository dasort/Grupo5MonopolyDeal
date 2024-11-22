'''Este módulo tiene funciones para realizar el hasheado de una cadena agregándole un salteado y para visualizar la contraseña y el salt
guardados en la base de datos como cadena de caracteres en hexadecimal.
'''
from hashlib import sha256
from secrets import token_hex, compare_digest

def hash_contrasenia(contrasenia: str) -> tuple[str, str]:
    '''Hashea una contraseña y le agrega un salteado.
    
    Devuelve la contraseña hasheada y la cadena que se usó como salteado, ambos en hexadecimal.
    '''
    hash_object = sha256()
    hash_object.update(contrasenia.encode()) # se pasa la contraseña al objeto hash como cadena de bytes
    salt = token_hex(32) # se genera un salteado aleatorio de 32 bytes
    hash_object.update(salt.encode()) # se agrega el salteado al final de la contraseña
    contrasenia_hexa = hash_object.hexdigest() # contraseña+salteado hasheados en hexa
    return contrasenia_hexa, salt # se devuelven los dos en hexadecimal

def compara_contrasenia(contrasenia_ingresada: str, contrasenia_en_bdd: str, salt: str) -> bool:
    '''Recibe la contraseña ingresada por el usuario; y la contraseña y el salt guardados en la base de datos\n
    y chequea que las contaseñas sean iguales.'''
    hash_object = sha256()
    hash_object.update(contrasenia_ingresada.encode())
    hash_object.update(salt.encode())
    contrasenia_ingresada = hash_object.hexdigest()
    return compare_digest(contrasenia_ingresada, contrasenia_en_bdd)
