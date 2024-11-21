from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QProgressBar, QLabel, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer

from utils.windowSettings import setup_window_settings
from data.config import db

import psutil
import pynvml

class Menu(QMainWindow):
    def __init__(self):
        # Подключение дизайна
        super().__init__()
        uic.loadUi('ui/menu.ui', self)
        self.setWindowTitle("PC Tool")
        self.setGeometry(100, 100, 1200, 800)

        # Установка стиля окна
        setup_window_settings(self)

        frame1_map = QPixmap("resources/frame1.png")
        frame2_map = QPixmap("resources/frame2.png")
        frame3_map = QPixmap("resources/frame3.png")
        self.frame1.setPixmap(frame1_map)
        self.frame2.setPixmap(frame2_map)
        self.frame3.setPixmap(frame3_map)

        self.button1.clicked.connect(self.main_page)
        self.button2.clicked.connect(self.monitoring)
        self.button3.clicked.connect(self.analyze)

        pynvml.nvmlInit()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)

    def main_page(self):
        self.frame1.show()
        self.frame2.show()
        self.frame3.show()
        self.user.show()
        self.label_4.show()
        try:
            self.cpu_label.hide()
            self.cpu_progress.hide()
            self.ram_label.hide()
            self.ram_progress.hide()
            self.gpu_label.hide()
            self.gpu_progress.hide()
        except:
            pass

    def monitoring(self):
        self.frame1.hide()
        self.frame2.hide()
        self.frame3.hide()
        self.user.hide()
        self.label_4.hide()
        try:
            self.cpu_label.hide()
            self.cpu_progress.hide()
            self.ram_label.hide()
            self.ram_progress.hide()
            self.gpu_label.hide()
            self.gpu_progress.hide()
        except:
            pass

        self.cpu_progress = QProgressBar(self)
        self.ram_progress = QProgressBar(self)
        self.gpu_progress = QProgressBar(self)

        self.cpu_label = QLabel("CPU: 0%", self)
        self.ram_label = QLabel("RAM: 0%", self)
        self.gpu_label = QLabel("GPU: 0%", self)

        self.cpu_progress.setStyleSheet("""
            QProgressBar {
                background-color: rgb(124, 113, 116);
                border-radius: 10px;
                color: white;
                height: 15px;
                width: 200px;
            }
            QProgressBar::chunk { 
                border-radius: 10px;
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(174, 82, 194, 255), stop: 1 rgba(111, 109, 174, 255));
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(201, 87, 149, 255), stop: 1 rgba(179, 65, 244, 255));
            }
        """)

        self.ram_progress.setStyleSheet("""
            QProgressBar {
                background-color: rgb(124, 113, 116);
                border-radius: 10px;
                color: white;
                height: 15px;
                width: 200px;
            }
            QProgressBar::chunk { 
                border-radius: 10px;
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(174, 82, 194, 255), stop: 1 rgba(111, 109, 174, 255));
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(201, 87, 149, 255), stop: 1 rgba(179, 65, 244, 255));
            }
        """)

        self.gpu_progress.setStyleSheet("""
            QProgressBar {
                background-color: rgb(124, 113, 116);
                border-radius: 10px;
                color: white;
                height: 15px;
                width: 200px;
            }
            QProgressBar::chunk { 
                border-radius: 10px;
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(174, 82, 194, 255), stop: 1 rgba(111, 109, 174, 255));
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(201, 87, 149, 255), stop: 1 rgba(179, 65, 244, 255));
            }
        """)

        self.cpu_label.setStyleSheet("""
            QLabel {
                font-size: 12px;
            }
        """)

        self.ram_label.setStyleSheet("""
            QLabel {
                font-size: 12px;
            }
        """)

        self.gpu_label.setStyleSheet("""
            QLabel {
                font-size: 12px;
            }
        """)

        self.cpu_progress.setMaximum(100)
        self.ram_progress.setMaximum(100)
        self.gpu_progress.setMaximum(100)

        self.cpu_label.setGeometry(320, 290, 200, 20)
        self.cpu_progress.setGeometry(320, 310, 200, 15)
        self.ram_label.setGeometry(320, 330, 200, 20)
        self.ram_progress.setGeometry(320, 350, 200, 15)
        self.gpu_label.setGeometry(320, 370, 200, 20)
        self.gpu_progress.setGeometry(320, 390, 200, 15)
        self.cpu_label.show()
        self.cpu_progress.show()
        self.ram_label.show()
        self.ram_progress.show()
        self.gpu_label.show()
        self.gpu_progress.show()

        self.timer.start(1000)

    def analyze(self):
        self.frame1.hide()
        self.frame2.hide()
        self.frame3.hide()
        self.user.hide()
        self.label_4.hide()
        try:
            self.cpu_label.hide()
            self.cpu_progress.hide()
            self.ram_label.hide()
            self.ram_progress.hide()
            self.gpu_label.hide()
            self.gpu_progress.hide()
        except:
            pass

    def update_stats(self):
        cpu_percent = psutil.cpu_percent()
        self.cpu_label.setText(f"CPU: {cpu_percent}%")
        self.cpu_progress.setValue(int(cpu_percent))

        ram_percent = psutil.virtual_memory().percent
        self.ram_label.setText(f"RAM: {ram_percent}%")
        self.ram_progress.setValue(int(ram_percent))

        try:
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            util = pynvml.nvmlDeviceGetUtilizationRates(handle)
            gpu_percent = util.gpu
            self.gpu_label.setText(f"GPU: {gpu_percent}%")
            self.gpu_progress.setValue(int(gpu_percent))
        except pynvml.NVMLError as error:
            self.gpu_label.setText(f"GPU: Ошибка ({error})")
            self.gpu_progress.setValue(0)

    def closeEvent(self, event):
        db.unlogin()
        pynvml.nvmlShutdown()
        event.accept()
