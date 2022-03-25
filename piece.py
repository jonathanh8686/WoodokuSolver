import typing

class PieceFactory():
    @staticmethod
    def get_piece(type: str) -> Piece:
        if(type == "dot"):
            return [[1]]
        elif(type == "horizontal_two"):
            return [[1], [1]]
        elif(type == "horizontal_three"):
            return [[1], [1], [1]]
        elif(type == "horizontal_four"):
            return [[1], [1], [1], [1]]
        elif(type == "horizontal_five"):
            return [[1], [1], [1], [1], [1]]
        elif(type == "vertical_two"):
            return [[1,1]]
        elif(type == "vertical_three"):
            return [[1,1,1]]
        elif(type == "vertical_four"):
            return [[1,1,1,1]]
        elif(type == "vertical_five"):
            return [[1,1,1,1,1]]
        elif(type == "square"):
            return [[1, 1], [1, 1]]
        elif(type == "right_z"):
            return [[0, 1, 1], [1, 1, 0]]
        elif(type == "left_z"):
            return [[1, 1, 0], [0, 1, 1]]
        elif(type == "up_l"):
            return [[1, 0], [1, 0], [1, 1]]
        elif(type == "right_l"):
            return [[1, 1, 1], [0, 0, 1]]
        elif(type == "left_l"):
            return [[1, 1, 1], [1, 0 ,0]]
        elif(type == "down_l"):
            return [[1, 1], [0, 1], [0, 1]]

class Piece:
    places = []
    def __init__(self, type: str):
