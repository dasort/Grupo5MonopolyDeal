from modelo.cartas.carta import Carta


class Propiedades(Carta):
    def __init__(self):
        # Inicialización de grupos y propiedades
        self.__cantidad_grupos = 0
        self.__propiedades = {
            "marron": {"lista": [], "grupos": 0},
            "celeste": {"lista": [], "grupos": 0},
            "rosa": {"lista": [], "grupos": 0},
            "naranja": {"lista": [], "grupos": 0},
            "rojo": {"lista": [], "grupos": 0},
            "amarillo": {"lista": [], "grupos": 0},
            "verde": {"lista": [], "grupos": 0},
            "azul": {"lista": [], "grupos": 0},
            "servicio": {"lista": [], "grupos": 0},
            "ferrocarril": {"lista": [], "grupos": 0}
            }

    def agregar_elemento(self, elemento: Carta):
        diccionario = {"sublista": [], "numero": 0}
        

        if elemento.color in self.__propiedades:
            # Inicializa si la lista está vacía
            if not self.__propiedades[elemento.color]["lista"]:
                print("Inicializando primera sublista")
                diccionario["sublista"].append(elemento)
                diccionario["numero"] += 1
                self.__propiedades[elemento.color]["lista"].append(diccionario)
                self.__cantidad_grupos = self.contar_grupos(self.__propiedades[elemento.color]["lista"])
                return

            # Verifica si todas las sublistas están completas
            todas_completas = all(
                (cartas["numero"] >= 3 and elemento.color not in ["servicio", "ferrocarril"]) or
                (cartas["numero"] >= 4 and elemento.color in ["servicio", "ferrocarril"])
                for cartas in self.__propiedades[elemento.color]["lista"]
            )

            # Intenta agregar el elemento a una sublista existente
            for cartas in self.__propiedades[elemento.color]["lista"]:
                # Caso 1: Sublista incompleta y no es servicio/ferrocarril
                if cartas["numero"] < 3 and elemento.color not in ["servicio", "ferrocarril"]:
                    cartas["sublista"].append(elemento)
                    cartas["numero"] += 1
                    self.__propiedades[elemento.color]["grupos"] = self.contar_grupos(self.__propiedades[elemento.color]["lista"])
                    self.contar()
                    #self.__cantidad_grupos = self.contar_grupos(self.__propiedades[elemento.color]["lista"])
                    return  # Salimos después de agregar

                # Caso 2: Sublista incompleta y es servicio/ferrocarril
                if cartas["numero"] < 4 and elemento.color in ["servicio", "ferrocarril"]:
                    cartas["sublista"].append(elemento)
                    cartas["numero"] += 1
                    self.__propiedades[elemento.color]["grupos"] = self.contar_grupos(self.__propiedades[elemento.color]["lista"])
                    self.contar()
                    
                    return  # Salimos después de agregar

            # Si todas las sublistas están completas, crea una nueva
            if todas_completas:
                print("Creando nueva sublista porque todas están completas")
                diccionario["sublista"].append(elemento)
                diccionario["numero"] += 1
                self.__propiedades[elemento.color].append(diccionario)
                self.__propiedades[elemento.color]["grupos"] = self.contar_grupos(self.__propiedades[elemento.color]["lista"])
                self.contar()

    def quitar_propiedad(self, carta: Carta):
        if carta.color in self.__propiedades:
            lista = self.__propiedades[carta.color]['lista']
            lista["sublista"].remove(carta)
            lista["numero"] -= 1
            self.__propiedades[carta.color] = self.ordenar_listas(self.__propiedades[carta.color]["lista"])
            self.__propiedades[carta.color]["grupos"] = self.contar_grupos(self.__propiedades[carta.color]["lista"])
        else:
            raise IndexError('Error en quitar_propiedad')

    def ordenar_listas(self, listas):
        elementos_faltantes = []
        nuevas_listas = []
        for sublista in listas:
            if isinstance(sublista, dict):
                if sublista["numero"] < 3:
                    elementos_faltantes.extend(sublista["sublista"])
                else:
                    nuevas_listas.append(sublista)
            else:
                raise ValueError("Se esperaba un diccionario en las sublistas.")

        while elementos_faltantes:
            nueva_sublista = {"sublista": elementos_faltantes[:3], "numero": len(elementos_faltantes[:3])}
            nuevas_listas.append(nueva_sublista)
            elementos_faltantes = elementos_faltantes[3:]

        return nuevas_listas

    def contar_grupos(self, lista):
        grupos = 0
        for sublista in lista:
            
            if (sublista["numero"] == 3 and sublista["sublista"][0].color not in ["servicio", "ferrocarril"]) or sublista["numero"] == 4:
                #print(f"Contando: {sublista["numero"]}")
                grupos += 1
        return grupos
    
    def contar(self):
        # Inicializamos el contador de grupos
        total_grupos = 0

        # Recorremos cada color y sus propiedades en el diccionario
        for propiedades in self.__propiedades.values():
            # Sumamos el valor de "grupos" en cada color
            total_grupos += propiedades["grupos"]
        print(f" Grupos totales contados: {total_grupos}")
        # Devolvemos el total de los grupos
        self.__cantidad_grupos =  total_grupos
        
    def mostrar_propiedades(self):
        print("===== PROPIEDADES =====")
        # Recorremos el diccionario de colores
        for color, datos in self.__propiedades.items():
            print(f"Color: {color.capitalize()}, GRUPOS: {datos["grupos"]}")

            # Recorremos la lista de cada color
            for elemento in datos["lista"]:
                if isinstance(elemento, dict):  # Si el elemento es una lista
                    print(f"  Es una sublista: {elemento["numero"]}")
                    
                    for i in elemento["sublista"]:
                        print(f"  Lista - {i.id}, {i.color} ")
                    # Llamamos a la función recursiva para recorrer la sublista
                else:
                    pass
                    #print(f"  - {elemento.id}, {elemento.color}")  # Si es un objeto, mostramos su id
        print(f"Cantidad de grupos: {self.__cantidad_grupos}")
        print("-" * 30)  # Separador para cada color
        
    @property
    def propiedades(self):
        return self.__propiedades
    
    def get_grupos(self):
        return self.__cantidad_grupos

    def get_cartas_propiedades(self) -> list[Carta]:
        cartas = []
        for color in self.__propiedades.keys():
            lista = self.__propiedades[color]['lista'] # lista de diccionarios
            for dicc in lista:
                cartas.extend(dicc['sublista']) # lista de cartas
        return cartas

    def hay_propiedad(self) -> bool:
        propiedades = self.get_cartas_propiedades()
        if propiedades:
            return True
        return False

    def hay_propiedad_color(self, color: str) -> bool:
        cartas = self.get_cartas_propiedades()
        colores = [carta.color for carta in cartas]
        if color in colores:
            return True
        return False
        
    __maximo_cartas_por_set = {
        "marron": 2,
        "azul": 2,
        "servicio": 2,
        "celeste": 3,
        "rojo": 3,
        "naranja": 3,
        "amarillo": 3,
        "rosa": 3,
        "verde": 3,
        "ferrocarril": 4
    }

    __valor_alquiler_por_set = {
        "marron": [1, 2],
        "azul": [3, 8],
        "servicio": [1, 2],
        "celeste": [1, 2, 3],
        "rojo": [2, 3, 6],
        "naranja": [1, 3, 5],
        "amarillo": [2, 4, 6],
        "rosa": [1, 2, 4],
        "verde": [2, 4, 7],
        "ferrocarril": [1, 2, 3, 4]
    }

    def get_sets_completos(self) -> list:
        sets_completos = list()
        
        for color in self.__propiedades.keys():
            lista = self.__propiedades[color]['lista'] # lista de diccionarios
            for dicc in lista:
                set_propiedades = dicc['sublista']
                if len(set_propiedades) == self.__maximo_cartas_por_set[color]:
                    sets_completos.append(set_propiedades)
        return sets_completos
    
    def get_sets(self):
        sets = list()

        for color in self.__propiedades.keys():
            lista = self.__propiedades[color]['lista'] # lista de diccionarios
            for dicc in lista:
                set_propiedades = dicc['sublista']
                sets.append(set_propiedades)
        return sets
    
    def cantidad_de_sets_completos(self) -> int:
        sets_completos = self.get_sets_completos()
        return len(sets_completos)

    def get_valor_alquiler(self, color: str) -> int:
        sets_del_color = []
        lista = self.__propiedades[color]['lista'] # lista de diccionarios
        for dicc in lista:
            sets_del_color.append(dicc['sublista']) # lista de cartas
        sets_del_color.sort(key=lambda x: len(x), reverse=True)
        mayor_set_del_color = sets_del_color[0]
        valor_alquiler = self.__valor_alquiler_por_set[color][len(mayor_set_del_color) - 1]
        return valor_alquiler
        # primero se accede al color correcto en el diccionario valor_alquiler_por_set, luego se accede a la posición de la
        # lista que tiene un índice igual a la cantidad de propiedades en el set. Se le resta uno porque el primer índice
        # es 0 y la mínima cantidad es 1

    def accion(self) -> None:
        pass

    def es_jugable(self):
        pass
