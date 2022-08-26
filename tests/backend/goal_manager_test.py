"""Tests for :class:`GoalManager` class.
"""
from datetime import timedelta

from hockeygameclock.backend.goal import Goal
from hockeygameclock.backend.goal_manager import GoalManager
from hockeygameclock.backend.player import Player
from hockeygameclock.backend.types import TeamType


def test_goal_manager_add_goal_home():
    """Test add_goal() of GoalManger class."""
    # Arrange
    time = timedelta(minutes=2)
    scorer = Player(number=24)
    goal = Goal(time=time, scorer=scorer)
    goal_manager = GoalManager()

    # Act
    goal_manager.add_goal(team=TeamType.HOME, goal=goal)

    # Assert
    assert goal_manager.home_goals[0] == goal


def test_goal_manager_add_goal_guest():
    """Test add_goal() of GoalManger class."""
    # Arrange
    time = timedelta(minutes=2)
    scorer = Player(number=24)
    goal = Goal(time=time, scorer=scorer)
    goal_manager = GoalManager()

    # Act
    goal_manager.add_goal(team=TeamType.GUEST, goal=goal)

    # Assert
    assert goal_manager.guest_goals[0] == goal


def test_goal_manager_add_goal_home_multiple():
    """Test add_goal() of GoalManger class."""
    # Arrange
    time_1 = timedelta(minutes=2)
    scorer_1 = Player(number=24)
    goal_1 = Goal(time=time_1, scorer=scorer_1)
    time_2 = timedelta(minutes=4)
    scorer_2 = Player(number=39)
    goal_2 = Goal(time=time_2, scorer=scorer_2)
    goal_manager = GoalManager()

    # Act
    goal_manager.add_goal(team=TeamType.HOME, goal=goal_1)
    goal_manager.add_goal(team=TeamType.HOME, goal=goal_2)

    # Assert
    assert goal_manager.home_goals[0] == goal_1
    assert goal_manager.home_goals[1] == goal_2
