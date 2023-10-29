"""ClockPage module.

This module defines the ``ClockPage`` class.
"""

from typing import Optional

from PySide6.QtWidgets import QWidget

# pylint: disable-next=import-error,no-name-in-module
from hockeygameclock.frontend.generated.clock_widget import Ui_ClockWidget  # type: ignore[reportMissingImports]


class ClockPage(QWidget):
    """Clock page UI."""

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        Ui_ClockWidget().setupUi(self)
