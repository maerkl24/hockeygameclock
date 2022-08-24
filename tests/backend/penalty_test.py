"""Tests for Penalty class.
"""
from datetime import timedelta

from hockeyclock.backend.penalty import Penalty
from hockeyclock.backend.player import Player


def test_penalty_constructor():
    """Test constructor of Penalty class."""
    player = Player(number=24)
    penalty = Penalty(player=player, penalty="2")
    assert penalty.player == player
    assert penalty.penalty == "2"
    assert penalty.code is None


def test_penalty_set_start_time():
    """Test set_start_time() method of Penalty class."""
    start_time = timedelta(minutes=2)
    player = Player(number=24)
    penalty = Penalty(player=player, penalty="2")
    penalty.set_start_time(start_time=start_time)
    assert penalty.start_time == start_time


def test_penalty_set_end_time():
    """Test set_end_time() method of Penalty class."""
    end_time = timedelta(minutes=4)
    player = Player(number=24)
    penalty = Penalty(player=player, penalty="2")
    penalty.set_end_time(end_time=end_time)
    assert penalty.end_time == end_time


def test_penalty_update_remaining_time():
    """Test update_remaining_time() method of Penalty class."""
    expected_remaining_time = timedelta(minutes=1, seconds=59, milliseconds=900)
    elapsed_time = timedelta(milliseconds=100)
    player = Player(number=24)
    penalty = Penalty(player=player, penalty="2")
    penalty.remaining_time = timedelta(minutes=2)
    penalty.update_remaining_time(elapsed_time=elapsed_time)
    assert penalty.remaining_time == expected_remaining_time


def test_penalty_is_over_true():
    """Test is_over() method of Penalty class."""
    elapsed_time = timedelta(minutes=2)
    player = Player(number=24)
    penalty = Penalty(player=player, penalty="2")
    penalty.remaining_time = timedelta(minutes=2)
    penalty.update_remaining_time(elapsed_time=elapsed_time)
    assert penalty.is_over() is True


def test_penalty_is_over_false():
    """Test is_over() method of Penalty class."""
    elapsed_time = timedelta(minutes=1)
    player = Player(number=24)
    penalty = Penalty(player=player, penalty="2")
    penalty.remaining_time = timedelta(minutes=2)
    penalty.update_remaining_time(elapsed_time=elapsed_time)
    assert penalty.is_over() is False
