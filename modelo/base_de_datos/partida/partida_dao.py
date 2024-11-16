from abc import ABC, abstractmethod



class partida_dao(ABC):
    @abstractmethod
    def agregar_partida(self):
        pass
    @abstractmethod
    def obtener_partida(self):
        pass
    @abstractmethod
    def eliminar_partida(self):
        pass
    @abstractmethod
    def actulizar_ganador_partida(Self):
        pass
    