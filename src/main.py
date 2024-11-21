import sys
from PyQt6.QtWidgets import QApplication

from handlers.login import Login
from handlers.menu import Menu

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = Login()
    menu_window = Menu()

    login_window.menu_window = menu_window
    menu_window.login_window = login_window

    login_window.show()
    sys.exit(app.exec())
