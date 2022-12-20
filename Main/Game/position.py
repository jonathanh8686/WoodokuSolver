class Position():
    """A position represents a location (by row and column)
    on a Woodoku board. This class is immutable.
    """

    def __init__(self, row: int, col: int) -> None:
        """Creates a new Position object that represents a location
        on the board at the given row and column (zero-indexed)

        Args:
            row (int): The row (counting from the top of the board) of this position
            col (int): The column (counting from the left of the board) of this position

        Raises:
            ValueError: If the row or column is negative
        """
        if (row < 0):
            raise ValueError("Invalid position, row cannot be negative")
        if (col < 0):
            raise ValueError("Invalid position, column cannot be negative")
        self.__row = row
        self.__col = col

    @property
    def row(self):
        return self.__row

    @property
    def col(self):
        return self.__col
