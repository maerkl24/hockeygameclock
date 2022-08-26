"""Tests for :class:`GoalManager` class.
"""
from datetime import timedelta

from hockeygameclock.backend.goal import Goal
from hockeygameclock.backend.player import Player


def test_goal_manager_constructor():
    """Test constructor of GoalManger class."""
    time = timedelta(minutes=2)
    scorer = Player(number=24)
    goal = Goal(time=time, scorer=scorer)
    assert goal.time == time
    assert goal.scorer == scorer
    assert goal.assist is None
