"""GoalManager module.

This module defines the `GoalManger` class.
"""

from typing import List

from hockeygameclock.backend.goal import Goal
from hockeygameclock.backend.types import TeamType


class GoalManager:
    """Manages all goals."""

    def __init__(self) -> None:
        """Constructor."""
        self.home_goals: List[Goal] = []
        self.guest_goals: List[Goal] = []

    def add_goal(self, team: TeamType, goal: Goal) -> None:
        """Add new goal.

        Args:
            team: The to which scored the goal.
            goal: The goal.
        """
        # select goal lists for home or guest team
        if team == TeamType.HOME:
            goals = self.home_goals
        elif team == TeamType.GUEST:
            goals = self.guest_goals

        # append goal to goal list
        goals.append(goal)
