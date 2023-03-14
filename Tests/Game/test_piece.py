from Main.Game.piece import InvalidPieceError, Piece
import random
import pytest

def test_one_dim_pieces():
    p = Piece([[True]])
    assert p.get_size() == (1, 1)
    assert p.is_filled_at((0, 0))

    p = Piece([[True, True]])
    assert p.get_size() == (1, 2)
    assert p.is_filled_at((0, 0))
    assert p.is_filled_at((0, 1))

    p = Piece([[True, False]])
    assert p.get_size() == (1, 2)
    assert p.is_filled_at((0, 0))
    assert not p.is_filled_at((0, 1))

    p = Piece([[False, False]])
    assert p.get_size() == (1, 2)
    assert not p.is_filled_at((0, 0))
    assert not p.is_filled_at((0, 1))


@pytest.mark.parametrize("length", [
    1,
    2,
    3,
    4,
    5,
    10,
    50,
    1000,
    50_000
])
def test_random_dimensional_piece(length: int):
    random.seed(0)
    filled: set[int] = set()
    piece_bools: list[list[bool]] = [[]]
    for i in range(length):
        piece_bools[0].append(random.random() <= 0.5)
        if (piece_bools[0][i]):
            filled.add(i)

    p = Piece(piece_bools)
    assert p.get_size() == (1, length)
    for i in range(length):
        assert p.is_filled_at((0, i)) == (i in filled)


def test_simple_pieces():
    p = Piece([[True, True], [True, True]])
    assert p.get_size() == (2, 2)
    for i in range(2):
        for j in range(2):
            assert p.is_filled_at((i, j))

    p = Piece([[True, False], [False, True]])
    assert p.get_size() == (2, 2)
    for i in range(2):
        for j in range(2):
            assert p.is_filled_at((i, j)) == (((i + j) % 2) == 0)

    p = Piece([[False, False], [False, False]])
    assert p.get_size() == (2, 2)
    for i in range(2):
        for j in range(2):
            assert not p.is_filled_at((i, j))

    p = Piece([[True, True, True], [True, True, True]])
    assert p.get_size() == (2, 3)
    for i in range(2):
        for j in range(3):
            assert p.is_filled_at((i, j))

    p = Piece([[True, False, True], [False, True, False]])
    assert p.get_size() == (2, 3)
    for i in range(2):
        for j in range(2):
            assert p.is_filled_at((i, j)) == (((i + j) % 2) == 0)


@pytest.mark.parametrize("side_length", [
    1,
    2,
    3,
    4,
    5,
    10,
    50,
    100,
])
def test_random_square_pieces(side_length: int):
    random.seed(0)
    filled: set[tuple[int, int]] = set()
    piece_bools: list[list[bool]] = []

    for row in range(side_length):
        piece_bools.append([])
        for col in range(side_length):
            piece_bools[row].append(random.random() <= 0.5)
            if (piece_bools[row][col]):
                filled.add((row, col))

    p = Piece(piece_bools)
    assert p.get_size() == (side_length, side_length)
    for row in range(side_length):
        for col in range(side_length):
            assert p.is_filled_at((row, col)) == ((row, col) in filled)

def test_zero_height_piece_fail():
    with pytest.raises(InvalidPieceError) as e_info:
        Piece([])
    assert str(e_info.value) == "Invalid piece_list, must have height greater than 0"

def test_zero_width_piece_fail():
    with pytest.raises(InvalidPieceError) as e_info:
        Piece([[], [], []])
    assert str(e_info.value) == "Invalid piece_list, must have width greater than 0"

def test_different_width_piece_fail():
    with pytest.raises(InvalidPieceError) as e_info:
        Piece([[True], [True, False], [True]])
    assert str(e_info.value) == "Invalid piece_list, all rows must be the same width"

    with pytest.raises(InvalidPieceError) as e_info:
        Piece([[False], [True], [True, True, True, False]])
    assert str(e_info.value) == "Invalid piece_list, all rows must be the same width"

    with pytest.raises(InvalidPieceError) as e_info:
        Piece([[False, False, False], [False, False], [True]])
    assert str(e_info.value) == "Invalid piece_list, all rows must be the same width"

    with pytest.raises(InvalidPieceError) as e_info:
        Piece([[True], [False, False]])
    assert str(e_info.value) == "Invalid piece_list, all rows must be the same width"

    complex_list = [[True] for _ in range(100)] + [[False, False]]
    with pytest.raises(InvalidPieceError) as e_info:
        Piece(complex_list)
    assert str(e_info.value) == "Invalid piece_list, all rows must be the same width"

def test_piece_equals():
    assert Piece([[True]]) == Piece([[True]])
    assert Piece([[True, False]]) == Piece([[True, False]])

    p = Piece([[True, False, False], [True, False, True]])
    p.get_size()
    p.is_filled_at((1, 2))
    assert p == Piece([[True, False, False], [True, False, True]])

def test_constructor_mutation():
    piece_list = [[True]]
    p = Piece(piece_list)
    assert p.get_size() == (1,1)
    piece_list.append([False, False])
    assert p.get_size() == (1,1)
    piece_list = []
    assert p.get_size() == (1,1)