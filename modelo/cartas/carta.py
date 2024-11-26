from abc import ABC, abstractmethod


class Carta(ABC):
    '''Clase abstracta que sirve de base para las cartas de acción, propiedad y dinero.'''
    def __init__(self, id_carta: int, nombre: str, tipo: str, valor: int, path_a_imagen: str, path_a_queHace: str) -> None:
        self._id_carta = id_carta
        self._nombre = nombre
        self._tipo = tipo
        self._valor = valor
        self._path_a_imagen = path_a_imagen
        self._path_a_queHace = path_a_queHace
        self._duenio: Jugador = None

    @property
    def id(self) -> int:
        '''El id de la carta diferencia las instancias de las cartas aunque tengan la misma implementación.'''
        return self._id_carta
    
    @id.setter
    def id(self, id: int) -> None:
        self._id_carta = id
    
    @property
    def nombre(self) -> str:
        '''Nombre de la carta.'''
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre
    
    @property
    def tipo(self) -> str:
        '''El tipo de la carta puede ser de propiedad, dinero o acción. Representa la categoría de la carta.'''
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo: str) -> None:
        self._tipo = tipo
    
    @property
    def valor(self) -> int:
        '''El valor determina la cantidad de dinero que vale la carta al ser usada en el banco o para transacciones.'''
        return self._valor
    
    @valor.setter
    def valor(self, valor: int) -> None:
        self._valor = valor

    @property
    def path_a_imagen(self) -> str:
        '''Es el path de la imagen que ilustra la carta.'''
        return self._path_a_imagen
    
    @path_a_imagen.setter
    def path_a_imagen(self, path_a_imagen: str) -> None:
        self._path_a_imagen = path_a_imagen
    
    @property
    def path_a_queHace(self) -> str:
        '''Es el path de la imagen que explica el funcionamiento de este tipo de cartas.'''
        return self._path_a_queHace
    
    @path_a_queHace.setter
    def path_a_queHace(self, path_a_queHace: str) -> None:
        self._path_a_queHace = path_a_queHace
    
    @property
    def duenio(self):
        return self._duenio
    
    @duenio.setter
    def duenio(self, duenio):
        self._duenio = duenio

    # sobrecargar en clases hijas que lo requieran (accion, propiedad de más de un color)
    def informacion_para_accion(self) -> str | None:
        '''Devuelve una cadena que especifica la información que necesita la carta para realizar su acción.\n
        En caso de que la carta no tenga una acción asociada (ej. cartas de propiedad comunes o cartas de dinero) devuelve None.'''
        return None

    def accion(self) -> None:
        '''Ejecuta la acción que le corresponde a la carta.'''
        self.duenio.sacar_de_mano(self)
    
    def mostrar_carta(self) -> None:
        '''Representación de la carta como cadena.'''
        print("Carta")
        print(f"ID: {self.id}") 
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Valor: {self.valor}")
