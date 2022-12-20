from Main.Game.position import Position
from Main.Util.generate_pieces import get_pieces
from Main.Game.woodoku_game import WoodokuGame
from Main.Game.piece import Piece


class InvalidMoveError(Exception):
    """Raised when the player makes an illegal move, by placing the
    piece on a tile that is already occupied, or by placing the piece
    that would be out of the bounds of the board.
    """
    pass


class ClassicWoodoku(WoodokuGame):
    """Represents the classic Woodoku game as available on iOS.
    It is always played on a 9x9 grid and you are given 3 pieces
    at a time to place. Your score is equal to the number of tiles
    that you fill plus bonus points for clearing. Clearing multiple
    sections of a board at once or consectutively will act as a
    multplier on the number of points you get.
    """
    SIZE: int = 9

    def __init__(self):
        '''
        Initalizes a new Game object which represents a Woodoku game
        '''

        # this board is a 2-D matrix of False and True, depending on
        # whether or not the piece is occuiped or not.
        self.board: list[list[bool]] = [
            [False for _ in range(self.SIZE)] for _ in range(self.SIZE)]

        self.actions: list[Piece] = []

        self.consecutive_clears = 0

    def __check_position_in_bounds(self, pos: Position) -> bool:
        """Returns a boolean that represents whether or not the given position is
        within the bounds of the board

        Args:
            pos (Position): The position to check whether or not is in the bounds
            of the board

        Returns:
            bool: Whether or not the position in within the bounds of the board
        """
        if (pos.row < 0 or pos.row >= self.SIZE):
            return False
        if (pos.col < 0 or pos.col >= self.SIZE):
            return False
        return True

    def check_piece_fit(self, piece: Piece, pos: Position) -> bool:
        """Checks if the given piece fits in the given position

        Args:
            piece (Piece): The piece to check for fit
            pos (Position): The position of the piece to check,
            note that when describing the position of a piece, the
            position always denotes the top left corner for the bounding
            box of such a piece

        Returns:
            bool: Whether or not the piece will fit in the given position
        """
        piece_size = piece.get_size()

        for row in range(piece_size[0]):
            for col in range(piece_size[1]):
                check_location = Position(pos.row + row, pos.col + col)
                if (not self.__check_position_in_bounds(check_location)):
                    return False
                if (self.board[check_location.row][check_location.col]):
                    return False

        return True

    def place_piece(self, piece: Piece, pos: Position) -> int:
        """Places the piece at the given position on the board, the position
        denotes the coordinate of the top-left corner of the bounding box
        of the piece. Will mutate this board into whatever the result of such
        a placement is (including clearing relavent sections) and returns
        the reward for such a move.

        Args:
            piece (Piece): The piece to attempt to place on the given position
            pos (Position): The position to attempt to place the piece at

        Raises:
            InvalidMoveError: If the move is illegal, when the piece would be
            placed on top of an already occupied tile

        Returns:
            int: The reward (points gained) for executing the move
        """
        if (not self.check_piece_fit(piece, pos)):
            raise InvalidMoveError(
                "The given piece does not fit in the given position")

        def __add_piece_to_board(piece: Piece, pos: Position) -> None:
            """Adds the given piece to the given position on the board

            Args:
                piece (Piece): The piece to add
                pos (Position): The position to add this piece on
            """
            piece_size = piece.get_size()
            for row in range(piece_size[0]):
                for col in range(piece_size[1]):
                    self.board[row + pos.row][col + pos.col] = True

        def __clear_sections() -> int:
            """Clears the appropiate sections of the board to be cleared,
            by checking rows, columns, and 3x3 disjoint squares on the board.

            Returns:
                int: The reward gained for performing such a move
            """
            # TODO: optimize this by only checking possible sections?

            def __clear_row(row: int) -> None:
                """Clears the row at the given row index

                Args:
                    row (int): The index of the row to remove
                """
                for col in range(self.SIZE):
                    self.board[row][col] = False

            def __clear_col(col: int) -> None:
                """Clears the column at the given column index

                Args:
                    col (int): The index of the column to remove
                """
                for row in range(self.SIZE):
                    self.board[row][col] = False

            def __clear_square(square_pos: Position) -> None:
                """Clears the square with top-left corner at the given position

                Args:
                    square_pos (Position): The position of the top-left corner
                    of the square to clear
                """
                for i in range(3):
                    for j in range(3):
                        self.board[square_pos.row +
                                   i][square_pos.col + j] = False

            reward = 0
            # check all rows
            for row in range(self.SIZE):
                to_clear = True
                for col in range(self.SIZE):
                    if (not self.board[row][col]):
                        to_clear = False
                        break
                if (to_clear):
                    reward += 9 * self.consecutive_clears
                    __clear_row(row)

            # check all columns
            for col in range(self.SIZE):
                to_clear = True
                for row in range(self.SIZE):
                    if (not self.board[row][col]):
                        to_clear = False
                        break
                if (to_clear):
                    reward += 9 * self.consecutive_clears
                    __clear_col(col)

            # check all 3x3 squares
            square_starts = [Position(i, j)
                             for i in range(0, self.SIZE, 3)
                             for j in range(0, self.SIZE, 3)]
            for start_pos in square_starts:
                to_clear = True
                for i in range(3):
                    for j in range(3):
                        if (not self.board[start_pos.row + i][start_pos.col + j]):
                            to_clear = False
                            break
                if (to_clear):
                    reward += 9 * self.consecutive_clears
                    __clear_square(start_pos)

            return reward

        __add_piece_to_board(piece, pos)
        reward = __clear_sections()

        return reward
