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
    def jugar_carta(self, jugador: Jugador):
        carta = self.elijir_carta(jugador)
        # Verificar si la carta puede ser jugada
        if carta.tipo == "Accion":
                self.ejecutar_accion(carta)
                self.__mesa = carta
        elif carta.tipo == "Propiedad":
            jugador.agregar_a_propiedad(carta)
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
