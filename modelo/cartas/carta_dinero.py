from modelo.cartas.carta import Carta


class CartaDinero(Carta):
    
    def accion(self) -> None:
        self.duenio.agregar_a_banco(self)
        super().accion()
