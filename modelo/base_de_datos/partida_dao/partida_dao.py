from abc import ABC, abstractmethod


class PartidaDAO(ABC):

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
    def actualizar_ganador_partida(Self):
        pass
    