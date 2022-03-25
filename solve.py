from generate_pieces import get_pieces
import typing

class Game:
    board = None
    def __init__(self):
        '''
        Initalizes a new Game object which represents a Woodoku game
        '''
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def check_piece_fit(self, piece: list[list[int]], location: tuple[int, int]):
        '''
        Returns True if the even piece will fit if placed with the top-left most
        cell at the given position
        '''
        pass

    def is_occupied_at(self, location: tuple[int, int]) -> bool:
        '''
        Returns True if the cell at the position described by the tuple
        location is filled in
        '''
        return False if self.board[location[0]][location[1]] == 0 else True

def solve_board(game, given_pieces):
    print(game.is_occupied_at((1, 1)))

def main():
    pieces = get_pieces()
    solve_board(Game(), [pieces[0], pieces[1], pieces[2]])


if(__name__ == "__main__"):
    main()


