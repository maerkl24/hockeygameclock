"""Player module.
"""
from typing import Optional, Literal

# Position for Player
Position = Literal['C', 'A', 'G', 'F']


class Player():
    """Class representing a player."""

    def __init__(self,
                 number: int,
                 position: Optional[Position] = None,
                 forename: Optional[str] = None,
                 surname: Optional[str] = None,
                 pass_number: Optional[int] = None) -> None:
        self.number = number
        self.position = position
        self.forename = forename
        self.surname = surname
        self.pass_number = pass_number
