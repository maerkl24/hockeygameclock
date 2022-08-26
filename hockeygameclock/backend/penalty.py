"""Penalty module.

This module defines the `Penalty` class and instantiates all allowed penalties.
"""

from datetime import timedelta


class Penalty:
    """Class representing a penalty."""

    def __init__(self, code: str, name: str, time: timedelta) -> None:
        """Constructor.

        Args:
            code: The short code of the penalty.
            name: The name of the penalty.
            time: The time a player must serve in the penalty box.
        """
        self.code = code
        self.name = name
        self.time = time


# Possible penalties
PEN_2 = Penalty(code="2", name="kleine Zeitstrafe", time=timedelta(minutes=2))
PEN_5 = Penalty(code="5", name="große Zeitstrafe", time=timedelta(minutes=5))
PEN_10 = Penalty(code="10", name="Disziplinarstrafe", time=timedelta(minutes=10))
PEN_GM = Penalty(code="GM", name="Spieldauerdisziplinarstrafe", time=timedelta(0))
PEN_5GM = Penalty(code="5+GM", name="große Zeitstrafe und Spieldauerdisziplinarstrafe", time=timedelta(minutes=5))
PEN_MP = Penalty(code="MP", name="Matchstrafe", time=timedelta(minutes=5))

# List of possible penalties
PENALTIES = [PEN_2, PEN_5, PEN_10, PEN_GM, PEN_5GM, PEN_MP]
