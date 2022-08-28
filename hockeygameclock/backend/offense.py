"""Offense module.

This module defines the ``Offense`` class and instantiates all allowed offenses.
"""

from typing import List

from hockeygameclock.backend.penalty import PEN_2, PEN_5, PEN_5GM, PEN_10, PEN_GM, PEN_MP, Penalty


class Offense:
    """Class representing an offense."""

    def __init__(self, code: str, name: str, possible_penalties: List[Penalty]) -> None:
        """Constructor.

        Args:
            code: The short code of the offense.
            name: The name of the offense.
            possible_penalties: The possible penalties of the offense.
        """
        self.code = code
        self.name = name
        self.possible_penalties = possible_penalties


# Possible offenses
OFF_A = Offense(code="A", name="Behinderung", possible_penalties=[PEN_2])
OFF_B = Offense(code="B", name="Unerlaubter Körperangriff", possible_penalties=[PEN_2, PEN_5, PEN_5GM, PEN_MP])
OFF_C = Offense(
    code="C", name="Faustschläge / Übertriebene Härte", possible_penalties=[PEN_2, PEN_5, PEN_10, PEN_5GM, PEN_MP]
)
OFF_D = Offense(code="D", name="Cross-Check", possible_penalties=[PEN_2, PEN_5, PEN_5GM, PEN_MP])
OFF_E = Offense(code="E", name="Halten", possible_penalties=[PEN_2])
OFF_F = Offense(code="F", name="Stockstich", possible_penalties=[PEN_5, PEN_5GM, PEN_MP])
OFF_G = Offense(code="G", name="Stockschlag", possible_penalties=[PEN_2, PEN_5, PEN_5GM, PEN_MP])
OFF_H = Offense(code="H", name="Beinstellen", possible_penalties=[PEN_2, PEN_5, PEN_5GM, PEN_MP])
OFF_I = Offense(code="I", name="Haken", possible_penalties=[PEN_2, PEN_5, PEN_5GM, PEN_MP])
OFF_J = Offense(code="J", name="Hoher Stock", possible_penalties=[PEN_2, PEN_5, PEN_5GM, PEN_MP])
OFF_K = Offense(code="K", name="Ellbogencheck", possible_penalties=[PEN_2, PEN_5, PEN_5GM, PEN_MP])
OFF_L = Offense(code="L", name="Check von Hinten", possible_penalties=[PEN_5, PEN_5GM, PEN_MP])
OFF_M = Offense(code="M", name="Bandencheck", possible_penalties=[PEN_2, PEN_5, PEN_5GM, PEN_MP])
OFF_N = Offense(code="N", name="Stockendstoß", possible_penalties=[PEN_5, PEN_5GM, PEN_MP])
OFF_O = Offense(code="O", name="Kniecheck", possible_penalties=[PEN_5, PEN_5GM, PEN_MP])
OFF_P = Offense(code="P", name="Kopfstoß", possible_penalties=[PEN_MP])
OFF_Q = Offense(code="Q", name="Check gegen den Kopf und Nackenbereich", possible_penalties=[PEN_5, PEN_5GM, PEN_MP])
OFF_R = Offense(code="R", name="Fußtritt", possible_penalties=[PEN_MP])
OFF_S = Offense(code="S", name="Schwalbe", possible_penalties=[PEN_2])
OFF_W = Offense(code="W", name="Zu viele Spieler auf dem Spielfeld / Wechselfehler", possible_penalties=[PEN_2])
OFF_X = Offense(code="X", name="Spielverzögerung", possible_penalties=[PEN_2])
OFF_Y = Offense(code="Y", name="Vergehen von Torhütern", possible_penalties=[PEN_2])
OFF_ZA = Offense(code="ZA", name="Fehlverhalten", possible_penalties=[PEN_2, PEN_5, PEN_10, PEN_GM, PEN_MP])
OFF_ZB = Offense(code="ZB", name="Vergehen auf der Strafbank", possible_penalties=[PEN_2, PEN_10, PEN_GM, PEN_MP])
OFF_ZC = Offense(code="ZC", name="Vergehen im Zusammenhang mit Ausrüstung", possible_penalties=[PEN_2, PEN_10])

# List of possible penalties
OFFENSES = [
    OFF_A,
    OFF_B,
    OFF_C,
    OFF_D,
    OFF_E,
    OFF_F,
    OFF_G,
    OFF_H,
    OFF_I,
    OFF_J,
    OFF_K,
    OFF_L,
    OFF_M,
    OFF_N,
    OFF_O,
    OFF_P,
    OFF_Q,
    OFF_R,
    OFF_S,
    OFF_W,
    OFF_X,
    OFF_Y,
    OFF_ZA,
    OFF_ZB,
    OFF_ZC,
]
