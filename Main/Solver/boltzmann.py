from Main.Game.piece import Piece
from Main.Game.position import Position
from Main.Game.woodoku_game import WoodokuGame
from Main.Solver.selector import Selector
from Main.Solver.solver import Solver

import random

class Boltzmann(Selector):
    """A solver that implements a random strategy, selecting any of the
    legal moves in a given game state.
    """    
    @staticmethod
    def get_move(state: WoodokuGame) -> tuple[Piece, Position]:
        """Returns a random move out of all the possible valid moves to
        make

        Args:
            state (WoodokuGame): The state of the Woodokugame to move in

        Returns:
            tuple[Piece, Position]: The move that this solver has returned
            as the selected move
        """        
        return random.choice(Selector.get_legal_moves(state))
    

