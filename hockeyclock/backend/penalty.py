"""Penalty module.
"""
from typing import Optional, Literal
from datetime import timedelta
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

    def start(self, start_time: timedelta) -> None:
        """Start Penalty.

        Args:
            start_time: The start time.
        """
        self.start_time = start_time
