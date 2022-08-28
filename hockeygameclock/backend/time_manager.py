"""TimeManager module.

This module defines the ``TimeManager`` class.
"""
from datetime import timedelta
from time import perf_counter


# TODO: Rethink TimeManager concept.
# How do we measure time (in combination with Qt)?
# Maybe use update_time() instead of measuring time in here?
# Maybe create a state machine for TimeManager?
# How can we create/connect events (e.g. timeout is over)?
class TimeManager:
    """Manages time."""

    def __init__(self) -> None:
        """Constructor."""
        self.period_length: timedelta
        self.break_length: timedelta
        self.timeout_length: timedelta
        self.period = 1
        self.time: float = 0.0
        self.intermediate_start_time: float = 0.0
        self.running: bool = False

    def set_period_length(self, period_length: timedelta) -> None:
        """Set period length.

        Args:
            period_length: Length of the periods.
        """
        self.period_length = period_length

    def set_break_length(self, break_length: timedelta) -> None:
        """Set break length.

        Args:
            break_length: Length of the break between two periods.
        """
        self.break_length = break_length

    def set_timeout_length(self, timeout_length: timedelta) -> None:
        """Set break length.

        Args:
            timeout_length: Length of the timeout.
        """
        self.timeout_length = timeout_length

    def start(self) -> None:
        """Start timer."""
        if not self.running:
            self.intermediate_start_time = perf_counter()
            self.running = True

    def stop(self) -> None:
        """Stop timer."""
        if self.running:
            self.time += perf_counter() - self.intermediate_start_time
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
            return timedelta(seconds=self.time + perf_counter() - self.intermediate_start_time)
        # if timer is not running
        return timedelta(seconds=self.time)

    def update_time(self, elapsed_time: timedelta) -> None:
        """_summary_

        Args:
            elapsed_time: _description_
        """

    def period_is_over(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """

    def break_is_over(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """

    def timeout_is_over(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """
