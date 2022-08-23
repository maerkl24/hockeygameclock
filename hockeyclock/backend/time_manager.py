"""Time Manager module.
"""
from datetime import timedelta
from time import perf_counter


class TimeManager:
    """Manages time."""

    def __init__(self) -> None:
        """Constructor."""
        self.period = 1
        self.time: float = 0.0
        self.start_time: float = 0.0
        self.running: bool = False

    def start(self) -> None:
        """Start timer."""
        if not self.running:
            self.start_time = perf_counter()
            self.running = True

    def stop(self) -> None:
        """Stop timer."""
        if self.running:
            self.time += perf_counter() - self.start_time
            self.running = False

    def reset(self) -> None:
        """Reset timer to zero."""
        self.stop()
        self.time = 0.0

    def get_time(self) -> timedelta:
        """Get current time.

        Returns:
            Current time.
        """
        # if timer is running
        if self.running:
            return timedelta(seconds=self.time + perf_counter() - self.start_time)
        # if timer is not running
        return timedelta(seconds=self.time)
