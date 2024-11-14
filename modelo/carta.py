class Carta:
    def __init__(self) -> None:
        self.id_carta = None
        self.nombre = None
        self.descripcion = None
        self.accion = None
        self.tipo = None
        self.valor = None   
    def getTipo(self):
        return self.tipo
    def getAccion(self):
        return self.accion
    def getId(self):
        return self.id_carta
    def mostrar_carta(self):
        print("Carta")
        #print(f" Nombre: {self.nombre}")
        if self.descripcion != None:
            print(f"Descripcion: {self.descripcion}")
        print(f"Valor: {self.valor}")
        print(f"Tipo: {self.tipo}")
        print(f"ID: {self.id_carta}") 
        pass  