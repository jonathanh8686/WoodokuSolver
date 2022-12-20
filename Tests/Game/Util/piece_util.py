from Main.Game.piece import Piece


def get_dot_piece() -> Piece:
    return Piece([[True]])


def get_square_piece(size: int) -> Piece:
    return Piece([[True for _ in range(size)] for _ in range(size)])


def get_vertical_line_piece(length: int) -> Piece:
    return Piece([[True] for _ in range(length)])


def get_horizontal_line_piece(length: int) -> Piece:
    return Piece([[True for _ in range(length)]])


def get_cross_piece() -> Piece:
    return Piece([[False, True, False],
                  [True,  True, True],
                  [False, True, False]])


def get_t_piece() -> Piece:
    return Piece([[True,  True, True],
                  [False, True, False],
                  [False, True, False]])
