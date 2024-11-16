from __future__ import annotations
from jugador.hash_contrasenia import hash_contrasenia, a_hexa


class Jugador:
    def __init__(self, id_jugador: int, nombre: str, apellido: str, nickname: str, contrasenia: memoryview, salt: memoryview) -> None:
        self.__id_jugador = id_jugador
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nickname = nickname
        self.__contrasenia = contrasenia
        self.__salt = salt
    
    @classmethod
    def constructor_reducido(cls, nombre: str, apellido: str, nickname: str, contrasenia: str | int) -> Jugador:
        jugador = cls.__new__(cls)
        jugador.__nombre = nombre
        jugador.__apellido = apellido
        jugador.__nickname = nickname
        jugador.set_contrasenia(str(contrasenia))
        return jugador

    # capaz crear otro constructor que no reciba id_jugador?
    def get_id_jugador(self) -> int:
        return self.__id_jugador
    def get_nombre(self) -> str:
        return self.__nombre
    def get_apellido(self) -> str:
        return self.__apellido
    def get_nickname(self) -> str:
        return self.__nickname
    def get_contrasenia(self) -> str:
        return a_hexa(self.__contrasenia)
    def get_salt(self) -> str:
        return a_hexa(self.__salt)
    

    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre
    def set_apellido(self,apellido: str) -> None:
        self.__apellido = apellido
    def set_nickname(self, nickname: str) -> None:
        self.__nickname = nickname
    def set_contrasenia(self, clave_nueva: str) -> None:
        self.__contrasenia, self.__salt = hash_contrasenia(clave_nueva)

    
    def __str__(self):
        return (f"jugador [id = {self.__id_jugador}, "
                f"nombre = {self.__nombre}, "
                f"apellido = {self.__apellido}, "
                f"nickname(alias) = {self.__nickname}, "
                f"contraseña = {self.__contrasenia.tobytes().decode()}, "
                f"salt = {self.__salt.tobytes().decode()}]")
