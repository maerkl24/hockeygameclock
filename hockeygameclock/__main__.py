"""Main module of ``hockeygameclock``.
"""
import sys

from PySide6.QtWidgets import QApplication

from hockeygameclock.frontend.main_window import MainWindow


def main():
    """Main function of ``hockeygameclock``."""
    # Create Qt application instance
    app = QApplication(sys.argv)

    # Create and show main window
    window = MainWindow()
    window.show()

    # Execute application
    app.exec()


if __name__ == "__main__":
    main()
