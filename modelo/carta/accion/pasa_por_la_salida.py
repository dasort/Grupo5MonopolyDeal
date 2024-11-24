from carta.carta import Carta


class PasaPorLaSalida(Carta):
    
    def informacion_para_accion(self) -> str | None:
        return 'mazo'

    def accion(self, mazo) -> None:
        for _ in range(2):
            carta = mazo.dar_cartas(1)
            carta.duenio = self.duenio
            self.duenio.agregar_a_mano(carta)
        self.duenio = None
