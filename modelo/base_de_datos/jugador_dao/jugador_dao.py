from abc import ABC, abstractmethod
from jugador_dao.jugador_bdd import JugadorBDD


class JugadorDAO(ABC):
    
    @abstractmethod
    def crear_jugador(self, jugador: JugadorBDD) -> None:
        pass
    
    @abstractmethod
    def eliminar_jugador(self, jugador: JugadorBDD) -> None:
        pass
    
    @abstractmethod
    def obtener_jugador(self, nickname: str) -> JugadorBDD:
        pass
    
    @abstractmethod
    def actulizar_jugador(self, jugador: JugadorBDD) -> None:
        pass
