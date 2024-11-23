from modelo.carta.carta import Carta
class Propiedades(Carta):
    # colores = ["Azul","Verde","Rojo","Amarillo","Rosa"] 
    def __init__(self):
        # Diccionario para almacenar propiedades por color
        self.__propiedades = {
            "Rojo": [],
            "Azul": [],
            "Amarillo": [],
            "Verde": [],
            "Rosa": []
        }

    def agregar_a_propiedades(self, carta: Carta):
        # Agregar la carta al color correspondiente
        if carta.color in self.__propiedades:
            self.__propiedades[carta.color].append(carta)
        else:
            print(f"Color no reconocido: {carta.color}")

    def mostrar_propiedades(self):
        print("\nPROPIEDADES")
        for color, cartas in self.__propiedades.items():
            print(f"{color}:")
            for carta in cartas:
                carta.mostrar_carta()  # Metodo de la clase Carta
            print("---")