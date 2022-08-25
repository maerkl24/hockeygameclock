"""Fouls module.
"""

from datetime import timedelta
from typing import List


class Penalty:
    """Class representing a penalty."""

    def __init__(self, code: str, name: str, time: timedelta | None) -> None:
        """Constructor.

        Args:
            code: The short code of the penalty.
            name: The name of the penalty.
            time: The time a player must serve in the penalty box.
        """
        self.code = code
        self.name = name
        self.time = time


class Foul:
    """Class representing a foul."""

    def __init__(self, code: str, name: str, penalties: List[Penalty]) -> None:
        """Constructor.

        Args:
            code: The short code of the foul.
            name: The name of the foul.
            penalties: The possible penalties of this foul.
        """
        self.code = code
        self.name = name
        self.penalties = penalties


# All available penalties
PEN_2 = Penalty(code="2", name="kleine Zeitstrafe", time=timedelta(minutes=2))
PEN_5 = Penalty(code="5", name="große Zeitstrafe", time=timedelta(minutes=5))
PEN_10 = Penalty(code="10", name="Disziplinarstrafe", time=timedelta(minutes=10))
PEN_GM = Penalty(code="GM", name="Spieldauerdisziplinarstrafe", time=None)
PEN_5GM = Penalty(code="5+GM", name="große Zeitstrafe und Spieldauerdisziplinarstrafe", time=timedelta(minutes=5))
PEN_MP = Penalty(code="MP", name="Matchstrafe", time=timedelta(minutes=5))

# All available fouls
FOULS = [
    # Foulspiel
    Foul(code="A", name="Behinderung", penalties=[PEN_2]),
    Foul(code="B", name="Unerlaubter Körperangriff", penalties=[PEN_2, PEN_5, PEN_5GM, PEN_MP]),
    Foul(code="C", name="Faustschläge / Übertriebene Härte", penalties=[PEN_2, PEN_5, PEN_10, PEN_5GM, PEN_MP]),
    Foul(code="D", name="Cross-Check", penalties=[PEN_2, PEN_5, PEN_5GM, PEN_MP]),
    Foul(code="E", name="Halten", penalties=[PEN_2]),
    Foul(code="F", name="Stockstich", penalties=[PEN_5, PEN_5GM, PEN_MP]),
    Foul(code="G", name="Stockschlag", penalties=[PEN_2, PEN_5, PEN_5GM, PEN_MP]),
    Foul(code="H", name="Beinstellen", penalties=[PEN_2, PEN_5, PEN_5GM, PEN_MP]),
    Foul(code="I", name="Haken", penalties=[PEN_2, PEN_5, PEN_5GM, PEN_MP]),
    Foul(code="J", name="Hoher Stock", penalties=[PEN_2, PEN_5, PEN_5GM, PEN_MP]),
    Foul(code="K", name="Ellbogencheck", penalties=[PEN_2, PEN_5, PEN_5GM, PEN_MP]),
    Foul(code="L", name="Check von Hinten", penalties=[PEN_5, PEN_5GM, PEN_MP]),
    Foul(code="M", name="Bandencheck", penalties=[PEN_2, PEN_5, PEN_5GM, PEN_MP]),
    Foul(code="N", name="Stockendstoß", penalties=[PEN_5, PEN_5GM, PEN_MP]),
    Foul(code="O", name="Kniecheck", penalties=[PEN_5, PEN_5GM, PEN_MP]),
    Foul(code="P", name="Kopfstoß", penalties=[PEN_MP]),
    Foul(code="Q", name="Check gegen den Kopf und Nackenbereich", penalties=[PEN_5, PEN_5GM, PEN_MP]),
    Foul(code="R", name="Fußtritt", penalties=[PEN_MP]),
    Foul(code="S", name="Schwalbe", penalties=[PEN_2]),
    # Auswechseln von Spielern
    Foul(code="W", name="Zu viele Spieler auf dem Spielfeld / Wechselfehler", penalties=[PEN_2]),
    # Spielverzögerung
    Foul(code="X", name="Spielverzögerung", penalties=[PEN_2]),
    # Vergehen von Torhütern
    Foul(code="Y", name="Vergehen von Torhütern", penalties=[PEN_2]),
    # Fehlverhalten
    Foul(code="ZA", name="Fehlverhalten", penalties=[PEN_2, PEN_5, PEN_10, PEN_GM, PEN_MP]),
    # Vergehen auf der Strafbank
    Foul(code="ZB", name="Vergehen auf der Strafbank", penalties=[PEN_2, PEN_10, PEN_GM, PEN_MP]),
    # Vergehen im Zusammenhang mit Ausrüstung
    Foul(code="ZC", name="Vergehen im Zusammenhang mit Ausrüstung", penalties=[PEN_2, PEN_10]),
]
