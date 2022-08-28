"""Types module.

This module defines all custom types of ``hockeygameclock``.
"""
from enum import Enum, auto


class TeamType(Enum):
    """Type for team.

    Args:
        Enum: Inherits from Enum.
    """

    #: The home team.
    HOME = auto()

    #: The guest team.
    GUEST = auto()
