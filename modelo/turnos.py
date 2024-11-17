from abc import ABC,abstractmethod
#interfaz que va a dar el turno actual con su debido mazo

class Turnos(ABC):
    
    @abstractmethod
    def jugador_actual(self)-> None:
        pass
    @abstractmethod
    def pasar_turno(self)-> None:
        pass
    @abstractmethod
    def cargar_mazo_del_jugador_actual(self)-> None:
        pass