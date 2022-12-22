from typing import Optional
from Main.Game.observer import ClassicTextObserver, Observer
from Main.Game.woodoku_game import WoodokuGame
from Main.Solver.solver import Solver
from Main.Solver.boltzmann import Boltzmann
from Main.Solver.pythagoras import Pythagoras
from Main.Game.classic_woodoku import ClassicWoodoku

class Environment:
    def __init__(self, observers: Optional[list[Observer]]= None):
        if(observers is None):
            observers = []
        self.__observers = observers

    def run_game(self, solver: Solver, woodoku_game: WoodokuGame) -> int:
        """Runs a given game solver on a game state, will return the score
        that the solver got on such a game.

        Args:
            solver (Solver): The solver to use on the game
            woodoku_game (WoodokuGame): The initial game state that the solver
            will act in

        Returns:
            int: The score that the solver recieves from the beginning of the
            game until the game's is_over() function returns True.
        """        

        for observer in self.__observers:
            observer.receive_state(woodoku_game)

        score = 0
        while(not woodoku_game.is_over()):
            piece, position = solver.get_move(woodoku_game)
            if(not woodoku_game.piece_will_fit(piece, position)):
                return -1
            score += woodoku_game.place_piece(piece, position)

            print("\n\n")
            print(piece, f"{position.row}, {position.col}")
            for observer in self.__observers:
                observer.receive_state(woodoku_game)

        return score

if __name__ == "__main__":
    env = Environment(observers=[ClassicTextObserver()])
    solver = Pythagoras()
    game = ClassicWoodoku()

    print(env.run_game(solver, game))