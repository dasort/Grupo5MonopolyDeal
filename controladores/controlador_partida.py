from random import choice
from typing import Callable
from modelo.jugador import Jugador
from modelo.mazo_de_cartas import MazoDeCartas
from modelo.mazo_de_descarte import MazoDeDescarte
from modelo.cartas.carta import Carta
from modelo.base_de_datos.conexion.monopoly_db import Database
from modelo.base_de_datos.partida_dao.partida_bdd import PartidaBDD
from modelo.base_de_datos.partida_dao.partida_dao_imp import PartidaDaoImpl
from vistas.vista_tablero import Tablero


class ControladorPartida:
    def __init__(self, main_menu: Callable, jugadores: list[Jugador]):
        self.__main_menu = main_menu
        self.__jugadores = jugadores  # Instancias de la clase Jugador
        self.__jugador_actual = choice(self.__jugadores)
        self.__cartas_jugadas_en_turno = 0
        self.__mazo = MazoDeCartas()
        self.__cartas_descarte = MazoDeDescarte()  # Pila de descarte
        self.__turno_actual = self.__jugadores.index(self.__jugador_actual)
        self.__ganador: Jugador = None
        self.repartir_cartas()
        self.__vista = Tablero(self)
        self.__vista.show()

    def get_mazo(self):
        return self.__mazo

    def get_jugador_actual(self) -> Jugador:
        return self.__jugador_actual

    def get_jugadores(self):
        return self.__jugadores
    
    def get_turno_actual(self):
        return self.__turno_actual
    
    def jugadores_sin_actual(self) -> list[Jugador]:
        sin_actual= []
        for jugador in self.__jugadores:
            if jugador is not self.__jugador_actual:
                sin_actual.append(jugador)
        return sin_actual
    
    # Reparte 5 cartas a cada jugador
    def repartir_cartas(self):
        for jugador in self.__jugadores:
            jugador.tomar_carta(self.__mazo.dar_cartas(5))
        self.dar_dos_cartas()
    
    # Toma una carta aleartoria del mazo eliminandola
    def tomar_carta_mazo(self, jugador: Jugador):
        jugador.tomar_carta(self.__mazo.dar_cartas(1))
    
    def dar_dos_cartas(self):
        self.__jugador_actual.tomar_carta(self.__mazo.dar_cartas(2))

    def dar_cinco_cartas(self):
        self.__jugador_actual.tomar_carta(self.__mazo.dar_cartas(5))

############################################################################################################################
######################################## Código para jugar las cartas ######################################################
############################################################################################################################

    def jugar_carta(self, carta: Carta) -> None:
        # Verificar si la carta puede ser jugada
        if carta.es_jugable(self.__jugadores):
            try:
                pedido = carta.informacion_para_accion()
                if pedido is not None:
                    datos_para_accion = self.procesa_pedido(pedido, carta)
                    carta.accion(datos_para_accion)
                else:
                    carta.accion()
                if carta.tipo == 'accion':
                    self.__cartas_descarte.aniade_carta(carta)
                self.__cartas_jugadas_en_turno += 1
                self.__vista.update_interfaz()
                if self.chequea_ganador():
                    self.registrar_partida()
                    self.terminar_partida()
                if self.__cartas_jugadas_en_turno == 3:
                    self.terminar_turno()
            except Exception as e:
                print(f'{carta.mostrar_carta()} {e}')
        else:
            self.__vista.carta_no_es_jugable()
    
    def procesa_pedido(self, pedido, carta: Carta) -> list:
        if pedido == 'EsMiCumpleaños':
            return self.pedido_es_mi_cumpleanios(carta)
        elif pedido == 'CobradordDeDeuda':
            return self.pedido_cobrador_de_deuda(carta)
        elif pedido == 'NegocioFurtivo':
            return self.pedido_negocio_furtivo(carta)
        elif pedido == 'PasaPorLaSalida':
            return [self.__mazo]
        elif pedido == 'TratoForzoso':
            return self.pedido_trato_forzoso(carta)
        elif pedido == 'Renta':
            return self.pedido_renta(carta)
        elif pedido == 'RentaMulticolor':
            return self.pedido_renta_multicolor(carta)
        elif pedido == 'PropiedadComodin':
            return [self.elegir_color(carta, carta.color)]
        else:
            raise ValueError
    
    def pedido_es_mi_cumpleanios(self, carta: Carta) -> list[Carta]:
        cartas_para_pago = []
        jugadores_validos = self.jugadores_validos_para_cobro(2)
        for jugador in jugadores_validos:
            cartas_para_pago.extend(self.elegir_dinero(jugador, 2))
        return cartas_para_pago
    
    def pedido_roba_negocios(self, carta: Carta):
        jugadores_validos = self.roba_negocios_jugadores_validos()
        jugador_seleccionado = self.elegir_jugador(jugadores_validos)
        set_elegido = self.elegir_set(jugador_seleccionado)
        return set_elegido

    def roba_negocios_jugadores_validos(self):
        jugadores_validos = []
        for jugador in self.jugadores_sin_actual():
            sets_jugador = jugador.get_sets_completos_jugador()
            if len(sets_jugador) > 0:
                jugadores_validos.append(jugador)
        return jugadores_validos

    def pedido_cobrador_de_deuda(self, carta: Carta) -> list[Carta]:
        cartas_para_pago = []
        jugadores_validos = self.jugadores_validos_para_cobro(5)
        jugador_seleccionado = self.elegir_jugador(jugadores_validos)
        cartas_para_pago = self.elegir_dinero(jugador_seleccionado, 5)
        return cartas_para_pago
    
    def pedido_negocio_furtivo(self, carta: Carta) -> list[Carta]:
        propiedad_seleccionada = []
        jugador_seleccionado = self.elegir_jugador(self.jugadores_sin_actual())
        propiedad_seleccionada = self.elegir_propiedad(jugador_seleccionado) # hay que verificar que no esté en un set
        return [propiedad_seleccionada]

    def pedido_trato_forzoso(self, carta: Carta) -> list[Carta]:
        propiedad_propia = self.elegir_propiedad(carta.duenio) # se podría mandar una cadena que se muestre en el dialog
        jugadores_validos = self.jugadores_validos_trato_forzoso()
        jugador_seleccionado = self.elegir_jugador(jugadores_validos) # ej. 'Elija una de sus propiedades para intercambiar con otro jugador'
        propiedad_otro = self.elegir_propiedad(jugador_seleccionado) # Esta cadena se mostraría en el dialog en la interfaz
        return [propiedad_propia, propiedad_otro]

    def jugadores_validos_trato_forzoso(self):
        jugadores_validos = []
        for jugador in self.__jugadores:
            if jugador != self.__jugador_actual:
                if jugador.tiene_propiedades():
                    jugadores_validos.append(jugador)
        return jugadores_validos

    def pedido_renta(self, carta: Carta) -> list[Carta]:
        cartas_para_pago = []
        colores = self.colores_disponibles(carta)
        color = self.elegir_color(carta, colores)
        cantidad_a_cobrar = carta.duenio.get_valor_alquiler_color(color)
        jugadores_validos = self.jugadores_validos_para_cobro(cantidad_a_cobrar)
        for jugador in jugadores_validos:
            cartas_para_pago.extend(self.elegir_dinero(jugador, cantidad_a_cobrar))
        return cartas_para_pago

    def colores_disponibles(self, carta: Carta):
        colores_propiedades = []
        for color in carta.color:
            if carta.duenio.tiene_propiedades_color(color):
                colores_propiedades.append(color)
        return colores_propiedades

    def pedido_renta_multicolor(self, carta: Carta) -> list[Carta]:
        cartas_para_pago = []
        colores = self.colores_disponibles(carta)
        color = self.elegir_color(carta, colores)
        cantidad_a_cobrar = carta.duenio.get_valor_alquiler_color(color)
        jugadores_validos = self.jugadores_validos_para_cobro(cantidad_a_cobrar)
        jugador_elegido = self.elegir_jugador(jugadores_validos)
        cartas_para_pago.extend(self.elegir_dinero(jugador_elegido, cantidad_a_cobrar))
        return cartas_para_pago
    
    def jugadores_validos_para_cobro(self, valor_minimo: int):
        return [jugador for jugador in self.jugadores_sin_actual() if jugador.calcular_valor_banco() > valor_minimo]

    def elegir_jugador(self, jugadores_validos: list[Jugador]) -> Jugador:
        jugador = self.__vista.elegir_jugador(jugadores_validos)
        return jugador # tiene que salir un solo jugador de la vista

    def elegir_dinero(self, jugador_seleccionado: Jugador, dinero_necesario: int) -> list[Carta]:
        cartas = self.__vista.elegir_dinero(jugador_seleccionado.get_banco(), dinero_necesario)
        return cartas

    def elegir_propiedad(self, jugador: Jugador):
        propiedades = jugador.get_todas_las_propiedades()
        propiedad_elegida = self.__vista.elegir_propiedad(propiedades)
        return propiedad_elegida
    
    def elegir_color(self, carta: Carta, colores) -> str:
        color = self.__vista.elegir_color(colores)
        return color

    #def elegir_set(self, jugador_seleccionado):
    #    sets_completos = jugador_seleccionado.get_sets_completos()
    #    set = self.__vista.
############################################################################################################################
######################################## Termina código para jugar las cartas ##############################################
############################################################################################################################

############################################################################################################################
############################################# Código para terminar la partida ##############################################
############################################################################################################################

    def chequea_ganador(self) -> bool:
        for jugador in self.__jugadores:
            sets_jugador = jugador.get_sets_completos_jugador()
            if sets_jugador == 3:
                if self.__ganador is None:
                    self.__ganador = jugador
                elif isinstance(self.__ganador, Jugador):
                    self.__ganador = [self.__ganador]
                    self.__ganador.append(jugador)
                    break
        if self.__ganador is not None:
            return True
        return False
    
    def registrar_partida(self):
        conexion = Database().conexion()
        partida_dao = PartidaDaoImpl(conexion)
        partida = PartidaBDD()
        partida.id_partida = partida_dao.obtener_id_partida()
        if isinstance(self.__ganador, list):
            partida.id_ganador = None
        elif isinstance(self.__ganador, Jugador) and self.__ganador.datos_bdd is None:
            partida.id_ganador = None
        else:
            partida.id_ganador = self.__ganador.datos_bdd.get_id_jugador()
        partida_dao.agregar_partida(partida)
        for jugador in self.__jugadores:
            if jugador.datos_bdd is not None:
                partida_dao.registrar_jugador_en_partida(partida, jugador)
        conexion.close()
    
    def terminar_partida(self):
        self.__vista.muestra_resumen_y_sale()
        
############################################################################################################################
########################################### Termina código para ganar la partida ###########################################
############################################################################################################################

    def terminar_turno(self):
        # if self.__turno_actual == len(self.__jugadores) - 1:
        #     self.__turno_actual = 0
        # else:
        #     self.__turno_actual += self.__turno_actual + 1
        #     print(self.__turno_actual)
        self.__turno_actual = (self.__turno_actual + 1) % len(self.get_jugadores())
        self.__jugador_actual = self.__jugadores[self.__turno_actual]
        self.__cartas_jugadas_en_turno = 0
        tamanio_mano = len(self.__jugador_actual.get_mano())
        if tamanio_mano <= 5:
            self.dar_dos_cartas()
        elif tamanio_mano == 6:
            self.tomar_carta_mazo(self.__jugador_actual)
        elif tamanio_mano == 0:
            self.dar_cinco_cartas()
        self.__vista.finalizar_turno()
        self.__vista.update_interfaz()
    
    def volver(self):
        self.__vista.close()
        self.__main_menu.get_vista().show()
