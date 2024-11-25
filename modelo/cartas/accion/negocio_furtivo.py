from cartas.carta import Carta


class NegocioFurtivo(Carta):
    
    def informacion_para_accion(self) -> str | None:
        return 'NegocioFurtivo'
    
    def accion(self, info) -> None:
        propiedad = info[0]
        propiedad.duenio = self.duenio
        self.duenio.agregar_a_propiedades(propiedad)
        self.duenio = None
