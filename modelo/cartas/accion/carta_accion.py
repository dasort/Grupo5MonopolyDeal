from modelo.cartas.carta import Carta
from modelo.cartas.carta_dinero import CartaDinero


class CartaAccion(CartaDinero, Carta):
    
    def cambia_a_dinero(self):
        self.tipo = 'dinero'
        
    def accion(self) -> None:
        super().accion()
