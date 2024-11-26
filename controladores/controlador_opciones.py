from PyQt6.QtWidgets import QMessageBox 
from PyQt6.QtGui import QGuiApplication

class ControladorOpciones:
    def __init__(self, opcion):
        self.__opcion = opcion

    def mostrar_creditos(self):
        mensaje = QMessageBox(self.__opcion)
        mensaje.setWindowTitle("Créditos")
        mensaje.setText("Nosotros desarrollamos este juego:")
        mensaje.setInformativeText(
            "\n\nBonifacio, Lucas\n"
            "Cárdenas, Franco\n"
            "Lopes, Carlos\n"
            "Gonzales, Nadin\n"
            "Cabana, Ricardo (Abandonó)\n"
            "Williams, Dahiana\n"
            "Vidal, Maida Diego\n"
            "Ampuero, Alejandro\n"
            "Contreras, Joel\n")
        mensaje.setIcon(QMessageBox.Icon.Information)
        mensaje.setStandardButtons(QMessageBox.StandardButton.Ignore)
        mensaje.exec()

    def volver(self):
        self.__opcion.hide()

    def centrar_ventana(self):
        forma_pantalla = QGuiApplication.primaryScreen().availableGeometry()
        forma_ventana = self.__opcion.frameGeometry()
        centro_pantalla = forma_pantalla.center()
        forma_ventana.moveCenter(centro_pantalla)
        self.__opcion.move(forma_ventana.topLeft())
