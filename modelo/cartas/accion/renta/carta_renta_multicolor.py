from Grupo5MonopolyDeck.modelo.cartas.accion.renta.carta_renta import CartaRenta


class CartaRentaMulticolor(CartaRenta):
    
    def informacion_para_accion(self) -> str | None:
        return 'RentaMulticolor'
