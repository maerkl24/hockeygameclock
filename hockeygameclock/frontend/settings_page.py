"""SettingsPage module.

This module defines the ``SettingsPage`` class.
"""

from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGridLayout, QLabel, QWidget


class SettingsPage(QWidget):
    """Settings page UI."""

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self._layout = QGridLayout(self)
        label = QLabel(self)
        label.setText("Settings")
        label.setStyleSheet('color: rgb(255, 255, 255); font: 700 48pt "Segoe UI";')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._layout.addWidget(label)
