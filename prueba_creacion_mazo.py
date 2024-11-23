from modelo.carta.carta import Carta
from modelo.builder_cartas import *
from modelo.mazo_de_cartas import MazoDeCartas
import modelo.lista_cartas as sett

cartas = []

builder = CrearBuilderCarta()
director = Director()
director.builder = builder

lista_de_cartas = sett.LISTA_PROPIEDADES + sett.LISTA_DINERO + sett.LISTA_ACCIONES

for carta in lista_de_cartas:
    if carta['tipo'] == 'propiedad':
        director.carta_propiedad(
            carta['id'],
            carta['nombre'],
            carta['tipo'],
            carta['valor'],
            carta['color'],
            carta['path_a_imagen'],
            carta['path_a_queHace']
        )
        cartas.append(director.builder.carta)
    elif carta['tipo'] == 'dinero':
        director.carta_dinero(
            carta['id'],
            carta['nombre'],
            carta['tipo'],
            carta['valor'],
            carta['path_a_imagen'],
            carta['path_a_queHace']
        )
        cartas.append(director.builder.carta)
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
        cartas.append(director.builder.carta)
    else:
        raise Exception('Algo salió mal')

mazo = MazoDeCartas(cartas)

una_carta = mazo.dar_cartas(1)
una_carta[0].mostrar_carta()
