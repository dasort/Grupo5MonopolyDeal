from modelo.cartas.carta import Carta


class CobradorDeDeuda(Carta):
    
    def informacion_para_accion(self) -> str | None:
        return 'CobradordDeDeuda'
    
    def accion(self, info) -> None:
        cartas = info[0]
        for carta in cartas:
            carta.duenio = self.duenio
            self.duenio.agregar_a_banco(carta)
        self.duenio = None
