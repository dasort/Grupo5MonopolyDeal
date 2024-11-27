from vistas.vista_crear_partida import CrearPartida
from controladores.controlador_partida import ControladorPartida
from controladores.controlador_iniciar_sesion import Controlador_iniciar_sesion
from modelo.jugador import Jugador


class ControladorCrearPartida:
    def __init__(self, main_menu):
        self.__main_menu = main_menu
        self.__vista = CrearPartida(self)
        self.__vista.show()

    def volver(self):
        self.__vista.hide()
        self.__main_menu.get_vista().show()

    def abre_iniciar_sesion(self, jugador, jugadores):
        self.__vista.hide()
        var = Controlador_iniciar_sesion(jugador, jugadores, self.__main_menu, self)

    def cambio_cant_jugadores(self):
        if len(self.__vista.jugadores) >= self.__vista.minimo_jugadores:
            if len(self.__vista.jugadores) == self.__vista.maximo_jugadores:
                self.__vista.agregar_jugador_boton.setEnabled(False)
                self.__vista.shortcut1.setEnabled(False)
            else:
                self.__vista.agregar_jugador_boton.setEnabled(True)
                self.__vista.crear_partida_boton.setEnabled(True)
                self.__vista.aviso_label.hide()
                self.__vista.shortcut1.setEnabled(True)
        else:
            if len(self.__vista.jugadores) == 1:
                self.__vista.quitar_jugador_boton.setEnabled(True)
                self.__vista.crear_partida_boton.setEnabled(False)
                self.__vista.aviso_label.show()
                self.__vista.shortcut2.setEnabled(True)
            else:
                self.__vista.quitar_jugador_boton.setEnabled(False)
                self.__vista.shortcut2.setEnabled(False)

    def quitar_jugador(self):
        if self.__vista.jugadores:
            jugador = self.__vista.jugadores.pop()
            jugador["widget_jugador"].deleteLater()
            jugador["layout_jugador"].deleteLater()
            jugador["info_jugador_layout"].deleteLater()
            jugador["nombre_label"].deleteLater()
            jugador["nombre_input"].deleteLater()
            jugador["avatar_label"].deleteLater()
            jugador["avatar_combo"].deleteLater()
            jugador["sesion_label"].deleteLater()
            jugador["boton_cuenta"].deleteLater()
            self.cambio_cant_jugadores()
            self.__vista.cargar_iconos()

    def devolver_jugador(self):
        return Jugador(f'Anónimo{len(self.__vista.jugadores)+1}')

    def crear_partida(self):
        # jugadores = []
        # for jugador in self.__vista.jugadores:
        #     nombre = jugador['nombre'].text()
        #     avatar = jugador['avatar'].currentData()
        #     dinero = jugador['dinero']
        #     propiedades = jugador['propiedades']
        #     banco = jugador['banco']
        #     acciones = jugador['acciones']
        #     jugadores.append({'nombre': nombre, 'avatar': avatar, 'dinero': dinero, 'propiedades': propiedades, 'banco': banco, 'acciones': acciones})
        # self.__vista.close()
        # self.start_game(jugadores)

        jugadores = []
        for j in self.__vista.jugadores:
            jugador = j['jugador_objeto']
            jugador.nombre = j['nombre'].text()
            jugador.avatar = j['avatar'].currentData()
            jugadores.append(jugador)
        self.__vista.close()
        self.start_game(jugadores)
        
    def start_game(self, jugadores):
        ControladorPartida(self.__main_menu, jugadores)
