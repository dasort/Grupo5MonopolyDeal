from modelo.cartas.accion.carta_accion import CartaAccion


class TratoForzoso(CartaAccion):
    
    def informacion_para_accion(self) -> str | None:
        return 'TratoForzoso'

    def accion(self, info) -> None:
        if self.tipo == 'dinero':
            super().accion()
        else:
            if info[0]:
                propiedad_propia = info[0]
                propiedad_otro = info[1]
                propiedad_propia.duenio.get_objeto_propiedad().quitar_propiedad(propiedad_propia)
                propiedad_otro.duenio.get_objeto_propiedad().quitar_propiedad(propiedad_otro)
                propiedad_propia.duenio = propiedad_otro.duenio
                propiedad_otro.duenio = self.duenio
                propiedad_otro.duenio.agregar_a_propiedades(propiedad_otro)
                propiedad_propia.duenio.agregar_a_propiedades(propiedad_propia)
                super().accion()
                self.duenio = None

    def es_jugable(self, lista_jugadores: list) -> bool:
        if self.duenio.get_objeto_propiedad()
        for jugador in lista_jugadores:
            if jugador 
