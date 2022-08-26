"""Types module.

This module defines all custom types of :module:`hockeygameclock`:
- `TeamType`
"""
from enum import Enum, auto


class TeamType(Enum):
    """Type for team.

    Args:
        Enum: Inherits from Enum.

    Attributes:
        HOME: The home team.
        GUEST: The guest team.
    """

    HOME = auto()
    GUEST = auto()
