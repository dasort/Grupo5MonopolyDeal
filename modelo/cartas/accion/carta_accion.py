from abc import abstractmethod
from modelo.cartas.carta import Carta
from modelo.cartas.carta_dinero import CartaDinero


class CartaAccion(CartaDinero, Carta):
    
    def cambia_a_dinero(self):
        self.tipo = 'dinero'
        
    def accion(self) -> None:
        if self.tipo == 'dinero':
            super(CartaDinero, self).accion()
        elif self.tipo == 'accion':
            Carta.accion(self)
        else:
            raise TypeError('Error de tipo en CartaAccion.')

    @abstractmethod
    def es_jugable(self, lista_jugadores: list) -> bool:
        pass
