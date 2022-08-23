"""Timer module.
"""
# pylint: disable=no-name-in-module
from PySide6.QtCore import QTime, QElapsedTimer


class Timer:
    """Timer to measure elapsed time."""

    def __init__(self):
        self.last_time: QTime = QTime(0, 0, 0, 0)
        self.running_time: QElapsedTimer = QElapsedTimer()
        self.running: bool = False

    def start(self):
        if self.running:
            self.running_time.start()
            self.running = True

    def stop(self):
        if self.running:
            self.last_time = self.last_time.addMSecs(self.running_time.elapsed())
            self.running = False

    def reset(self):
        self.stop()
        self.last_time = QTime(0, 0, 0, 0)

    def get_time(self) -> QTime:
        if not self.running:
            return self.last_time
        else:
            return self.last_time.addMSecs(self.running_time.elapsed())
