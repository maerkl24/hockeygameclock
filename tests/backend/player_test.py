"""Tests for :class:`Player` class.
"""
from hockeygameclock.backend.player import Player


def test_player_constructor():
    """Test constructor of Player class."""
    player = Player(number=24)
    assert player.number == 24
    assert player.position is None
    assert player.forename is None
    assert player.surname is None
    assert player.pass_number is None


def test_player_constructor_with_optionals():
    """Test constructor of Player class with all optional arguments."""
    player = Player(number=24, position="C", forename="Kilian", surname="Märkl", pass_number=1234)
    assert player.number == 24
    assert player.position == "C"
    assert player.forename == "Kilian"
    assert player.surname == "Märkl"
    assert player.pass_number == 1234
