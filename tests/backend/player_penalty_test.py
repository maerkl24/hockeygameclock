"""Tests for PlayerPenalty class.
"""
from datetime import timedelta

from hockeyclock.backend.offense import OFF_A
from hockeyclock.backend.penalty import PEN_2, PEN_GM
from hockeyclock.backend.player import Player
from hockeyclock.backend.player_penalty import PlayerPenalty


def test_player_penalty_constructor():
    """Test constructor of PlayerPenalty class."""
    player = Player(number=24)
    penalty = PlayerPenalty(player=player, penalty=PEN_2)
    assert penalty.player == player
    assert penalty.penalty == PEN_2
    assert penalty.offense is None
    assert penalty.remaining_time == PEN_2.time


def test_player_penalty_constructor_with_optionals():
    """Test constructor of PlayerPenalty class with all optional arguments."""
    player = Player(number=24)
    penalty = PlayerPenalty(player=player, penalty=PEN_2, offense=OFF_A)
    assert penalty.player == player
    assert penalty.penalty == PEN_2
    assert penalty.offense == OFF_A
    assert penalty.remaining_time == PEN_2.time


def test_player_penalty_set_start_time():
    """Test set_start_time() method of PlayerPenalty class."""
    start_time = timedelta(minutes=2)
    player = Player(number=24)
    penalty = PlayerPenalty(player=player, penalty=PEN_2)
    penalty.set_start_time(start_time=start_time)
    assert penalty.start_time == start_time


def test_player_penalty_set_end_time():
    """Test set_end_time() method of PlayerPenalty class."""
    end_time = timedelta(minutes=4)
    player = Player(number=24)
    penalty = PlayerPenalty(player=player, penalty=PEN_2)
    penalty.set_end_time(end_time=end_time)
    assert penalty.end_time == end_time


def test_player_penalty_update_remaining_time():
    """Test update_remaining_time() method of PlayerPenalty class."""
    expected_remaining_time = timedelta(minutes=1, seconds=59, milliseconds=900)
    elapsed_time = timedelta(milliseconds=100)
    player = Player(number=24)
    penalty = PlayerPenalty(player=player, penalty=PEN_2)
    penalty.update_remaining_time(elapsed_time=elapsed_time)
    assert penalty.remaining_time == expected_remaining_time


def test_player_penalty_is_over_true():
    """Test is_over() method of PlayerPenalty class."""
    elapsed_time = timedelta(minutes=2)
    player = Player(number=24)
    penalty = PlayerPenalty(player=player, penalty=PEN_2)
    penalty.update_remaining_time(elapsed_time=elapsed_time)
    assert penalty.is_over() is True


def test_player_penalty_is_over_false():
    """Test is_over() method of PlayerPenalty class."""
    elapsed_time = timedelta(minutes=1)
    player = Player(number=24)
    penalty = PlayerPenalty(player=player, penalty=PEN_2)
    penalty.update_remaining_time(elapsed_time=elapsed_time)
    assert penalty.is_over() is False


def test_player_penalty_is_over_penalty_gm():
    """Test is_over() method of PlayerPenalty class."""
    player = Player(number=24)
    penalty = PlayerPenalty(player=player, penalty=PEN_GM)
    assert penalty.is_over() is True
