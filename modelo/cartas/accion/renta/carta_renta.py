from modelo.cartas.carta import Carta


class CartaRenta(Carta):
    
    def __init__(self, id_carta: int, nombre: str, tipo: str, valor: int, path_a_imagen: str, path_a_queHace: str, color: str) -> None:
        super().__init__(id_carta, nombre, tipo, valor, path_a_imagen, path_a_queHace)
        self._color = color
        self._color_elegido = None

    @property
    def color(self) -> str:
        if self.color is not str:
            return self._color
        return self._color_elegido

    def informacion_para_accion(self) -> str | None:
        return 'Renta'
    
    def accion(self, info) -> None:
        cartas = info[0]
        super().accion()
        for carta in cartas:
            carta.duenio = self.duenio
            self.duenio.agregar_a_banco(carta)
        self.duenio = None
        self._color_elegido = None
