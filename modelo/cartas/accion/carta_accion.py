from abc import abstractmethod
from modelo.cartas.carta import Carta


class CartaAccion(Carta):
    
    def cambia_a_dinero(self):
        self.tipo = 'dinero'
        
    def accion(self) -> None:
        Carta.accion(self)

    @abstractmethod
    def es_jugable(self, lista_jugadores: list) -> bool:
        pass
