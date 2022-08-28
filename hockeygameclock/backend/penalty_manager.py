"""PenaltyManager module.

This module defines the ``PenaltyManager`` class.
"""

from datetime import timedelta
from typing import List

from hockeygameclock.backend.player_penalty import PlayerPenalty
from hockeygameclock.backend.types import TeamType


class PenaltyManager:
    """Manages all penalties."""

    def __init__(self) -> None:
        """Constructor."""
        self.max_active_penalties = 2
        self.home_penalties_pending: List[PlayerPenalty]
        self.home_penalties_active: List[PlayerPenalty]
        self.home_penalties_expired: List[PlayerPenalty]
        self.guest_penalties_pending: List[PlayerPenalty]
        self.guest_penalties_active: List[PlayerPenalty]
        self.guest_penalties_expired: List[PlayerPenalty]

    def add_penalty(self, team: TeamType, penalty: PlayerPenalty) -> None:
        """Add new penalty.

        Args:
            team: The to be penalized team.
            penalty: The penalty.
        """
        # select penalty lists for home or guest team
        if team == TeamType.HOME:
            penalties_pending = self.home_penalties_pending
            penalties_active = self.home_penalties_active
        elif team == TeamType.GUEST:
            penalties_pending = self.guest_penalties_pending
            penalties_active = self.guest_penalties_active

        # check if active penalties is less than maximum number of active penalties
        if len(penalties_active) < self.max_active_penalties:
            # append penalty to active list
            penalties_active.append(penalty)
        else:
            # append penalty to pending list
            penalties_pending.append(penalty)

    def update_time(self, elapsed_time: timedelta) -> None:
        """Update remaining times of active penalties.

        Args:
            elapsed_time: Elapsed time since last update_time() call.
        """
        # TODO: Execute code for home and guest
        penalties_pending = self.home_penalties_pending
        penalties_active = self.home_penalties_active
        penalties_expired = self.home_penalties_expired

        # iterate over all active penalties
        for idx, penalty_active in enumerate(penalties_active):
            # update remaining time of penalty
            penalty_active.update_remaining_time(elapsed_time)
            # check if penalty is over
            if penalty_active.is_over():
                # move penalty to expired list
                penalties_expired.append(penalties_active.pop(idx))
                # check if there are pending penalties
                if len(penalties_pending):
                    # move penalty to active list
                    penalties_active.append(penalties_pending.pop(0))
