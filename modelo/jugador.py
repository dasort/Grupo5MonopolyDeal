from propiedades import Propiedades
from modelo.carta.carta import Carta
class Jugador:
    def __init__(self,nombre,avatar: str):
        self.__avatar = avatar
        self.__nombre = nombre
        self.__listas = {"Mano":[],"Banco":[],"Propiedades":Propiedades()}
    def agregar_a_mano(self, carta: Carta):
        self.__listas["Mano"].append(carta)

    def agregar_a_banco(self, carta: Carta):
        self.__listas["Banco"].append(carta)

    def agregar_a_propiedades(self, carta: Carta):
        # Usa el método de la clase Propiedades para agregar la carta
        self.__listas["Propiedades"].agregar_a_propiedades(carta)
    def tomar_carta(self, cartas):
        if isinstance(cartas, (list)):
            self.__listas["Mano"].extend(cartas)
        else:
            self.__listas["Mano"].extend([cartas])
    
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
    def get_mano(self):
        return "Mano", self.__listas["Mano"]
    def get_banco(self):
        return "Banco",self.__listas["Banco"]
    def get_propiedades(self):
        return "Propiedades",self.__listas["Propiedades"].get_todas_las_cartas()
    def get_avatar(self):
        return self.__avatar
    
    @property
    def nombre (self):
        return self.__nombre
