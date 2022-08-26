"""Tests for :class:`Penalty` class.
"""
from datetime import timedelta

from hockeygameclock.backend.penalty import Penalty


def test_penalty_constructor():
    """Test constructor of Penalty class."""
    # Act
    penalty = Penalty(code="2", name="kleine Zeitstrafe", time=timedelta(minutes=2))

    # Assert
    assert penalty.code == "2"
    assert penalty.name == "kleine Zeitstrafe"
    assert penalty.time == timedelta(minutes=2)
