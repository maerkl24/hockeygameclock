"""Main module of ``hockeygameclock``.
"""
import os
import sys
from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from hockeygameclock.frontend.windows.main_window import MainWindow

#: Path to Project root
PROJECT_ROOT = Path(__file__).parent.parent


def main():
    """Main function of ``hockeygameclock``."""
    # Set QT font DPI for high scale a 4K monitor
    os.environ["QT_FONT_DPI"] = "96"
    # In case of 4K monitor enable
    # os.environ["QT_SCALE_FACTOR"] = "2"

    # Create Qt application instance
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(PROJECT_ROOT.joinpath("assets/logo.svg").as_posix()))  # TODO: Refactor icon storage

    # Create and show main window
    window = MainWindow()
    window.show()

    # Execute application
    # TODO: Better? sys.exit(app.exec())
    app.exec()


if __name__ == "__main__":
    main()
