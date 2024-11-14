from carta import Carta
from abc import ABC, abstractmethod
import random
class BuilderCarta(ABC):
    
    @property
    @abstractmethod
    def carta(self) -> None:
        pass
    @abstractmethod
    def produce_id(self) -> None:
        pass
    @abstractmethod
    def produce_tipo(self,tipo) -> None:
        pass
    @abstractmethod
    def produce_descripcion(self,descripcion) -> None:
        pass
    @abstractmethod
    def produce_valor(self,valor) -> None:
        pass
    @abstractmethod
    def produce_accion(self,accion) -> None:
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
    def produce_id(self,id) -> None:
        self._carta.id_carta = id
        
    def produce_tipo(self,tipo) -> None:
        self._carta.tipo = tipo
    
    def produce_descripcion(self,descripcion) -> None:
        self._carta.descripcion = descripcion
        self._carta.nombre = "Nombre de Carta"
    
    def produce_valor(self,valor) -> None:
        self._carta.valor = valor
    
    def produce_accion(self, accion) -> None:
        if callable(accion):
            self._carta.accion = accion
        else:
            raise ValueError("La acción debe ser una función.")

class Director:
    def __init__(self):
        self._builder = None
    
    # Get y Set 
    @property
    def builder(self) -> BuilderCarta:
        return self._builder
    @builder.setter
    def builder(self, builder: BuilderCarta) -> None:
        self._builder = builder
    
    # Creador de los tipos de Cartas
    
    # Accion, Descripcion, Tipo, ID  
    def carta_accion(self,accion,descripcion,tipo,id)-> None:
        self._builder.produce_id(id)
        self.builder.produce_accion(accion)
        self.builder.produce_descripcion(descripcion)
        self._builder.produce_tipo(tipo)
        self._builder.produce_valor(random.randint(1,3))
    # Descripcion, Tipo, ID  
    def carta_propiedad(self,descripcion,tipo,id)->None:
        self._builder.produce_id(id)
        self.builder.produce_descripcion(descripcion)
        self._builder.produce_tipo(tipo)
        self._builder.produce_valor(random.randint(1,5))
    # Tipo, ID  
    def carta_dinero(self,tipo,id)->None:
        self._builder.produce_id(id)
        self._builder.produce_tipo(tipo) 
        self._builder.produce_valor(random.randint(1,7))