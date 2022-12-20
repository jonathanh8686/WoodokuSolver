import pytest
from Main.Game.piece import Piece

@pytest.fixture
def dot_piece() -> Piece:
    return Piece([[True]])

@pytest.fixture
def square_piece(size: int) -> Piece:
    return Piece([[True for _ in range(size)] for _ in range(size)])

@pytest.fixture
def vertical_line_piece(length: int) -> Piece:
    return Piece([[True] for _ in range(length)])

@pytest.fixture
def horizontal_line_piece(length: int) -> Piece:
    return Piece([[True for _ in range(length)]])