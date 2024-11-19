from jugador import Jugador
import random
from carta import Carta
class Controlador:
    def __init__(self, jugadores: Jugador):
        self.__jugadores = jugadores  # Instancias de la clase Jugador
        self.__mazo = []
        self.__mesa = None
        self.__cartas_descarte = []  # Pila de descarte
        self.__turno_actual = 0  
        self.repartir_cartas()
        
    #carga el mazo del jugador con una lista de cartas
    def cargar_mazo(self,cartas :Carta):
        self.__mazo.extend(cartas)
        
    #retorna el mazo cargado con las cartas
    def mostrar_mazo(self):
        return self.__mazo
    
    # Reparte 5 cartas a cada jugador
    def repartir_cartas(self):
        for jugador in self.__jugadores:
            cartas_a_repartir = self.sacar_cartas(5)  # Obtiene una lista de 5 cartas
            jugador.tomar_carta(cartas_a_repartir)
    
    # Toma una carta aleartoria del mazo eliminandola
    def tomar_carta_mazo(self,jugador: Jugador):
        carta = random.choice(self.__mazo)
        self.__mazo.remove(carta)
        jugador.tomar_carta(carta)
    
    # Otra funcion que necesita cambios cuando se termine de hacer el mazo
    def jugar_carta(self, jugador: Jugador, carta : Carta):
        # Verificar si la carta puede ser jugada
        print("Entro a jugar_carta")
        if carta.tipo == "Accion":
                self.ejecutar_accion(carta)
                self.__mesa = carta
        elif carta.tipo == "Propiedad":
            jugador.agregar_a_propiedades(carta)
            print("Se agrego una propiedad")
        elif carta.tipo == "Dinero":
            jugador.agregar_a_banco(carta)
            print("Se agrego al banco")
            
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
