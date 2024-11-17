from random import shuffle
from carta import Carta
from mazo_de_descarte import MazoDeDescarte


class MazoDeCartas:
    '''El mazo de cartas contiene todas las cartas que se usan en el juego.\n
    Permite dar cartas a los jugadores según la cantidad que se desee.
    '''
    
    def __init__(self, cartas: list[Carta]) -> None:
        self.__mazo = cartas # cartas comienza con todas las cartas que se usan en el juego
        shuffle(self.__mazo)
    
    def __dar_carta(self) -> Carta:
        '''Devuelve una carta del mazo.
        '''
        carta = self.__mazo.pop[0]
        return carta
    
    def __refrescar_mazo(self, descarte: MazoDeDescarte) -> None:
        '''Mezcla las cartas en la pila de descarte y se usan como mazo.
        '''
        self.__mazo = descarte.get_descarte()
        shuffle(self.__mazo)
    
    def dar_cartas(self, cantidad_a_devolver: int) -> list[Carta]:
        '''Devuelve la cantidad de cartas especificadas como parámetro.\n
        Mezcla la pila de descarte y lo usa como mazo si no hay suficientes cartas en el mazo.
        '''
        if cantidad_a_devolver > len(self.__mazo): # chequeo que hayan suficientes cartas en el mazo
            self.__refrescar_mazo()
        cartas = [self.__dar_carta() for _ in range(cantidad_a_devolver)] # crea una lista de cartas con la cantidad pedida
        return cartas
