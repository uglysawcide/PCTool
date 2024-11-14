from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

from utils.windowSettings import setup_window_settings


class Menu(QMainWindow):
    def __init__(self):
        # Подключение дизайна
        super().__init__()
        uic.loadUi('ui/menu.ui', self)

        # Установка стиля окна
        setup_window_settings(self)