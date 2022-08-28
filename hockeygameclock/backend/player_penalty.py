"""PlayerPenalty module.

This module defines the ``PlayerPenalty`` class.
"""
from datetime import timedelta
from typing import Optional

from hockeygameclock.backend.offense import Offense
from hockeygameclock.backend.penalty import Penalty
from hockeygameclock.backend.player import Player


class PlayerPenalty:
    """Class representing a players penalty."""

    def __init__(self, player: Player, penalty: Penalty, offense: Optional[Offense] = None) -> None:
        """Constructor.

        Args:
            player: The to be penalized player.
            penalty: The penalty.
            offense: The offense.
        """
        self.player = player
        self.penalty = penalty
        self.offense = offense
        self.start_time: timedelta
        self.end_time: timedelta
        self.remaining_time = penalty.time

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
