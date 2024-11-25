from modelo.cartas.carta import Carta


class MazoDeDescarte:
    '''El mazo de descarte guarda las cartas de acción jugadas por los jugadores.
    '''
    def __init__(self) -> None:
        self.__descarte: list[Carta] = [] # se llena a medida que se juegan las cartas de acción
    
    def get_descarte(self) -> list[Carta]: # se usa cuando no se pueden robar suficientes cartas del mazo de cartas
        return self.__descarte

    def get_ultima_carta_jugada(self) -> Carta:
        '''Devuelve la última carta de acción jugada.
        '''
        return self.__descarte[0]

    def aniade_carta(self, carta: Carta) -> None:
        '''Recibe una carta jugada y la añade a la pila de descarte.
        '''
        self.__descarte.insert(0, carta) # añade la carta al principio de la lista (índice 0 siempre tiene la última carta de acción jugada)
