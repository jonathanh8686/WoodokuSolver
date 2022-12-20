from abc import ABC, abstractmethod

from Main.Game.piece import Piece
from Main.Game.position import Position


class WoodokuGame(ABC):
    """Represents an abstract version of the WoodokuGame,
    the game is played on an NxN board. Supports placing
    pieces and will return the reward (additional score) for
    each move. It also allows the user to check if a move is
    legal before executing it (by checking if a piece will fit).
    It also will provide the user with a set of Pieces that are
    available for placement.
    """

    @abstractmethod
    def place_piece(self, piece: Piece, pos: Position) -> int:
        """Simulates the placement of a given piece at the given locatio, will return
        the reward given for such a move as well as an instance for the next state
        that the game is in.
        """
        pass

    @abstractmethod
    def piece_will_fit(self, piece: Piece, pos: Position) -> bool:
        """Returns true or false depending on whether or not the piece can
        be placed at the given location legally.

        Args:
            piece (Piece): The piece to check for placement
            location (Position): The location to check

        Returns:
            bool: Whether or not the piece can be placed at the given location
            without error
        """
        pass

    @abstractmethod
    def get_available_pieces(self) -> list[Piece]:
        """Returns the list of currently available pieces for placement

        Returns:
            list[Piece]: The list of currently available pieces for placement
        """
        pass
