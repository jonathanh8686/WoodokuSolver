from Main.Game.piece import Piece
from Main.Game.position import Position
from Main.Game.woodoku_game import WoodokuGame
from Main.Solver.selector import Selector
from Main.Solver.solver import Solver

class Pythagoras(Selector):
    """A solve that returns the first legal move, in order by
    1. The order that pieces are given in available pieces
    2. Legal positions in row-column order
    """    

    @staticmethod
    def get_move(state: WoodokuGame) -> tuple[Piece, Position]:
        """Returns the first legal move in order by defined in the
        documentation for Pythagoras

        Args:
            state (WoodokuGame): The state to find a move to play in

        Returns:
            tuple[Piece, Position]: The move to play
        """        
        return Selector.get_legal_moves(state)[0]