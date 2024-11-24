from carta.carta import Carta
from jugador import Jugador


class CartaRentaMulticolor(Carta):
    
    def informacion_para_accion(self) -> str | None:
        return 'jugador'
    
    def accion(self, jugador: Jugador) -> None:
        pass
