from __future__ import annotations
from .hash_contrasenia import hash_contrasenia


class JugadorBDD:

    def __init__(self, id_jugador: int, nombre: str, apellido: str, nickname: str, contrasenia: str, salt: str) -> None:
        self.__id_jugador = id_jugador
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nickname = nickname
        self.__contrasenia = contrasenia
        self.__salt = salt
    
    @classmethod
    def constructor_reducido(cls, nombre: str, apellido: str, nickname: str, contrasenia: str | int) -> JugadorBDD:
        jugador = cls.__new__(cls)
        jugador.__nombre = nombre
        jugador.__apellido = apellido
        jugador.__nickname = nickname
        jugador.set_contrasenia(str(contrasenia))
        return jugador

    def get_id_jugador(self) -> int:
        return self.__id_jugador
    def get_nombre(self) -> str:
        return self.__nombre
    def get_apellido(self) -> str:
        return self.__apellido
    def get_nickname(self) -> str:
        return self.__nickname
    def get_contrasenia(self) -> str:
        return self.__contrasenia
    def get_salt(self) -> str:
        return self.__salt
    
    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre
    def set_apellido(self,apellido: str) -> None:
        self.__apellido = apellido
    def set_nickname(self, nickname: str) -> None:
        self.__nickname = nickname
    def set_contrasenia(self, clave: str) -> None:
        self.__contrasenia, self.__salt = hash_contrasenia(clave)

    def __str__(self):
        return (f"jugador [id = {self.__id_jugador}, "
                f"nombre = {self.__nombre}, "
                f"apellido = {self.__apellido}, "
                f"nickname(alias) = {self.__nickname}, "
                f"contraseña = {self.__contrasenia}, "
                f"salt = {self.__salt}]")
