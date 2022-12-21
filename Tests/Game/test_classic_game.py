from Main.Game.classic_woodoku import ClassicWoodoku
from Main.Game.position import Position
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

def test_place_piece():
    game = ClassicWoodoku()

    # check that inital state makes sense
    assert len(game.get_available_pieces()) == 3
    assert game.consecutive_clears == 0

    # place the vert-2-line at (1, 0)
    assert game.place_piece(game.get_available_pieces()[0], Position(1, 0)) == 2

    # available pieces updated correctly
    assert len(game.get_available_pieces()) == 2
    assert game.consecutive_clears == 0

    # check board updated correctly and place vert-3-line in (1, 1)
    assert not game.piece_will_fit(game.get_available_pieces()[0], Position(0, 0))
    assert game.piece_will_fit(game.get_available_pieces()[0], Position(1, 1))
    assert game.place_piece(game.get_available_pieces()[0], Position(1, 1)) == 3

    # check available pieces updated correctly
    assert len(game.get_available_pieces()) == 1

    # check board updated correctly and place hort-3-line at (0, 0)
    assert game.piece_will_fit(game.get_available_pieces()[0], Position(0, 0))
    assert game.place_piece(game.get_available_pieces()[0], Position(0, 0)) == 3

    # check that we are expecting the right pieces
    assert len(game.get_available_pieces()) == 3
    assert game.get_available_pieces()[2] == get_horizontal_line_piece(4)

    # add three more pieces that clear the top-left section
    assert game.place_piece(game.get_available_pieces()[0], Position(3, 0)) == 5
    assert game.place_piece(game.get_available_pieces()[0], Position(0, 2)) == 4
    assert game.place_piece(game.get_available_pieces()[0], Position(2, 2)) == 4 + 9*2


    # check that the top-left section is cleared
    for i in range(3):
        for j in range(3):
            assert not game.board[i][j]
