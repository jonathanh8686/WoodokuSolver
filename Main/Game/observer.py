from abc import ABC, abstractmethod
from Main.Game.woodoku_game import WoodokuGame
from Main.Game.classic_woodoku import ClassicWoodoku
class Observer:
    @abstractmethod
    def receive_state(self, state: WoodokuGame) -> None:
        pass

class ClassicTextObserver(Observer):
    def receive_state(self, state: WoodokuGame) -> None:
        assert isinstance(state, ClassicWoodoku)
        board_str = ""
        for row in range(len(state.board)):
            for col in range(len(state.board[row])):
                board_str += "■" if state.board[row][col] else '□'
            board_str += "\n"
        print(board_str)