"""Tests for Offense class.
"""
from hockeyclock.backend.offense import Offense
from hockeyclock.backend.penalty import PEN_2


def test_offense_constructor():
    """Test constructor of Offense class."""
    offense = Offense(code="A", name="Behinderung", possible_penalties=[PEN_2])
    assert offense.code == "A"
    assert offense.name == "Behinderung"
    assert offense.possible_penalties == [PEN_2]
