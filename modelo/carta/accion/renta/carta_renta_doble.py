from carta.carta import Carta


class CartaRentaDoble(Carta):
    
    @property
    def color(self) -> str:
        if self.color is not str:
            raise ValueError
        return self.__color_elegido
    
    @color.setter
    def color(self, color: str) -> str:
        self.__color_elegido = color
        
    def informacion_para_accion(self) -> str | None:
        return 'RentaDoble'
    
    def accion(self, info) -> None:
        cartas = info[1]
        for carta in cartas:
            carta.duenio = self.duenio
            self.duenio.agregar_a_banco(carta)
        self.duenio = None
