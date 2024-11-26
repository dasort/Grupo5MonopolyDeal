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
                propiedad.duenio.get_objeto_propiedad().quitar_propiedad(propiedad)
                propiedad.duenio = self.duenio
                self.duenio.agregar_a_propiedades(propiedad)
                self.duenio = None
        