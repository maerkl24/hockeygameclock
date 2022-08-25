"""Goal module.
"""
from datetime import timedelta
from typing import Optional

from hockeyclock.backend.player import Player


class Goal:
    """Class representing a goal."""

    def __init__(self, time: timedelta, scorer: Player, assist: Optional[Player] = None) -> None:
        """Constructor.

        Args:
            time: Time of the goal.
            scorer: Scorer of the goal.
            assist: Assist of the goal.
        """
        self.time = time
        self.scorer = scorer
        self.assist = assist
