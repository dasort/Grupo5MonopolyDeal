from typing import Callable


class Carta:
    def __init__(self) -> None:
        self.__id_carta: int = None
        self.__nombre: str = None
        self.__accion: Callable = None
        self.__tipo: str = None
        self.__valor: int = None
        self.__color: str | list[str] = None
        self.__path_a_imagen: str = None
        self.__path_a_queHace: str = None

    @property
    def id(self) -> int:
        '''El id de la carta duferencia las instancias de las cartas aunque tengan la misma implementación.'''
        return self.__id_carta
    
    @id.setter
    def id(self, id: int) -> None:
        self.__id_carta = id
    
    @property
    def nombre(self) -> str:
        '''Nombre de la carta.'''
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self.__nombre = nombre
    
    @property
    def accion(self) -> Callable:
        '''La acción es una función que representa el efecto de la carta cuando es jugada.\n
        Solo existe en las cartas de acción.'''
        return self.__accion
    
    @accion.setter
    def accion(self, accion: Callable) -> None:
        self.__accion = accion
    
    @property
    def tipo(self) -> str:
        '''El tipo de la carta puede ser de propiedad, dinero o acción. Representa la categoría de la carta.'''
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo: str) -> None:
        self.__tipo = tipo
    
    @property
    def valor(self) -> int:
        '''El valor determina la cantidad de dinero que vale la carta al ser usada en el banco o para transacciones.'''
        return self.__valor
    
    @valor.setter
    def valor(self, valor: int) -> None:
        self.__valor = valor
    
    @property
    def color(self) -> str | list[str]:
        return self.__color

    @color.setter
    def color(self, color: str | list[str]):
        self.__color = color

    @property
    def path_a_imagen(self) -> str:
        '''Es el path de la imagen que ilustra la carta.'''
        return self.__path_a_imagen
    
    @path_a_imagen.setter
    def path_a_imagen(self, path_a_imagen: str) -> None:
        self.__path_a_imagen = path_a_imagen
    
    @property
    def path_a_queHace(self) -> str:
        '''Es el path de la imagen que explica el funcionamiento de este tipo de cartas.'''
        return self.__path_a_queHace
    
    @path_a_queHace.setter
    def path_a_queHace(self, path_a_queHace: str) -> None:
        self.__path_a_queHace = path_a_queHace
    
    def mostrar_carta(self) -> None:
        print("Carta")
        print(f"ID: {self.id}") 
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Valor: {self.valor}")
        if self.tipo == 'propiedad':
            print(f"Color: {self.color}")
        elif self.tipo == 'accion':
            print(f"Accion: {self.accion.__name__}")
