"""Tests for ``Offense`` class.
"""
from hockeygameclock.backend.offense import Offense
from hockeygameclock.backend.penalty import PEN_2


def test_offense_constructor():
    """Test constructor of Offense class."""
    # Act
    offense = Offense(code="A", name="Behinderung", possible_penalties=[PEN_2])

    # Assert
    assert offense.code == "A"
    assert offense.name == "Behinderung"
    assert offense.possible_penalties == [PEN_2]
