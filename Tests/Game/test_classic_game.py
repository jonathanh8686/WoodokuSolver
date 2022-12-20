from Main.Game.classic_woodoku import ClassicWoodoku
from Tests.Game.Util.piece_util import get_dot_piece, get_horizontal_line_piece, get_vertical_line_piece

def test_default_constructor():
    game = ClassicWoodoku()

    assert len(game.get_available_pieces()) == 3

    # because the default game is seeded, we check that the pieces
    # are what we expect
    assert game.get_available_pieces()[0] == get_vertical_line_piece(2)
    assert game.get_available_pieces()[1] == get_vertical_line_piece(3)
    assert game.get_available_pieces()[2] == get_horizontal_line_piece(3)

    assert len(game.board) == 9
    for row in game.board:
        assert len(row) == 9
        for tile in row:
            assert not tile
    assert game.consecutive_clears == 0

def test_get_available_pieces_mutation():
    game = ClassicWoodoku()

    pieces = game.get_available_pieces()

    assert len(pieces) == 3
    assert pieces[0] == get_vertical_line_piece(2)
    assert game.get_available_pieces()[0] == pieces[0]
    assert pieces[1] == get_vertical_line_piece(3)
    assert game.get_available_pieces()[1] == pieces[1]
    assert pieces[2] == get_horizontal_line_piece(3)
    assert game.get_available_pieces()[2] == pieces[2]

    pieces[0] = get_dot_piece()

    assert len(pieces) == 3
    assert pieces[0] == get_dot_piece()
    assert game.get_available_pieces()[0] == get_vertical_line_piece(2)
    assert game.get_available_pieces()[0] != pieces[0]
    assert game.get_available_pieces()[1] == pieces[1]
    assert game.get_available_pieces()[2] == pieces[2]

    pieces.append(get_vertical_line_piece(5))
    assert len(pieces) == 4
    assert len(game.get_available_pieces()) == 3
