from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from utils.windowSettings import setup_window_settings


class Login(QMainWindow):
    def __init__(self):
        # Подключение дизайна
        super().__init__()
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

    def on_register(self):
        login = self.login.text()
        password = self.password.text()

        if login == '' or password == '':
            self.warning_text.setText("Не указан логин или пароль")
            self.warning_text.show()
