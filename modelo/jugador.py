from modelo.propiedades import Propiedades
from modelo.cartas.carta import Carta
from modelo.base_de_datos.jugador_dao.jugador_bdd import JugadorBDD


class Jugador:
    def __init__(self, nombre: str = None, avatar: str = None):
        self.__avatar = avatar
        self.__nombre = nombre
        self.__listas = {"Mano":[],"Banco":[],"Propiedades":Propiedades()}
        self.__datos_bdd: JugadorBDD = None
        
    def agregar_a_mano(self, cartas: Carta):
        self.__listas["Mano"].append(cartas)

    def agregar_a_banco(self, carta: Carta):
        self.__listas["Banco"].append(carta)

    def agregar_a_propiedades(self, carta: Carta):
        # Usa el método de la clase Propiedades para agregar la carta
        self.__listas["Propiedades"].agregar_a_propiedades(carta)
        
    def tomar_carta(self, cartas):
        if isinstance(cartas, (list)):
            for carta in cartas:
                carta.duenio = self
            self.__listas["Mano"].extend(cartas)
        else:
            carta.duenio = self
            self.__listas["Mano"].extend([cartas])
    
    def calcular_valor_banco_propiedades(self) -> int:
        '''Calcula el valor de las cartas en el banco y la lista de propiedades del jugador.\n
        Necesario porque un jugador no puede pagarle a otro si no tiene el valor necesario.'''
        propiedades = self.get_propiedades().get_cartas_propiedades()
        banco = self.get_banco()
        valor_total = 0
        for carta in propiedades + banco:
            valor_total += carta.valor
        return valor_total
    
    def elegir_carta(self, lista: str, carta: Carta):
        # Obtener la lista de cartas
        try:
            if lista != "Propieadades":
                cartas_lista = self.__listas[lista]
                # Intentar remover la carta de la lista especificada
                cartas_lista.remove(carta)
                return carta
            else:
                # Si la lista es "Propiedades", usar el método de la clase Propiedades
                self.__listas["Propiedades"].eliminar_carta(carta)
                return carta
        
        except ValueError as e:
            print(f"Error: {e}")
            raise  # Re-lanza el error para ser manejado a un nivel superior si es necesario
        
    # Métodos para obtener las cartas de las listas
    def get_mano(self) -> list[Carta]:
        return self.__listas["Mano"]
    
    def get_banco(self) -> list[Carta]:
        return self.__listas["Banco"]
    
    def get_propiedades(self) -> dict:
        return self.__listas["Propiedades"].propiedades
    
    def get_avatar(self):
        return self.__avatar
    
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre) -> None:
        self.__nombre = nombre
    
    def set_avatar(self, avatar) -> None:
        self.__avatar = avatar
        
    def get_objeto_propiedad(self) -> Propiedades:
        return self.__listas["Propiedades"]

    @property
    def datos_bdd(self) -> JugadorBDD:
        return self.__datos_bdd
    
    @datos_bdd.setter
    def datos_bdd(self, datos: JugadorBDD):
        self.__datos_bdd = datos

    def remover_propiedad(self, carta: Carta):
        self.get_objeto_propiedad().quitar_propiedad(carta)