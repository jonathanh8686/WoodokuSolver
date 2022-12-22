from abc import ABC, abstractmethod
from Main.Game.piece import Piece
from Main.Game.position import Position
from Main.Game.woodoku_game import WoodokuGame

class Solver(ABC):
    """Represents an abstract class that is capable of responding with
    a desired move in a WoodokuGame
    """    

    @staticmethod
    @abstractmethod
    def get_move(state: WoodokuGame) -> tuple[Piece, Position]:
        """Returns the the piece and position that it would like to place in
        the given WoodokuGame state given some set of parameters.

        Args:
            state (WoodokuGame): The state to query for a move

        Returns:
            tuple[Piece, Position]: The piece to place and the position to attempt
            to place it at
        """        
        pass



