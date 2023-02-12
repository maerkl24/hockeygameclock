"""MainWindow module.

This module defines the ``MainWindow`` class.
"""
from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QMainWindow

from hockeygameclock.frontend.ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    """Main window of hockeygameclock.

    Args:
        QMainWindow: QMainWindow class.
        Ui_MainWindow: Ui_MainWindow class.
    """

    def __init__(self) -> None:
        """Constructor."""
        super().__init__()
        self.old_pos = QPoint()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_ui_events()

    def connect_ui_events(self) -> None:
        """Connect the events functions for the UI elements."""
        # Page selection buttons
        self.ui.clock_page_button.clicked.connect(self.set_clock_page)
        self.ui.settings_page_button.clicked.connect(self.set_settings_page)

    def set_clock_page(self) -> None:
        """Activate Clock page."""
        self.ui.pages.setCurrentWidget(self.ui.clock_page)

    def set_settings_page(self) -> None:
        """Activate Settings page."""
        self.ui.pages.setCurrentWidget(self.ui.settings_page)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        super().mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        super().mouseMoveEvent(event)
        delta = event.globalPos() - self.old_pos
        self.move(self.pos() + delta)
        self.old_pos = event.globalPos()
