from modelo.cartas.accion.carta_accion import CartaAccion


class CobradorDeDeuda(CartaAccion):
    
    def informacion_para_accion(self) -> str | None:
        return 'CobradordDeDeuda'
    
    def accion(self, info) -> None:
        if info:
            cartas = info
            super().accion()
            for carta in cartas:
                carta.duenio.sacar_de_banco(carta)
                carta.duenio = self.duenio
                self.duenio.agregar_a_banco(carta)
            self.duenio = None
        
    def es_jugable(self, lista_jugadores: list) -> bool:
        for jugador in lista_jugadores:
            if jugador != self.duenio:
                if jugador.calcular_valor_banco() >= 5:
                    return True
        return False
