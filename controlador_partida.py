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
                
    #retorna el mazo cargado con las cartas
    @property
    def mazo(self) -> MazoDeCartas:
        return self.__mazo
    
    # Reparte 5 cartas a cada jugador
    def repartir_cartas(self):
        for jugador in self.__jugadores:
            jugador.agregar_cartas(self.__mazo.dar_cartas(5))
        
    # Otra funcion que necesita cambios cuando se termine de hacer el mazo
    def jugar_carta(self, carta: Carta) -> None:
        # Verificar si la carta puede ser jugada
        pedido = carta.informacion_para_accion()
        if pedido is not None:
            datos_para_accion = self.procesa_pedido(pedido)
        carta.accion(datos_para_accion)
    
    def procesa_pedido(self, pedido) -> list:
        if pedido == 'EsMiCumpleaños':
            pass
        elif pedido == 'CobradordDeDeuda':
            pass
        elif pedido == 'NegocioFurtivo':
            pass
        elif pedido == 'PasaPorLaSalida':
            pass
        elif pedido == 'TratoForzoso':
            pass
        elif pedido == 'RentaDoble':
            pass
        elif pedido == 'RentaMulticolor':
            pass
        elif pedido == 'PropiedadComodin':
            pass
        else:
            raise ValueError
    
    def ejecutar_accion(self, carta):
        print("Ejecutando Accion: ")
        carta.accion(self.__jugadores)
        
    # Elije la una carta de la mano esta funcion necesita cambios pero es la idea de lo que hay que hacer
    def  elijir_carta(self,jugador: Jugador) -> Carta:
        print("Elije la Carta")
        jugador.mostrar_mano()
        # Implementacion sin interfaz
        carta_id = int(input("Dame el ID de la carta a Jugar: "))
        return jugador.jugar_carta(carta_id)
    
    #devulve el jugador actual segun el turno actual
    def jugador_actual(self):
        return self.__jugadores[self.__turno_actual]
    
    #devuelve el turno actual segun la posicion de la lista de jugadores
    def pasar_turno(self):
        if self.turno_actual + 1 >= len(self.__jugadores): 
            self.turno_actual = 0
        else: self.turno_actual += 1
