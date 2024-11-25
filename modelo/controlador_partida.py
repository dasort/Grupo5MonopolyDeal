from modelo.jugador import Jugador
from modelo.mazo_de_cartas import MazoDeCartas
from modelo.mazo_de_descarte import MazoDeDescarte
from modelo.cartas.carta import Carta


class ControladorPartida:
    def __init__(self, jugadores: Jugador):
        # self.__vista = Vista(self) # poner el nombre de la vista correcto
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
    
    # Otra funcion que necesita cambios cuando se termine de hacer el mazo
    def jugar_carta(self, carta: Carta) -> None:
        # Verificar si la carta puede ser jugada
        pedido = carta.informacion_para_accion()
        if pedido is not None:
            datos_para_accion = self.procesa_pedido(pedido)
        carta.accion(datos_para_accion)
    
    def procesa_pedido(self, pedido) -> list:
        match pedido:
            case 'EsMiCumpleaños':
                pass
            case 'CobradordDeDeuda':
                pass
            case 'NegocioFurtivo':
                pass
            case 'PasaPorLaSalida':
                pass
            case 'TratoForzoso':
                pass
            case 'RentaDoble':
                pass
            case 'RentaMulticolor':
                pass
            case 'PropiedadComodin':
                pass
            case _:
                raise ValueError(f"Pedido desconocido: {pedido}")
            
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
