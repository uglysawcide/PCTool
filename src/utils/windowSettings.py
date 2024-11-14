from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt


class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 15, 25, 0)
        self.layout.setSpacing(20)

        # Кнопки управления окном
        self.minimize_button = QPushButton("—")
        self.minimize_button.setFixedSize(30, 30)
        self.minimize_button.clicked.connect(self.parent.showMinimized)
        self.layout.addWidget(self.minimize_button)

        self.close_button = QPushButton("✕")
        self.close_button.setFixedSize(30, 30)
        self.close_button.clicked.connect(self.parent.close)
        self.layout.addWidget(self.close_button)

        self.layout.addStretch(1)
        self.layout.addWidget(self.minimize_button)
        self.layout.addWidget(self.close_button)

        self.minimize_button.setStyleSheet("""
            QPushButton {
                color: white;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #555;
                border-radius: 20px;
            }
        """)

        self.close_button.setStyleSheet("""
            QPushButton {
                color: white;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #ff4d4d;
                border-radius: 20px;
            }
        """)


def setup_window_settings(window):
    # Скрытие стандартной верхней панели окна
    window.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    # Создание кастомной верхней панели
    title_bar = CustomTitleBar(window)
    window.layout().setMenuBar(title_bar)

    # Переменные для перетаскивания окна
    window._old_pos = None

    def mouse_press_event(event):
        if event.button() == Qt.MouseButton.LeftButton:
            window._old_pos = event.globalPosition().toPoint()

    def mouse_release_event(event):
        if event.button() == Qt.MouseButton.LeftButton:
            window._old_pos = None

    def mouse_move_event(event):
        if not window._old_pos:
            return

        delta = event.globalPosition().toPoint() - window._old_pos
        window.move(window.pos() + delta)
        window._old_pos = event.globalPosition().toPoint()

    # Переопределение методов для перетаскивания окна
    window.mousePressEvent = mouse_press_event
    window.mouseReleaseEvent = mouse_release_event
    window.mouseMoveEvent = mouse_move_event
