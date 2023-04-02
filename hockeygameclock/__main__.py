"""Main module of ``hockeygameclock``.
"""
import sys
from pathlib import Path

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication

from hockeygameclock.frontend.main_window import MainWindow

#: Path to Project root
PROJECT_ROOT = Path(__file__).parent.parent


def main() -> None:
    """Main function of ``hockeygameclock``."""
    # Create Qt application instance
    app = QApplication(sys.argv)
    app.setWindowIcon(QPixmap(PROJECT_ROOT.joinpath("assets/logo.svg")))

    # Create and show main window
    window = MainWindow()
    window.show()

    # Execute application
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
