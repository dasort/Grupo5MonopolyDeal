from modelo.cartas.carta import Carta


class CartaPropiedad(Carta):
    
    def __init__(self, id_carta: int, nombre: str, tipo: str, valor: int, path_a_imagen: str, path_a_queHace: str, color: str | list[str]) -> None:
        super().__init__(id_carta, nombre, tipo, valor, path_a_imagen, path_a_queHace)
        self._color = color
    
    @property
    def color(self) -> str | list[str]:
        return self._color
    
    @color.setter
    def color(self, color) -> None:
        self._color = color

    def accion(self) -> None:
        self.duenio.agregar_a_propiedades(self)
