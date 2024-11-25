from cartas.carta import Carta
from cartas.carta_dinero import CartaDinero
from cartas.propiedad.carta_propiedad import CartaPropiedad
from cartas.propiedad.carta_propiedad_comodin import CartaPropiedadComodin
from cartas.accion.renta.carta_renta_doble import CartaRentaDoble
from cartas.accion.renta.carta_renta_multicolor import CartaRentaMulticolor
from cartas.accion.es_mi_cumpleanios import EsMiCumpleanios
from cartas.accion.cobrador_de_deudas import CobradorDeDeuda
from cartas.accion.negocio_furtivo import NegocioFurtivo
from cartas.accion.pasa_por_la_salida import PasaPorLaSalida
from cartas.accion.trato_forzoso import TratoForzoso
# from carta.accion.roba_negocios import RobaNegocios
from cartas.accion.renta.carta_renta_doble import CartaRentaDoble
from cartas.accion.renta.carta_renta_multicolor import CartaRentaMulticolor
from mazo_de_cartas import MazoDeCartas
from lista_cartas import *

cartas = []

def crear_carta_propiedad_renta(carta: dict, carta_clase: callable) -> Carta:
    return carta_clase(
        carta['id'],
        carta['nombre'],
        carta['tipo'],
        carta['valor'],
        carta['path_a_imagen'],
        carta['path_a_queHace'],
        carta['color']
    )

for carta in LISTA_PROPIEDADES + LISTA_PROPIEDADES_COMODIN + LISTA_RENTA_DOBLE + LISTA_RENTA_MULTICOLOR:
    if carta in LISTA_PROPIEDADES:
        creada = crear_carta_propiedad_renta(carta, CartaPropiedad)
    elif carta in LISTA_PROPIEDADES_COMODIN:
        creada = crear_carta_propiedad_renta(carta, CartaPropiedadComodin)
    elif carta in LISTA_RENTA_DOBLE:
        creada = crear_carta_propiedad_renta(carta, CartaRentaDoble)
    elif carta in LISTA_PROPIEDADES_COMODIN:
        creada = crear_carta_propiedad_renta(carta, CartaRentaMulticolor)
    else:
        raise Exception('Algo salió mal')
    cartas.append(creada)
    
for carta in LISTA_DINERO:
    cartas.append(
        CartaDinero(
            carta['id'],
            carta['nombre'],
            carta['tipo'],
            carta['valor'],
            carta['path_a_imagen'],
            carta['path_a_queHace']
        )
    )

def crear_carta_accion(carta: dict, carta_accion: callable) -> Carta:
    return carta_accion(
        carta['id'],
        carta['nombre'],
        carta['tipo'],
        carta['valor'],
        carta['path_a_imagen'],
        carta['path_a_queHace']
    )

for carta in LISTA_ACCIONES:
    if carta['nombre'] == "Es Mi Cumpleaños":
        creada = crear_carta_accion(carta, EsMiCumpleanios)
    elif carta['nombre'] == "Negocio Furtivo":
        creada = crear_carta_accion(carta, NegocioFurtivo)
    elif carta['nombre'] == "Pasa Por La Salida":
        creada = crear_carta_accion(carta, PasaPorLaSalida)
    # elif carta['nombre'] == "Roba Negocios":
    #     creada = crear_carta_accion(carta, RobaNegocios)
    elif carta['nombre'] == "Trato Forzoso":
        creada = crear_carta_accion(carta, TratoForzoso)
    elif carta['nombre'] == "Cobrador De Deudas":
        creada = crear_carta_accion(carta, CobradorDeDeuda)
    elif carta['nombre'] == "Cobrador De Deudas":
        creada = crear_carta_accion(carta, CobradorDeDeuda)
    else:
        raise Exception('Algo salió mal')
    cartas.append(creada)

mazo = MazoDeCartas(cartas)

una_carta = mazo.dar_cartas(1)
una_carta[0].mostrar_carta()
