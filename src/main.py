import sys
from PyQt6.QtWidgets import QApplication, QMessageBox

from handlers.login import Login
from handlers.menu import Menu


def exception_hook(exctype, value, traceback):
    QMessageBox.critical(None, "Критическая ошибка", f"Type: {exctype}\nValue: {value}\nTraceback: {traceback}")


sys.excepthook = exception_hook

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = Login()
    menu_window = Menu()

    login_window.menu_window = menu_window
    menu_window.login_window = login_window

    login_window.show()
    login_window.setWindowTitle("PC Tool")
    sys.exit(app.exec())