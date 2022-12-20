class InvalidPieceException(ValueError):
    pass


class Piece:
    def __init__(self, piece_list: list[list[bool]]):
        """Creates a piece based on the given arra

        Args:
            piece_list (list[list[bool]]): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
        """
        if (len(piece_list) <= 0):
            raise ValueError(
                "Invalid piece_list, must have height greater than 0")

        if (any([len(piece_list[i]) <= 0 for i in range(len(piece_list))])):
            raise ValueError(
                "Invalid piece list, must have width greater than 0")

        if (any([len(piece_list[i]) != len(piece_list[0]) for i in range(len(piece_list))])):
            raise ValueError(
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
