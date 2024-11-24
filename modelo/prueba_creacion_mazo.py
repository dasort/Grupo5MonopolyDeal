from carta.carta import Carta
from carta.carta_dinero import CartaDinero
from carta.propiedad.carta_propiedad import CartaPropiedad
from carta.accion.renta.carta_renta import CartaRenta
from carta.accion.renta.carta_renta_multicolor import CartaRentaMulticolor
from carta.accion import es_mi_cumpleanios
from mazo_de_cartas import MazoDeCartas
import lista_cartas

def crear_carta(carta: dict):
    if carta['tipo'] == 'propiedad':
        return CartaPropiedad(
            carta['id'],
            carta['nombre'],
            carta['tipo'],
            carta['valor'],
            carta['color'],
            carta['path_a_imagen'],
            carta['path_a_queHace']
        )

cartas = []

lista_de_cartas = lista_cartas.LISTA_PROPIEDADES + lista_cartas.LISTA_DINERO + lista_cartas.LISTA_ACCIONES

for carta in lista_de_cartas:
    if carta['tipo'] == 'propiedad':
        cartas.append(
            CartaPropiedad(
                
            )
        )
    elif carta['tipo'] == 'dinero':
        CartaDinero(
            carta['id'],
            carta['nombre'],
            carta['tipo'],
            carta['valor'],
            carta['path_a_imagen'],
            carta['path_a_queHace']
        )
    elif carta['tipo'] == 'accion':
        director.carta_accion(
            carta['id'],
            carta['nombre'],
            carta['tipo'],
            carta['accion'],
            carta['valor'],
            carta['path_a_imagen'],
            carta['path_a_queHace']
        )
    else:
        raise Exception('Algo salió mal')

mazo = MazoDeCartas(cartas)

una_carta = mazo.dar_cartas(1)
una_carta[0].mostrar_carta()
