"""Player module.
"""
from typing import Optional, Literal
# pylint: disable=no-name-in-module
from PySide6.QtCore import QTime
from hockeyclock.backend.player import Player


# Codes for Penalties
Codes = {
    # Fouls
    'A': 'Behinderung',
    'B': 'Unerlaubter Körperangriff',
    'C': 'Faustschläge / Übertriebene Härte',
    'D': 'Cross-Check',
    'E': 'Halten',
    'F': 'Stockstich',
    'G': 'Stockschlag',
    'H': 'Beinstellen',
    'I': 'Haken',
    'J': 'Hoher Stock',
    'K': 'Ellbogencheck',
    'L': 'Check von Hinten',
    'M': 'Bandencheck',
    'N': 'Stockendstoß',
    'O': 'Kniecheck',
    'P': 'Kopfstoß',
    'Q': 'Check gegen den Kopf und Nackenbereich',
    'R': 'Fußtritt',
    'S': 'Schwalbe',
    # Others
    'W': 'Auswechseln von Spielern',
    'X': 'Spielverzögerung',
    'Y': 'Vergehen von Torhütern',
    'ZA': 'Fehlverhalten',
    'ZB': 'Vergehen auf der Strafbank',
    'ZC': 'Vergehen im Zusammenhang mit Ausrüstung',
}


class Penalty:
    """Class representing a penalty."""

    def __init__(self, player: Player, code: ) -> None:
        """Constructor.

        Args:
            player: The player who gets the penalty.
        """
        self.player = player
        self.start_time: QTime
        self.end_time: QTime

    def start(self, start_time: QTime) -> None:
        """Start Penalty.

        Args:
            start_time: The start time.
        """
        self.start_time = start_time
