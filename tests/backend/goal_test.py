"""Tests for Goal class.
"""
from datetime import timedelta

from hockeyclock.backend.goal import Goal
from hockeyclock.backend.player import Player


def test_goal_constructor():
    """Test constructor of Goal class."""
    time = timedelta(minutes=2)
    scorer = Player(number=24)
    goal = Goal(time=time, scorer=scorer)
    assert goal.time == time
    assert goal.scorer == scorer
    assert goal.assist is None


def test_goal_constructor_with_optionals():
    """Test constructor of Goal class."""
    time = timedelta(minutes=2)
    scorer = Player(number=24)
    assist = Player(number=10)
    goal = Goal(time=time, scorer=scorer, assist=assist)
    assert goal.time == time
    assert goal.scorer == scorer
    assert goal.assist == assist
