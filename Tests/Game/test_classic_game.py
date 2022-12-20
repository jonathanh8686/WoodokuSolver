from Main.Game.classic_woodoku import ClassicWoodoku
from Tests.Game.Util.piece_util import get_horizontal_line_piece, get_vertical_line_piece

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