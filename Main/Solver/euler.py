import math
from typing import Optional
from Main.Game.piece import Piece
from Main.Game.position import Position
from Main.Game.woodoku_game import WoodokuGame
from Main.Solver.boltzmann import Boltzmann
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
        legal_moves = Selector.get_legal_moves(self.__state)
        for move in legal_moves:
            temp_state = self.__state.copy()
            temp_state.place_piece(*move)
            self.__children[move] = Node(temp_state, 0, 0, parent=self)
    
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
    """Returns the best most via evaluation of the position using
    Monte Carlo Tree Search
    """

    def __init__(self, seconds_per_move: int = 5):
        self.__seconds_per_move = seconds_per_move

    def get_move(self, state: WoodokuGame) -> tuple[Piece, Position]:
        start_time = time.time()
        root = Node(state, 0, 0)
        root.populate_children()
        nodes_explored = 0
        while (time.time() - start_time <= self.__seconds_per_move):
            nodes_explored += 1
            leaf = self.select(root)
            leaf.populate_children()
            rollout_result = self.rollout(leaf)
            self.back_propagate(leaf, rollout_result)
            print(nodes_explored)
        
        return self.get_best_child_action(root)
        

    def select(self, current_node: Node) -> Node:
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
        
    def rollout(self, current_node: Node) -> int:
        return Environment().run_game(Boltzmann(), current_node.state)

    def back_propagate(self, leaf_node: Node, result: int) -> None:
        leaf_node.total_reward += result
        leaf_node.times_visited += 1
        if(leaf_node.parent is not None):
            self.back_propagate(leaf_node.parent, result)

    def get_best_child_action(self, node: Node) -> tuple[Piece, Position]:
        best_child = list(node.children.items())[0][1]
        best_action = list(node.children.items())[0][0]

        for action, child in node.children.items():
            if(best_child.total_reward / best_child.times_visited < child.total_reward / child.times_visited):
                best_child = child
                best_action = action
        return best_action

