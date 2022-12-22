from Main.Game.piece import Piece
from Main.Game.position import Position
from Main.Game.woodoku_game import WoodokuGame
from Main.Solver.solver import Solver
from abc import abstractmethod

class Selector(Solver):

    @abstractmethod
    def get_move(self, state: WoodokuGame) -> tuple[Piece, Position]:
        pass

    @staticmethod
    def get_legal_moves(state: WoodokuGame) -> list[tuple[Piece, Position]]:
        """Returns a list of all legal moves in the given game state

        Args:
            state (WoodokuGame): The state of the Woodokugame to get all
            legal moves in

        Returns:
            list[tuple[Piece, Position]]: A list of all possible legal moves
            in the given game state
        """        
        def __get_legal_positions(piece: Piece) -> list[Position]:
            """Returns a list of all the possible positions that this piece
            is able to go in

            Args:
                piece (Piece): The piece to check for legal positions

            Returns:
                list[Position]: A list of positions that this piece could be
                placed onto
            """            
            possible_positions: list[Position] = []
            for row in range(state.get_size()):
                for col in range(state.get_size()):
                    if(state.piece_will_fit(piece, Position(row, col))):
                        possible_positions.append(Position(row, col))
            return possible_positions

            
        available_pieces = state.get_available_pieces()

        possible_moves: list[tuple[Piece, Position]] = []
        for piece in available_pieces:
            possible_positions = __get_legal_positions(piece)
            possible_moves.extend([(piece, pos) for pos in possible_positions])

        return possible_moves
    