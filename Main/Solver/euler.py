import math
import random
from typing import Optional
from Main.Game.piece import Piece
from Main.Game.position import Position
from Main.Game.woodoku_game import WoodokuGame
from Main.Solver.boltzmann import Boltzmann
from Main.Solver.pythagoras import Pythagoras
from Main.Solver.selector import Selector
from Main.Solver.solver import Solver
from Main.Environment.environment import Environment

import time

class Node():
    """Represents a Node in the MCTS algorithm
    """

    def __init__(self, state: WoodokuGame,
                 total_reward: int,
                 times_visited: int,
                 children: Optional[dict[tuple[Piece, Position], "Node"]]=None,
                 parent: Optional["Node"] = None):
        self.__state = state
        self.__total_reward = total_reward
        self.__times_visited = times_visited

        if(children is None):
            children = {}
        self.__children = children
        self.__parent = parent


    def populate_children(self) -> None:
        """Creates and populates the children of this node by randomly
        selecting moves and determining the resultant state
        """
        legal_moves = Selector.get_legal_moves(self.__state)
        random.shuffle(legal_moves)
        
        def explore_child(move: tuple[Piece, Position]) -> None:
            temp_state = self.__state.copy()
            temp_state.place_piece(*move)
            self.__children[move] = Node(temp_state, 0, 0, parent=self)

        for move in legal_moves[:50]:
            explore_child(move)

    @property
    def children(self) -> dict[tuple[Piece, Position], "Node"]:
        return self.__children

    @property
    def total_reward(self) -> int:
        return self.__total_reward

    @total_reward.setter
    def total_reward(self, val: int) -> None:
        self.__total_reward = val

    @property
    def times_visited(self) -> int:
        return self.__times_visited

    @times_visited.setter
    def times_visited(self, val: int) -> None:
        self.__times_visited = val

    @property
    def state(self) -> WoodokuGame:
        return self.__state.copy()
    
    @property
    def parent(self) -> Optional["Node"]:
        return self.__parent


class Euler(Solver):
    """Returns the best move via evaluation of the position using
    Monte Carlo Tree Search
    """

    def __init__(self, seconds_per_move: int = 5):
        self.__seconds_per_move = seconds_per_move

    def get_move(self, state: WoodokuGame) -> tuple[Piece, Position]:
        """Returns a move as determined by a Monte-Carlo Tree Search on the
        given WoodokuGame state.

        Args:
            state (WoodokuGame): The state of the game to evaluate

        Returns:
            tuple[Piece, Position]: The piece and the position to place it
        """
        start_time = time.time()
        root = Node(state, 0, 0)
        root.populate_children()

        nodes_explored = 0
        while (time.time() - start_time <= self.__seconds_per_move):
            leaf = self.select(root)
            leaf.populate_children()
            rollout_result = self.rollout(leaf, Pythagoras())
            self.back_propagate(leaf, rollout_result)

            nodes_explored += 1
            # print(nodes_explored)
        
        best_action = self.get_best_child_action(root)
        return best_action

    def select(self, current_node: Node) -> Node:
        """Selects a node in the MCTS exploration tree to evaluate by
        calculating the average return and using the UCB algorithm.

        Args:
            current_node (Node): The parent node, whose children are being
            considered for selection

        Returns:
            Node: The node which is selected via UCB
        """
        def __score(node: Node) -> float:
            if(node.parent is None):
                return 0

            average_return = node.total_reward / node.times_visited
            c = 2**0.5
            return average_return + c * (math.log(node.parent.times_visited)/node.times_visited)

        unvisited: list[Node] = []
        for _, node in current_node.children.items():
            if(node.times_visited == 0):
                unvisited.append(node)
        # if there are any unvisited nodes
        if(len(unvisited) != 0):
            # use the first one
            return unvisited[0]

        all_nodes: list[Node] = list(current_node.children.values())
        selected_node = list(sorted(all_nodes, key=__score, reverse=True))[0]
        return selected_node
        
    def rollout(self, current_node: Node, solver: Solver) -> int:
        """Approximates the value of a Node via a rollout algorithm. In this case
        the Pythagoreas Strategy is the rollout.

        Args:
            current_node (Node): The current node to evaluate to the end of a
            game via the given rollout
            solver (Solver): The solver that will determine what to do in order
            to rollout. (This solver should be fast, rolling out is only meant to
            quickly approximate the end-state of a game)

        Returns:
            int: The value of this vertex as computed via roll out.
        """
        # curr_board = current_node.state.board
        # roll_score = 0
        # for row in range(len(curr_board)):
        #     for col in range(len(curr_board[row])):
        #         roll_score += 1 if curr_board[row][col] else 0
        # return roll_score
        return Environment().run_game(solver, current_node.state)

    def back_propagate(self, leaf_node: Node, result: int) -> None:
        """Propagates the value of this vertex back up the tree to the parent
        to update the emperical values of each state

        Args:
            leaf_node (Node): The leaf node to start propagation from
            result (int): The value of the leaf node, which represents the
            value to be propagated up the tree
        """
        leaf_node.total_reward += result
        leaf_node.times_visited += 1
        if(leaf_node.parent is not None):
            self.back_propagate(leaf_node.parent, result)

    def get_best_child_action(self, node: Node) -> tuple[Piece, Position]:
        """Determines the action that is expected to return the highest valuation
        from the given node

        Args:
            node (Node): The node from which the actions are being executed

        Returns:
            tuple[Piece, Position]: The action that returns the best reward from this
            position
        """
        best_child = list(node.children.items())[0][1]
        best_action = list(node.children.items())[0][0]

        for action, child in node.children.items():
            if(child.times_visited == 0):
                continue

            if(best_child.total_reward / best_child.times_visited < child.total_reward / child.times_visited):
                best_child = child
                best_action = action
                print(f"Found better: {best_child.total_reward / best_child.times_visited}")

        return best_action

