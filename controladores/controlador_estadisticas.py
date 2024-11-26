class ControladorEstadisticas:
    def __init__(self, main_menu):
        self.__main_menu = main_menu
        self.__vista = Estadisticas(self)

    def mostrar_vista(self):
        self.__vista.show()
    
    def volver(self): #ocultar la vista de estadisticas
        self.__vista.hide() 

    def actualizar_datos(self):
        nombre = "(Nombre de ejemplo)"
        apellido = "(Apellido de ejemplo)"
        nickname = "(Nickname de ejemplo)"
        partidas_jugadas = "(Partidas Jugadas de ejemplo)"
        partidas_ganadas = "(Partidas Ganadas de ejemplo)"
        
        # Actualizar los datos en la vista
        self.__vista.nombre_label.setText(self.__vista.nombre_label.text() + nombre)
        self.__vista.apellido_label.setText(self.__vista.apellido_label.text() + apellido)
        self.__vista.nickname_label.setText(self.__vista.nickname_label.text() + nickname)
        self.__vista.partidas_jugadas_label.setText(self.__vista.partidas_jugadas_label.text() + partidas_jugadas)
        self.__vista.partidas_ganadas_label.setText(self.__vista.partidas_ganadas_label.text() + partidas_ganadas)