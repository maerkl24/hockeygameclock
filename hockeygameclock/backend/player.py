"""Player module.

This module defines the `Player` class.
"""
from typing import Literal, Optional

# Position for Player
# TODO: Maybe change to Enum
PositionType = Literal["C", "A", "G", "F"]


class Player:
    """Class representing a player."""

    def __init__(
        self,
        number: int,
        position: Optional[PositionType] = None,
        forename: Optional[str] = None,
        surname: Optional[str] = None,
        pass_number: Optional[int] = None,
    ) -> None:
        """Constructor.

        Args:
            number: The players jersey number.
            position: The players position.
            forename: The players forename.
            surname: The players surname.
            pass_number: The players pass number.
        """
        self.number = number
        self.position = position
        self.forename = forename
        self.surname = surname
        self.pass_number = pass_number
