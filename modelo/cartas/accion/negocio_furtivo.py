from modelo.cartas.accion.carta_accion import CartaAccion


class NegocioFurtivo(CartaAccion):
    
    def informacion_para_accion(self) -> str | None:
        return 'NegocioFurtivo'
    
    def accion(self, info) -> None:
        if self.tipo == 'dinero':
            super().accion()
        else:
            if info[0]:
                propiedad = info[0]
                super().accion()
                propiedad.duenio.get_objeto_propiedad().quitar_propiedad(propiedad)
                propiedad.duenio = self.duenio
                self.duenio.agregar_a_propiedades(propiedad)
                self.duenio = None
    
    def es_jugable(self, lista_jugadores: list) -> bool:
        for jugador in lista_jugadores:
            if jugador != self.duenio:
                if jugador.get_objeto_propiedad().get_cartas_propiedades():
                    return True
        return False
