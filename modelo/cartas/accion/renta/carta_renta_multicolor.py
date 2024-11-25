from modelo.cartas.accion.renta.carta_renta_doble import CartaRentaDoble


class CartaRentaMulticolor(CartaRentaDoble):
    
    def informacion_para_accion(self) -> str | None:
        return 'RentaMulticolor'
