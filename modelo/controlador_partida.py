from modelo.jugador import Jugador
from modelo.mazo_de_cartas import MazoDeCartas
from modelo.mazo_de_descarte import MazoDeDescarte
from modelo.cartas.carta import Carta


class ControladorPartida:
    def __init__(self, jugadores: list[Jugador]):
        self.__vista = Vista(self) # poner el nombre de la vista correcto
        self.__jugadores = jugadores  # Instancias de la clase Jugador
        self.__mazo = MazoDeCartas()
        self.__mesa = None
        self.__cartas_descarte = MazoDeDescarte()  # Pila de descarte
        self.__turno_actual = 0  
        self.repartir_cartas()

    # Reparte 5 cartas a cada jugador
    def repartir_cartas(self):
        for jugador in self.__jugadores: # Obtiene una lista de 5 cartas
            jugador.tomar_carta(self.__mazo.dar_cartas(5))
    
    # Toma una carta aleartoria del mazo eliminandola
    def tomar_carta_mazo(self,jugador: Jugador):
        jugador.tomar_carta(self.__mazo.__dar_carta())
    
    def jugar_carta(self, carta: Carta) -> None:
        # Verificar si la carta puede ser jugada
        pedido = carta.informacion_para_accion()
        if pedido is not None:
            datos_para_accion = self.procesa_pedido(pedido, carta)
        carta.accion(datos_para_accion)
    
    def procesa_pedido(self, pedido, carta: Carta) -> list:
        if pedido == 'EsMiCumpleaños':
            cartas_para_pago = []
            jugadores_validos = self.jugadores_validos_para_cobro(2)
            for jugador in self.__jugadores:
                if jugador is not carta.duenio:
                    cartas_para_pago.extend(self.elegir_dinero(jugador, 2))
            return cartas_para_pago
        elif pedido == 'CobradordDeDeuda':
            cartas_para_pago = []
            jugadores_validos = self.jugadores_validos_para_cobro(5)
            jugador_seleccionado = self.elegir_jugador(carta.duenio, jugadores_validos)
            cartas_para_pago = self.elegir_dinero(jugador_seleccionado, 5)
            return cartas_para_pago
        elif pedido == 'NegocioFurtivo':
            propiedad_seleccionada = []
            jugador_seleccionado = self.elegir_jugador(carta.duenio, self.__jugadores)
            propiedad_seleccionada = self.elegir_propiedad(jugador_seleccionado) # hay que verificar que no esté en un set
            return [propiedad_seleccionada]
        elif pedido == 'PasaPorLaSalida':
            return [self.__mazo]
        elif pedido == 'TratoForzoso':
            propiedad_propia = self.elegir_propiedad(carta.duenio) # se podría mandar una cadena que se muestre en el dialog
            jugador_seleccionado = self.elegir_jugador(carta.duenio) # ej. 'Elija una de sus propiedades para intercambiar con otro jugador'
            propiedad_otro = self.elegir_propiedad(jugador_seleccionado) # Esta cadena se mostraría en el dialog en la interfaz
            return [propiedad_propia, propiedad_otro]
        elif pedido == 'RentaDoble':
            pass
        elif pedido == 'RentaMulticolor':
            pass
        elif pedido == 'PropiedadComodin':
            return [self.elegir_color(carta.color)] # metodo en la vista que le permite al jugador elegir entre los colores de la carta
        else:
            raise ValueError
    
    def jugadores_validos_para_cobro(self, valor_minimo: int):
        return [jugador for jugador in self.__jugadores if jugador.calcular_valor_banco_propiedades() > valor_minimo]

    def elegir_jugador(self, jugador_excluido: Jugador, jugadores_validos: list[Jugador]) -> Jugador:
        jugadores = []
        for jugador in jugadores_validos:
            if jugador is not jugador_excluido:
                jugadores.append(jugador)
        dialogo = self.__vista.dialog_pedir_jugador(jugadores)
        dialogo.exec()
        return dialogo.jugador_seleccionado

    def elegir_dinero(self, jugador_seleccionado: Jugador, dinero_necesario: int) -> list[Carta]:
        dialogo = self.__vista.dialog_pedir_dinero(jugador_seleccionado.get_banco(), dinero_necesario)
        dialogo.exec()
        return dialogo.cartas_seleccionadas

    def elegir_propiedad(self, jugador: Jugador):
        propiedades = jugador.get_objeto_propiedad().get_cartas_propiedades()
        dialogo = self.__vista.dialog_pedir_propiedad(propiedades)
        dialogo.exec()
        return dialogo.propiedad_seleccionada
    
    def elegir_color(self, lista_colores: list[str]) -> str:
        dialogo = self.__vista.dialog_pedir_color(lista_colores)
        dialogo.exec()
        return dialogo.color_seleccionado

    # Elije la una carta de la mano esta funcion necesita cambios pero es la idea de lo que hay que hacer
    def  elijir_carta(self,jugador: Jugador) -> Carta:
        print("Elije la Carta")
        jugador.mostrar_mano()
        # Implementacion sin interfaz
        carta_id = int(input("Dame el ID de la carta a Jugar: "))
        return jugador.jugar_carta(carta_id)
    
    # Saca una cantidad esacta de cartas del mazo
    def sacar_cartas(self, cantidad: int):
        #self.__mazo = random.shuffle(self.__mazo)
        cartas = self.__mazo[:cantidad]
        self.__mazo = self.__mazo[cantidad:]
        return cartas
    
    #devulve el jugador actual segun el turno actual
    def jugador_actual(self):
        return self.__jugadores[self.__turno_actual]
    
    #devuelve el turno actual segun la posicion de la lista de jugadores
    def pasar_turno(self):
        if self.turno_actual + 1 >= len(self.__jugadores): 
            self.turno_actual = 0
        else: self.turno_actual += 1
        
    # devuelve el mazo de jugador en su turno
    def cargar_mazo_del_jugador_actual(self, cartas):
        jugador_actual = self.jugador_actual()
        jugador_actual.cargar_mazo(cartas)
        print(f"Mazo del jugador {jugador_actual.nombre()}: {jugador_actual.mostrar_mazo()}")
