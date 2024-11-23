from __future__ import annotations


class PartidaBDD: 
    def __init__(self, id_partida: int, id_ganador: int) -> None:
        self.__id_partida = id_partida
        self.__id_ganador = id_ganador
    
    @classmethod
    def constructor(cls, id_ganador: int) -> PartidaBDD:
        partida = cls.__new__(cls)
        partida.__id_ganador = id_ganador
        return partida
    
    @property 
    def id_partida(self) -> int:
        return self.__id_partida
    
    @id_partida.setter
    def id_partida(self, id_partida: int) -> None:
        self.__id_partida = id_partida
        
    @property 
    def id_ganador(self) -> int:
        return self.__id_ganador 
    
    @id_ganador.setter
    def id_ganador(self, id_ganador: int) -> None:
        self.__id_ganador = id_ganador

    def __str__(self):
        return f"Partida [id_patida= {self.__id_partida}, id_ganador= {self.__id_ganador} ]"
    