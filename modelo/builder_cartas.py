from abc import ABC, abstractmethod
from typing import Callable
if __name__ == '__main__':
    from carta import Carta
else:
    from modelo.carta import Carta


class BuilderCarta(ABC):
    
    @property
    @abstractmethod
    def carta(self) -> None:
        pass
    @abstractmethod
    def produce_id(self, id: int) -> None:
        pass
    @abstractmethod
    def produce_tipo(self, tipo: str) -> None:
        pass
    @abstractmethod
    def produce_nombre(self, nombre: str) -> None:
        pass
    @abstractmethod
    def produce_valor(self, valor: int) -> None:
        pass
    @abstractmethod
    def produce_accion(self, accion: Callable) -> None:
        pass
    @abstractmethod
    def produce_color(self, color: str | list[str]) -> None:
        pass
    @abstractmethod
    def produce_path_a_imagen(self, path_a_imagen: str) -> None:
        pass
    @abstractmethod
    def produce_path_a_queHace(self, path_a_queHace: str) -> None:
        pass


class CrearBuilderCarta(BuilderCarta):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._carta = Carta()

    @property
    def carta(self) -> Carta:
        carta = self._carta
        self.reset()
        return carta
    
    def produce_id(self, id: int) -> None:
        self._carta.id = id
        
    def produce_tipo(self, tipo: str) -> None:
        self._carta.tipo = tipo
    
    def produce_nombre(self, nombre: str) -> None:
        self._carta.nombre = nombre
    
    def produce_valor(self, valor: int) -> None:
        self._carta.valor = valor
    
    def produce_accion(self, accion: Callable) -> None:
        if callable(accion) or accion is None:
            self._carta.accion = accion
        else:
            raise ValueError("La acción debe ser una función.")
    
    def produce_color(self, color: str | list[str]) -> None:
        self._carta.color = color
    
    def produce_path_a_imagen(self, path_a_imagen: str) -> None:
        self._carta.path_a_imagen = path_a_imagen
    
    def produce_path_a_queHace(self, path_a_queHace: str) -> None:
        self._carta.path_a_queHace = path_a_queHace


class Director:
    def __init__(self):
        self.__builder = None
    
    # Get y Set 
    @property
    def builder(self) -> BuilderCarta:
        return self.__builder
    @builder.setter
    def builder(self, builder: BuilderCarta) -> None:
        self.__builder = builder
    
    # Creador de los tipos de Cartas
    
    # Accion, Descripcion, Tipo, ID  
    def carta_accion(self, id: int, nombre: str, tipo: str, accion: Callable, valor: int, path_a_imagen: str, path_a_queHace: str) ->None:
        self.__carta_basica(id, nombre, tipo, valor, path_a_imagen, path_a_queHace)
        self.__builder.produce_accion(accion)
        
    # Descripcion, Tipo, ID  
    def carta_propiedad(self, id: int, nombre: str, tipo: str, valor: int, color: str | list[str], path_a_imagen: str, path_a_queHace: str) ->None:
        self.__carta_basica(id, nombre, tipo, valor, path_a_imagen, path_a_queHace)
        self.__builder.produce_color(color)

    # Tipo, ID  
    def carta_dinero(self, id: int, nombre: str, tipo: str, valor: int, path_a_imagen: str, path_a_queHace: str) ->None:
        self.__carta_basica(id, nombre, tipo, valor, path_a_imagen, path_a_queHace)

    def __carta_basica(self, id: int, nombre: str, tipo: str, valor: int, path_a_imagen: str, path_a_queHace: str) -> None:
        self.__builder.produce_id(id)
        self.__builder.produce_nombre(nombre)
        self.__builder.produce_tipo(tipo)
        self.__builder.produce_valor(valor)
        self.__builder.produce_path_a_imagen(path_a_imagen)
        self.__builder.produce_path_a_queHace(path_a_queHace)
