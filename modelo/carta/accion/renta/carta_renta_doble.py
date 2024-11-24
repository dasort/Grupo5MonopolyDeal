from carta.carta import Carta
from jugador import Jugador


class CartaRentaDoble(Carta):
    
    @property
    def color(self) -> str:
        if self.color is not str:
            raise ValueError
        return self.__color_elegido
    
    def informacion_para_accion(self) -> str | None:
        return 'jugadores', 'color'
    
    def accion(self, jugadores: list[Jugador], color: str) -> None:
        self.__color_elegido = color
        for jugador in jugadores:
            jugador.
