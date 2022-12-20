from Main.Game.position import Position
class InvalidPieceException(ValueError):
    """Raised when trying to initalize an invalid piece
    """    
    pass

class Piece:
    """Represents a piece on a WoodokuGame.
    """    
    def __init__(self, piece_list: list[list[bool]]):
        """Creates a piece based on the given 2D array of booleans.

        Args:
            piece_list (list[list[bool]]): The 2D array of booleans that
            represents this piece

        Raises:
            InvalidPieceException: If the given array does not have the proper
            format, e.g. if it has 0 height, 0 width, or not all rows have same
            length.
        """
        if (len(piece_list) <= 0):
            raise InvalidPieceException(
                "Invalid piece_list, must have height greater than 0")

        if (any([len(piece_list[i]) <= 0 for i in range(len(piece_list))])):
            raise InvalidPieceException(
                "Invalid piece list, must have width greater than 0")

        if (any([len(piece_list[i]) != len(piece_list[0]) for i in range(len(piece_list))])):
            raise InvalidPieceException(
                "Invalid piece_list, all rows must be the same width")

        self.__piece_list = piece_list

    def get_size(self) -> tuple[int, int]:
        """Returns the size of the bounding box of this piece as (rows, columns)

        Note that this is always guaranteed to work due to checks by the constructor that
        verify the validity of the piece.

        Returns:
            tuple[int, int]: The size of the bounding box of this piece as (rows, columns)
        """
        return (len(self.__piece_list), len(self.__piece_list[0]))
    
    def is_filled_at(self, displacement: tuple[int, int]) -> bool:
        """Returns whether or not the piece is filled at the given displacement
        relative to the top left corner of it's bounding box

        Args:
            displacement (tuple[int, int]): The rows to travel down and columns
            to travel to the right relative to the top-left corner of the bounding
            box for this piece

        Returns:
            bool: Whether or not this piece is occupied at the described position
        """        
        return self.__piece_list[displacement[0]][displacement[1]]
