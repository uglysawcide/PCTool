from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from utils.windowSettings import setup_window_settings

from data.config import db


class Login(QMainWindow):
    def __init__(self):
        # Подключение дизайна
        super().__init__()
        self.setWindowTitle("PC Tool")
        uic.loadUi('ui/login.ui', self)

        # Установка стиля окна
        setup_window_settings(self)

        self.authorize.clicked.connect(self.on_login)
        self.register_2.clicked.connect(self.on_register)

    def on_login(self):
        login = self.login.text()
        password = self.password.text()

        if login == '' or password == '':
            self.warning_text.setText("Не указан логин или пароль")
            self.warning_text.show()
            return

        user = db.login(login, password)
        if user:
            self.menu_window.show()
            self.hide()
        else:
            self.warning_text.setText("Неверный логин или пароль")
            self.warning_text.show()



    def on_register(self):
        login = self.login.text()
        password = self.password.text()

        if login == '' or password == '':
            self.warning_text.setText("Не указан логин или пароль")
            self.warning_text.show()
            return

        is_register = db.register(login, password)
        if is_register:
            self.menu_window.show()
            self.hide()
        else:
            self.warning_text.setText("Пользователь уже существует")
            self.warning_text.show()