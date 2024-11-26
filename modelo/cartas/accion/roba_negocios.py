from modelo.cartas.accion.carta_accion import CartaAccion


class RobaNegocios(CartaAccion):
    
    def informacion_para_accion(self) -> str | None:
        return 'RobaNegocios'
    
    def accion(self, info):
        if self.tipo == 'dinero':
            super().accion()
        else:
            if info[0]:
                set_a_robar: list[CartaAccion] = info[0]
                for carta in set_a_robar:
                    carta.duenio.get_objeto_propiedad().quitar_propiedad(carta)
                    carta.duenio = self.duenio
                    self.duenio.agregar_a_propiedades(carta)
            self.duenio = None
        super().accion()

    def es_jugable(self, lista_jugadores: list) -> bool:
        return False