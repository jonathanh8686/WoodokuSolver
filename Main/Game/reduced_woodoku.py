import random
from typing import Optional
from Main.Game.classic_woodoku import ClassicWoodoku
from Main.Game.piece import Piece
from Main.Game.position import Position
from Main.Game.woodoku_game import WoodokuGame


class ReducedWoodoku(ClassicWoodoku):
    """Represents the classic Woodoku game as available on iOS.
    It is always played on a 9x9 grid and you are given 3 pieces
    at a time to place. Your score is equal to the number of tiles
    that you fill plus bonus points for clearing. Clearing multiple
    sections of a board at once or consectutively will act as a
    multplier on the number of points you get.
    """
    SIZE: int = 9

    def __init__(self, board: Optional[list[list[bool]]] = None,
                 consecutive_clears=0,
                 available_pieces: Optional[list[Piece]] = None,
                 seed=0):
        """Initalizes a new Game object which represents a Woodoku game
        Args:
            seed (int, optional): The seed for the RNG for this game. Defaults to 0.
        """
        self.__classic_game = ClassicWoodoku(board, consecutive_clears, available_pieces, seed)


    def piece_will_fit(self, piece: Piece, pos: Position) -> bool:
        return self.__classic_game.piece_will_fit(piece, pos)

    def place_piece(self, piece: Piece, pos: Position) -> int:
        return self.__classic_game.place_piece(piece, pos)


    def get_available_pieces(self) -> list[Piece]:
        """Returns a copy of list of available pieces the player can use
        this turn.

        Returns:
            list[Piece]: A copy of the list that contains all the available
            pieces that the player can use this turn
        """
        return [self.__classic_game.get_available_pieces()[0]]

    def is_over(self) -> bool:
        """Returns a boolean that represents whether or not the game is over

        Returns:
            bool: Whether or not the game is over
        """

        def __is_placeable(piece: Piece) -> bool:
            """Determines if the given piece has any valid moves on the current
            board

            Args:
                piece (Piece): The piece to check for valid moves

            Returns:
                bool: Whether or not the given piece has any valid moves
            """
            for row in range(self.SIZE):
                for col in range(self.SIZE):
                    if (self.__classic_game.piece_will_fit(piece, Position(row, col))):
                        return True
            return False

        return not __is_placeable(self.__classic_game.get_available_pieces()[0])



    def get_size(self) -> int:
        """Returns the size of the board that this game is played on,
        which is always 9

        Returns:
            int: The size of the board this game is played on, which is
            always 9
        """
        return self.__classic_game.SIZE

    @property
    def board(self) -> list[list[bool]]:
        """Returns a copy of the board for this game
        """
        return self.__classic_game.board

    @property
    def consecutive_clears(self) -> int:
        """Returns the number of consecutive clears in this game
        """
        return 0

    def copy(self) -> "WoodokuGame":
        return ReducedWoodoku(self.__classic_game.board,
                              self.__classic_game.consecutive_clears,
                              self.__classic_game.get_available_pieces(),
                              self.__classic_game.seed)
