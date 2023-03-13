import time
from typing import Optional
import tqdm #type: ignore
from Main.Game.observer import ClassicTextObserver, Observer
from Main.Game.reduced_woodoku import ReducedWoodoku
from Main.Game.woodoku_game import WoodokuGame
from Main.Solver.solver import Solver
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
            # if(not woodoku_game.piece_will_fit(piece, position)):
            #     return -1
            score += woodoku_game.place_piece(piece, position)

            for observer in self.__observers:
                observer.receive_state(woodoku_game)

        return score

if __name__ == "__main__":
    from Main.Solver.boltzmann import Boltzmann
    from Main.Solver.pythagoras import Pythagoras
    from Main.Solver.euler import Euler
    env = Environment(observers=[ClassicTextObserver()])
    # env = Environment()
    # solver = Euler(60)

    total_time:float = 0.0
    n = 1

    # import cProfile
    # cProfile.run('env.run_game(Euler(seconds_per_move=5), ReducedWoodoku(seed=0))')

    for i in range(n):
        start = time.perf_counter()
        score = env.run_game(Euler(seconds_per_move=5), ClassicWoodoku(seed=i))

        single_run_time = time.perf_counter() - start
        total_time += single_run_time
        print(f"Run {i} took {single_run_time}s with score {score}. Elapsed: {total_time}s")
    
    print(f"Average runtime: {total_time/n}s")