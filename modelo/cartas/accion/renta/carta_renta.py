from modelo.cartas.accion.carta_accion import CartaAccion


class CartaRenta(CartaAccion):
    
    def __init__(self, id_carta: int, nombre: str, tipo: str, valor: int, path_a_imagen: str, path_a_queHace: str, color: list) -> None:
        super().__init__(id_carta, nombre, tipo, valor, path_a_imagen, path_a_queHace)
        self._color = color
        self._color_elegido = None

    @property
    def color(self) -> str:
        if self.color is not str:
            return self._color
        return self._color_elegido

    @color.setter
    def color(self, color) -> None:
        self._color_elegido = color
        
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

    def es_jugable(self, lista_jugadores: list) -> bool:
        colores = self._color
        colores_que_tiene = []
        for color in colores:
            if self.duenio.tiene_propiedades_color(color):
                colores_que_tiene.append(color)
        if not colores_que_tiene:
            return False
        else:
            for color in colores_que_tiene:
                valor_renta = self.duenio.get_valor_alquiler_color(color)
                for jugador in lista_jugadores:
                    if jugador != self.duenio:
                        if jugador.calcular_valor_banco() >= valor_renta:
                            return True
                return False