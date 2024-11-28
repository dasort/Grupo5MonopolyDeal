from modelo.cartas.accion.carta_accion import CartaAccion


class PasaPorLaSalida(CartaAccion):
    
    def informacion_para_accion(self) -> str | None:
        return 'PasaPorLaSalida'

    def accion(self, info) -> None:
        if info[0]:
            mazo = info[0]
            self.duenio.sacar_de_mano(self)
            if len(self.duenio.get_mano()) == 6:
                cartas = mazo.dar_cartas(1)
            else:
                cartas = mazo.dar_cartas(2)
            for carta in cartas:
                carta.duenio = self.duenio
            self.duenio.tomar_carta(cartas)
            self.duenio = None
        else:
            raise ValueError('Error ejecutando la acción de PassaPorLaSalida.')

    def es_jugable(self, jugadores: list) -> bool:
        return True
