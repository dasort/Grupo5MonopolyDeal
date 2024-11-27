from PyQt6.QtWidgets import QDialog, QLabel, QListWidget, QVBoxLayout, QPushButton, QListWidgetItem
from PyQt6.QtCore import Qt

class ElegirDialog(QDialog):
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        self._seleccion = None
        
        self._layout_principal = QVBoxLayout(self)

        self._lbl = QLabel()
        self._layout_principal.addWidget(self._lbl)

        self._lista = QListWidget()
        self._layout_principal.addWidget(self._lista)

        self._boton_aceptar = QPushButton('Confirmar Selección')
        self._boton_aceptar.clicked.connect(self.aceptar)
        self._layout_principal.addWidget(self._boton_aceptar)
    
    def aceptar(self):
        
        self._seleccion = self._lista.currentItem()
        self._seleccion = self._seleccion.text()
        if self._seleccion:
            self.accept()
    
    def get_valor(self):
        return self._seleccion
    
    def close_event(self, event):
        event.ignore()

class ElegirColorDialog(ElegirDialog):
    
    def __init__(self, colores: list[str], parent = None) -> None:
        super().__init__(parent)

        self.setWindowTitle('Elegir Color')

        self._lbl.setText('Seleccione un color para la carta:')

        self._lista.addItems(colores)

class ElegirPropiedadDialog(ElegirDialog):
    def __init__(self, propiedades: list, parent=None) -> None:
        super().__init__(parent)
        
        self.__propiedades = propiedades
        
        self.setWindowTitle('Elegir Propiedad')

        self._lbl.setText('Seleccione una propiedad:')

        for propiedad in self.__propiedades:
            mostrar = propiedad.nombre + ' - ' + str(propiedad.id)
            self._lista.addItem(mostrar)
        
    def aceptar(self):
        self._seleccion = self._lista.currentItem()
        self._seleccion = self._seleccion.text()
        if self._seleccion:
            nombre, id = self._seleccion.split(' - ')
            id = int(id)
            for propiedad in self.__propiedades:
                if id == propiedad.id:
                    self._seleccion = propiedad
                    self.accept()
                    return
    
class ElegirJugadorDialog(ElegirDialog):
    def __init__(self, jugadores: list, parent=None) -> None:
        super().__init__(parent)
        
        self.__jugadores = jugadores
        
        self.setWindowTitle('Elegir Jugador')

        self._lbl.setText('Seleccione un jugador:')

        for jugador in self.__jugadores:
            mostrar = jugador.nombre
            self._lista.addItem(mostrar)
        
    def aceptar(self):
        self._seleccion = self._lista.currentItem()
        self._seleccion = self._seleccion.text()
        if self._seleccion:
            for jugador in self.__jugadores:
                if jugador.nombre == self._seleccion:
                    self._seleccion = jugador
                    self.accept()
                    return

class ElegirDineroDialog(ElegirDialog):
    def __init__(self, cartas: list, minimo,  parent=None) -> None:
        super().__init__(parent)
        
        self.__minimo = minimo
        self.__cartas = cartas
        
        self.setWindowTitle('Elegir Cartas Para Pagar')

        self._lbl.setText(f'Selecciona cartas que sumen al menos: {self.__minimo}')

        self._lista.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        
        for carta in self.__cartas:
            aniadir = QListWidgetItem(carta.nombre)
            aniadir.setData(Qt.ItemDataRole.UserRole, carta)
            self._lista.addItem(aniadir)
        
    def aceptar(self):
        cartas = self._lista.selectedItems()
        self._seleccion = []
        for carta in cartas:
            self._seleccion.append(carta.data(Qt.ItemDataRole.UserRole))
        if self._seleccion:
            suma = 0
            for carta in self._seleccion:
                suma = suma + carta.valor
            if suma >= self.__minimo:
                self.accept()
            else:
                self._lbl.setText(f"El valor total de las cartas seleccionadas es {suma}, debe ser al menos {self.__minimo}.")
    