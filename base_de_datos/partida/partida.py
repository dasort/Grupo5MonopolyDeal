
class Partida: 
    def __init__(self,id_partida,id_ganador) -> None:
        self.__id_partida = id_partida
        self.__id_ganador = id_ganador
        
    
    @property 
    def id_partida(self):
        return self.__id_partida
    @property 
    def id_ganador(self):
        return self.__id_ganador 
    
    def __str__(self):
        return f"Partida [id_patida= {self.__id_partida}, id_ganador= {self.__id_ganador} ]"
    
    