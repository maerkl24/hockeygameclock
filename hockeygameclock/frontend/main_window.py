"""MainWindow module.

This module defines the ``MainWindows`` class.
"""
from pathlib import Path

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow
from PySide6_DAW.Widgets import DesktopApplication, SideBarButton

from hockeygameclock.frontend.clock_page import ClockPage
from hockeygameclock.frontend.music_page import MusicPage
from hockeygameclock.frontend.settings_page import SettingsPage

#: Path to Project root
PROJECT_ROOT = Path(__file__).parent.parent.parent
#: PATH to icons
ICONS_PATH = PROJECT_ROOT.joinpath("ui/icons")


class MainWindow(QMainWindow):
    """Main Window class."""

    def __init__(self) -> None:
        """Constructor"""
        super().__init__(parent=None)

        self.setWindowTitle("Hockey Game Clock")
        self.setWindowIcon(QPixmap(PROJECT_ROOT.joinpath("assets/logo.svg")))
        self.setMinimumSize(800, 600)

        desktop_application = DesktopApplication(self)
        self.setCentralWidget(desktop_application)

        # Clock Page
        btn_clock = SideBarButton(QPixmap(ICONS_PATH.joinpath("clock.svg")), "Clock")
        page_clock = ClockPage()
        desktop_application.addPage(btn_clock, SideBarButton.Alignment.TOP, page_clock)

        # Music Page
        btn_music = SideBarButton(QPixmap(ICONS_PATH.joinpath("speaker.svg")), "Music")
        page_music = MusicPage()
        desktop_application.addPage(btn_music, SideBarButton.Alignment.TOP, page_music)

        # Settings Page
        btn_settings = SideBarButton(QPixmap(ICONS_PATH.joinpath("settings.svg")), "Settings")
        page_settings = SettingsPage()
        desktop_application.addPage(btn_settings, SideBarButton.Alignment.BOTTOM, page_settings)
