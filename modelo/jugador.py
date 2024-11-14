class Jugador:
    def __init__(self,nombre):
        self.__mano = []
        self.__banco = []
        self.__nombre = nombre
        self.__propiedades = []
    def tomar_carta(self, carta):
        self.__mano.append(carta)

    def jugar_carta(self, id_carta):
        for i, carta in enumerate(self.__mano):
            if carta.setid() == id_carta:
                carta_jugada = self.__mano.pop(i)
                # Aqui se puede aplicar la accion de las cartas
                return carta_jugada
        raise ValueError(f"No se encontró una carta con el ID {id_carta}")
    def agregar_a_propiedad(self, carta):
        self.__propiedades.append(carta)

    def agregar_a_banco(self, carta):
        self.__banco.append(carta)
        

    def mostrar_estado(self):
        print(" ")
        print(f"Nombre  del Jugador: {self.__nombre}")
        print(f"Mano")
        for mano in self.__mano:
                #print(" ")
                mano.mostrar_carta()
        print(f"Banco")
        for banco in self.__banco:
                #print(" ")
                banco.mostrar_carta()
        print(f"Propiedades")
        for propiedad in self.__propiedades:
                #print(" ")
                propiedad.mostrar_carta()