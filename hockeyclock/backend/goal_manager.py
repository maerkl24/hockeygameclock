"""Goal Manager module.
"""

from typing import List

from hockeyclock.backend.goal import Goal
from hockeyclock.backend.penalty_manager import TeamType


class GoalManager:
    """Manages all goals."""

    def __init__(self) -> None:
        """Constructor."""
        self.home_goals: List[Goal]
        self.guest_goals: List[Goal]

    def add_goal(self, team: TeamType, goal: Goal) -> None:
        """Add new goal.

        Args:
            team: The to which scored the goal.
            goal: The goal.

        Raises:
            ValueError: If `team` is invalid.
        """
        # select goal lists for home or guest team
        if team == "home":
            goals = self.home_goals
        elif team == "guest":
            goals = self.guest_goals
        else:
            raise ValueError(f'Invalid value "{team}" for team! Valid values are "home" or "guest".')

        # append goal to goal list
        goals.append(goal)
