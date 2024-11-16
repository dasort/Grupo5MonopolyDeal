from abc import ABC, abstractmethod

class monopoly_dao(ABC):
    
    @abstractmethod
    def crear_jugador(self,jugador):
        pass
    
    @abstractmethod
    def eliminar_jugador(self,id_jugador):
        pass
    
    @abstractmethod
    def obtener_jugador(self,nickname):
        pass
    
    @abstractmethod
    def guardar_partida(self,alias_ganador):
        pass
    
    @abstractmethod
    def actulizar_jugador(self,jugador):
        pass
