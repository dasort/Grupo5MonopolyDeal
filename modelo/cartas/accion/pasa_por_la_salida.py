from modelo.cartas.carta import Carta


class PasaPorLaSalida(Carta):
    
    def informacion_para_accion(self) -> str | None:
        return 'mazo'

    def accion(self, mazo) -> None:
        cartas = mazo.dar_cartas(1)
        for carta in cartas:
            carta.duenio = self.duenio
        self.duenio.agregar_a_mano(cartas)
        self.duenio = None
