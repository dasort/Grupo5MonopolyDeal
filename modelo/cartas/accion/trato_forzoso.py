from modelo.cartas.accion.carta_accion import CartaAccion


class TratoForzoso(CartaAccion):
    
    def informacion_para_accion(self) -> str | None:
        return 'TratoForzoso'

    def accion(self, info) -> None:
        if info[0]:
            propiedad_que_mando = info[0]
            propiedad_que_llega = info[1]
            propiedad_que_mando.duenio.sacar_de_propiedades(propiedad_que_mando)
            propiedad_que_llega.duenio.sacar_de_propiedades(propiedad_que_llega)
            propiedad_que_mando.duenio = propiedad_que_llega.duenio
            propiedad_que_llega.duenio = self.duenio
            propiedad_que_llega.duenio.agregar_a_propiedades(propiedad_que_llega)
            propiedad_que_mando.duenio.agregar_a_propiedades(propiedad_que_mando)
            super().accion()
            self.duenio = None

    def es_jugable(self, lista_jugadores: list) -> bool:
        if not self.duenio.tiene_propiedades():
            return False
        else:
            for jugador in lista_jugadores:
                if jugador != self.duenio:
                    if jugador.tiene_propiedades():
                        return True
            return False
