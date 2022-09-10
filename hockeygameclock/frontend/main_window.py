"""MainWindow module.

This module defines the ``MainWindow`` class.
"""
from PySide6.QtWidgets import QMainWindow

from hockeygameclock.frontend.ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main window of hockeygameclock.

    Args:
        QMainWindow: QMainWindow class.
        Ui_MainWindow: Ui_MainWindow class.
    """

    def __init__(self):
        """Constructor."""
        super().__init__()
        self.setupUi(self)
