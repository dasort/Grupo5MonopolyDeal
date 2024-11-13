from PyQt6.QtWidgets import QApplication
import sys
from main_menu import MainMenu

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainMenu()
    main_window.show()
    sys.exit(app.exec())