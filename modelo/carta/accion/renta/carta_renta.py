from carta.carta import Carta
from jugador import Jugador


class CartaRenta(Carta):
    
    def informacion_para_accion(self) -> str | None:
        return 'jugadores', 'color'
    
    def accion(self, jugadores: list[Jugador]) -> None:
        pass
