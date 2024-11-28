from modelo.cartas.carta import Carta
from modelo.cartas.carta_dinero import CartaDinero
from modelo.cartas.propiedad.carta_propiedad import CartaPropiedad
from modelo.cartas.propiedad.carta_propiedad_comodin import CartaPropiedadComodin
from modelo.cartas.accion.renta.carta_renta import CartaRenta
from modelo.cartas.accion.renta.carta_renta_multicolor import CartaRentaMulticolor
from modelo.cartas.accion.es_mi_cumpleanios import EsMiCumpleanios
from modelo.cartas.accion.cobrador_de_deudas import CobradorDeDeuda
from modelo.cartas.accion.negocio_furtivo import NegocioFurtivo
from modelo.cartas.accion.pasa_por_la_salida import PasaPorLaSalida
from modelo.cartas.accion.trato_forzoso import TratoForzoso
# from modelo.carta.accion.roba_negocios import RobaNegocios
from modelo.cartas.accion.renta.carta_renta_multicolor import CartaRentaMulticolor
from modelo.lista_cartas import *

def crear_cartas() -> list[Carta]:

    cartas: list[Carta] = []

    def crear_carta_propiedad_renta(carta: dict, carta_clase: callable):
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
            pass
            creada = crear_carta_propiedad_renta(carta, CartaRenta)
        elif carta in LISTA_RENTA_MULTICOLOR:
            pass
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

    def crear_carta_accion(carta: dict, carta_accion: callable):
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
            pass
        elif carta['nombre'] == "Negocio Furtivo":
            creada = crear_carta_accion(carta, NegocioFurtivo)
            pass
        elif carta['nombre'] == "Pasa Por La Salida":
            creada = crear_carta_accion(carta, PasaPorLaSalida)
            pass
        elif carta['nombre'] == "Roba Negocios":
            pass
            # creada = crear_carta_accion(carta, RobaNegocios)
        elif carta['nombre'] == "Trato Forzoso":
            creada = crear_carta_accion(carta, TratoForzoso)
            pass
        elif carta['nombre'] == "Cobrador De Deudas":
            creada = crear_carta_accion(carta, CobradorDeDeuda)
            pass
        elif carta['nombre'] == "Alquiler Doble":
            pass
        else:
            raise Exception('Algo salió mal')
        cartas.append(creada)

    return cartas