"""Penalty module.
"""
from datetime import timedelta
from typing import Literal, Optional

from hockeyclock.backend.player import Player

# Possible penalties
PenaltiesType = Literal["2", "5", "10", "GM", "5+GM", "10+GM", "MP"]
Penalties = [
    {"id": "2", "time": "2:00"},
    {"id": "5", "time": "5:00"},
    {"id": "10", "time": "10:00"},
    {"id": "GM", "time": None},
    {"id": "5+GM", "time": "5:00"},
    {"id": "10+GM", "time": "10:00"},
    {"id": "MP", "time": "5:00"},
]

# Possible penalty codes
Codes = {
    # Fouls
    "A": "Behinderung",
    "B": "Unerlaubter Körperangriff",
    "C": "Faustschläge / Übertriebene Härte",
    "D": "Cross-Check",
    "E": "Halten",
    "F": "Stockstich",
    "G": "Stockschlag",
    "H": "Beinstellen",
    "I": "Haken",
    "J": "Hoher Stock",
    "K": "Ellbogencheck",
    "L": "Check von Hinten",
    "M": "Bandencheck",
    "N": "Stockendstoß",
    "O": "Kniecheck",
    "P": "Kopfstoß",
    "Q": "Check gegen den Kopf und Nackenbereich",
    "R": "Fußtritt",
    "S": "Schwalbe",
    # Others
    "W": "Auswechseln von Spielern",
    "X": "Spielverzögerung",
    "Y": "Vergehen von Torhütern",
    "ZA": "Fehlverhalten",
    "ZB": "Vergehen auf der Strafbank",
    "ZC": "Vergehen im Zusammenhang mit Ausrüstung",
}


# pylint: disable=too-few-public-methods
class Penalty:
    """Class representing a penalty."""

    def __init__(self, player: Player, penalty: PenaltiesType, code: Optional[str] = None) -> None:
        """Constructor.

        Args:
            player: The to be penalized player.
            penalty: The penalty.
            code: The penalty code.
        """
        self.player = player
        self.penalty = penalty
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
