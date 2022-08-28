"""Tests for ``Goal`` class.
"""
from datetime import timedelta

from hockeygameclock.backend.goal import Goal
from hockeygameclock.backend.player import Player


def test_goal_constructor():
    """Test constructor of Goal class."""
    # Arrange
    time = timedelta(minutes=2)
    scorer = Player(number=24)

    # Act
    goal = Goal(time=time, scorer=scorer)

    # Assert
    assert goal.time == time
    assert goal.scorer == scorer
    assert goal.assist is None


def test_goal_constructor_with_optionals():
    """Test constructor of Goal class with all optional arguments."""
    # Arrange
    time = timedelta(minutes=2)
    scorer = Player(number=24)
    assist = Player(number=10)

    # Act
    goal = Goal(time=time, scorer=scorer, assist=assist)

    # Assert
    assert goal.time == time
    assert goal.scorer == scorer
    assert goal.assist == assist
