from cartas.carta import Carta


class CartaRentaDoble(Carta):
    
    def __init__(self, id_carta: int, nombre: str, tipo: str, valor: int, path_a_imagen: str, path_a_queHace: str, color: str) -> None:
        super().__init__(id_carta, nombre, tipo, valor, path_a_imagen, path_a_queHace)
        self._color = color
        self._color_elegido = None

    @property
    def color(self) -> str:
        return self._color
    
    @color.setter
    def color(self, color: str) -> str:
        self._color = color

    @property
    def color_elegido(self) -> str:
        return self._color_elegido
    
    @color_elegido.setter
    def color_elegido(self, color: str) -> str:
        self._color_elegido = color
        
    def informacion_para_accion(self) -> str | None:
        return 'RentaDoble'
    
    def accion(self, info) -> None:
        cartas = info[1]
        for carta in cartas:
            carta.duenio = self.duenio
            self.duenio.agregar_a_banco(carta)
        self.duenio = None
