from modelo.cartas.propiedad.carta_propiedad import CartaPropiedad


class CartaPropiedadComodin(CartaPropiedad):
    
    def __init__(self, id_carta: int, nombre: str, tipo: str, valor: int, path_a_imagen: str, path_a_queHace: str, color: str | list[str]) -> None:
        super().__init__(id_carta, nombre, tipo, valor, path_a_imagen, path_a_queHace, color)
        self.__color_elegido: str = None

    
    @property
    def color(self) -> str:
        if self._color is not str:
            return self._color
        return self.__color_elegido
    
    def informacion_para_accion(self) -> str | None:
        return 'PropiedadComodin'
    
    def accion(self, info) -> None:
        '''Setea el color de la carta a una de las opciones disponibles.'''
        color = info[0]
        self.__color_elegido = color
        super().accion()
