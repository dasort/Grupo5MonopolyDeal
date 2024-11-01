# Si se quiere guardar contraseñas en una base de datos para confirmar un login, guardarlas como texto puede causar vulnerabilidades
# y si alguien accede a la BD van a poder entrar a las cuentas de todas las personas registradas.
# Por esto es mejor guardar las contraseñas y otros datos sensibles como un hashing, para que no se pueda vulnerar una cuenta aunque
# se filtre la BD.
# La biblioteca hashlib provee varios métodos para realizar hashings sobre cadenas. Estos métodos ya están refinados y utilizan
# algoritmos de encriptación complejos, por lo que es más conveniente y seguro que programar un hashing propio que puede ser
# sencillo de vulnerar.
# El hashing más comunmente usado es el sha-256, definido como sha256 en la librería.
# sha256 es un método constructor que devuelve un objeto hash. A este objeto se le pueden pasar cadenas binarias (de la forma b'str')
# a través del método update() y devolver el hashing de la cadena con los métodos digest(), que devuelve un objeto de bytes,
# o hexdigest(), que devuelve una cadena en hexadecimal.

from hashlib import sha256

h = sha256() # constructor del algoritmo sha-256. Guarda el objeto hash en h

h.update(b'contrasenia') # update le pasa una cadena al objeto hash. La b convierte la cadena en un bytes string

# dos formas de obtener el hashing:

hash_hexa = h.hexdigest() # como hexadecimal
print('\nHash en hexadecimal: ' + hash_hexa, end='\n\n')

hash_byte = h.digest() # como objeto de bytes
print(f'Hash como objeto de bytes: {hash_byte}', end='\n\n')


# Usar solo hashing para guardar data sensible no es totalmente seguro, porque si dos usuarios ingresan la misma contraseña, el
# hashing resultante va a ser el mismo para los dos y si la contraseña es común y/o sencilla con decifrar una de las contraseñas se
# vulneran a 2 usuarios. En una base de datos grande puede que hayan un número de usuarios grande con la misma contraseña y hashing
# por lo que es importante ocultar a cualquier agente externo que esas cuentas tienen la misma contraseña.
# Para hacer eso se una un 'salt' o salteado, que es data aleatoria que se agrega a un hash para garantizar que sea único y diferenciarlo del
# resto. El salteado se agrega al principio o al final de la contraseña antes de que se hashee y se guarda en la base de datos sin
# encriptar.
# La biblioteca secrets posee métodos que generan números aleatorios criptográficamente fuertes y tokens seguros para usar en
# contraseñas y urls.
# Podemos usar el método token_bytes(nbytes: int) para generar una cadena de bytes aleatoria para usar como salt en nuestra
# encriptación.

import secrets

password = 'contrasenia'

print(f'Probando .encode: {password.encode()}', end='\n\n') # el método encode convierte una variable string a su equivalente en bytes string

salt = secrets.token_bytes(32) #genera un bytes string de 32 bytes. 32 bytes es considerado suficientemente seguro para muchos ámbitos

print(f'Salt generado: {salt}', end='\n\n')

h = sha256() # reseteando el contenido de h. El hash object no borra su contenido así que usar update otra vez concatena en vez de sobreescribir

# se agrega el salt al momento de pasar la contraseña al objeto hash

h.update(salt + password.encode())

hexa_con_salt = h.hexdigest()

bytes_con_salt = h.digest()

print('Hash con salt en hexadecimal: ' + hexa_con_salt, end='\n\n')

print(f'Hash como objeto de bytes con salt: {bytes_con_salt}', end='\n\n')
