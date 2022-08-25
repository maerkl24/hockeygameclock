"""Tests for Penalty class.
"""
from datetime import timedelta

from hockeyclock.backend.penalty import Penalty


def test_penalty_constructor():
    """Test constructor of Penalty class."""
    penalty = Penalty(code="2", name="kleine Zeitstrafe", time=timedelta(minutes=2))
    assert penalty.code == "2"
    assert penalty.name == "kleine Zeitstrafe"
    assert penalty.time == timedelta(minutes=2)
