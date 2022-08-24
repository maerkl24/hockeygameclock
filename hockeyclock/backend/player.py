"""Player module.
"""
from typing import Literal, Optional

# Position for Player
PositionType = Literal["C", "A", "G", "F"]


# pylint: disable=too-few-public-methods
class Player:
    """Class representing a player."""

    # pylint: disable=too-many-arguments
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
