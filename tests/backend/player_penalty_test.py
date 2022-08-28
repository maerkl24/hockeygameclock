"""Tests for ``PlayerPenalty`` class.
"""
from datetime import timedelta

from hockeygameclock.backend.offense import OFF_A
from hockeygameclock.backend.penalty import PEN_2, PEN_GM
from hockeygameclock.backend.player import Player
from hockeygameclock.backend.player_penalty import PlayerPenalty


def test_player_penalty_constructor():
    """Test constructor of PlayerPenalty class."""
    # Arrange
    player = Player(number=24)

    # Act
    penalty = PlayerPenalty(player=player, penalty=PEN_2)

    # Assert
    assert penalty.player == player
    assert penalty.penalty == PEN_2
    assert penalty.offense is None
    assert penalty.remaining_time == PEN_2.time


def test_player_penalty_constructor_with_optionals():
    """Test constructor of PlayerPenalty class with all optional arguments."""
    # Arrange
    player = Player(number=24)

    # Act
    penalty = PlayerPenalty(player=player, penalty=PEN_2, offense=OFF_A)

    # Assert
    assert penalty.player == player
    assert penalty.penalty == PEN_2
    assert penalty.offense == OFF_A
    assert penalty.remaining_time == PEN_2.time


def test_player_penalty_set_start_time():
    """Test set_start_time() method of PlayerPenalty class."""
    # Arrange
    start_time = timedelta(minutes=2)
    player = Player(number=24)
    penalty = PlayerPenalty(player=player, penalty=PEN_2)

    # Act
    penalty.set_start_time(start_time=start_time)

    # Assert
    assert penalty.start_time == start_time


def test_player_penalty_set_end_time():
    """Test set_end_time() method of PlayerPenalty class."""
    # Arrange
    end_time = timedelta(minutes=4)
    player = Player(number=24)
    penalty = PlayerPenalty(player=player, penalty=PEN_2)

    # Act
    penalty.set_end_time(end_time=end_time)

    # Assert
    assert penalty.end_time == end_time


def test_player_penalty_update_remaining_time():
    """Test update_remaining_time() method of PlayerPenalty class."""
    # Arrange
    expected_remaining_time = timedelta(minutes=1, seconds=59, milliseconds=900)
    elapsed_time = timedelta(milliseconds=100)
    player = Player(number=24)
    penalty = PlayerPenalty(player=player, penalty=PEN_2)

    # Act
    penalty.update_remaining_time(elapsed_time=elapsed_time)

    # Assert
    assert penalty.remaining_time == expected_remaining_time


def test_player_penalty_is_over_true():
    """Test is_over() method of PlayerPenalty class."""
    # Arrange
    elapsed_time = timedelta(minutes=2)
    player = Player(number=24)
    penalty = PlayerPenalty(player=player, penalty=PEN_2)

    # Act
    penalty.update_remaining_time(elapsed_time=elapsed_time)

    # Assert
    assert penalty.is_over() is True


def test_player_penalty_is_over_false():
    """Test is_over() method of PlayerPenalty class."""
    # Arragne
    elapsed_time = timedelta(minutes=1)
    player = Player(number=24)
    penalty = PlayerPenalty(player=player, penalty=PEN_2)

    # Act
    penalty.update_remaining_time(elapsed_time=elapsed_time)

    # Assert
    assert penalty.is_over() is False


def test_player_penalty_is_over_penalty_gm():
    """Test is_over() method of PlayerPenalty class."""
    # Arrange
    player = Player(number=24)
    penalty = PlayerPenalty(player=player, penalty=PEN_GM)

    # Act and Assert
    assert penalty.is_over() is True
