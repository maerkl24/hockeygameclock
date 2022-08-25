"""Penalty module.
"""
from datetime import timedelta
from typing import Optional

from hockeyclock.backend.fouls import Foul
from hockeyclock.backend.player import Player


class Penalty:
    """Class representing a penalty."""

    def __init__(self, player: Player, foul: Foul, code: Optional[str] = None) -> None:
        """Constructor.

        Args:
            player: The to be penalized player.
            penalty: The penalty.
            code: The penalty code.
        """
        self.player = player
        self.foul = foul
        self.code = code
        self.start_time: timedelta
        self.end_time: timedelta
        # TODO: set remaining time here
        self.remaining_time: timedelta

    def set_start_time(self, start_time: timedelta) -> None:
        """Set start time of penalty.

        Args:
            start_time: The start time.
        """
        self.start_time = start_time

    def set_end_time(self, end_time: timedelta) -> None:
        """Set edn time of penalty.

        Args:
            end_time: The end time.
        """
        self.end_time = end_time

    def update_remaining_time(self, elapsed_time: timedelta) -> None:
        """Update remaining time of penalty.

        Args:
            elapsed_time: Elapsed time since last call.
        """
        self.remaining_time -= elapsed_time

    def is_over(self) -> bool:
        """Check if penalty is over.

        Returns:
            bool: True if penalty is over, otherwise False.
        """
        # check if remaining time is less than or equal to zero
        if self.remaining_time <= timedelta(0):
            return True
        return False
