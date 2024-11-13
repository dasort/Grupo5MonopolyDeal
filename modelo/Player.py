# nota: Esta clase deberia implementar toda la logica de un jugador DENTRO del juego. Es diferente a la que contiene el DAO
#no lo puse en español porque ya hay una clase jugador

class Player:
    def __init__ (self, nombre_jugador) #Aca habria que ver una forma de conectar que el jugador de esta clase sea el mismo jugador que se registro en la BDD
        self.nombre_jugador = nombre_jugador
        self._dinero = 1500 
        self._propiedades = [] # array donde se van a almacenar las propiedades del jugador actual
        self.__en_carcel = False
        self.__turno = False
        
    ##tirar dados### 
    def tirar_dados()