# student: [YOUR NAME]
# number: [YOUR STUDENT NUMBER]


def sum_row(matrix: list[list[int]], row_n: int) -> int:
    """
    Returns the sum of row row_n of the matrix.

    >>> sum_row([[8, 1, 6], [3, 5, 7], [4, 9, 2]], 0)
    15

    >>> sum_row([[8, 1, 7], [3, 5, 6], [4, 9, 2]], 1)
    14
    """
    pass


def sum_column(matrix: list[list[int]], col_n: int) -> int:
    """
    Returns the sum of column col_n of the matrix.

    >>> sum_column([[8, 1, 6], [3, 5, 7], [4, 9, 2]], 2)
    15

    >>> sum_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0)
    12
    """
    pass


def sum_diagonal(matrix: list[list[int]], diagonal_n: int) -> int:
    """
    Returns the sum of a diagonal of the matrix.
    diagonal_n is 0 for the main diagonal and 1 for the anti-diagonal.

    >>> sum_diagonal([[8, 1, 7], [3, 5, 6], [4, 9, 2]], 0)
    15

    >>> sum_diagonal([[8, 1, 7], [3, 5, 6], [4, 9, 2]], 1)
    16
    """
    pass


def is_magic_square(matrix: list[list[int]]) -> bool:
    """
    Returns True if matrix is a magic square, False otherwise.

    >>> is_magic_square([[8, 1, 6], [3, 5, 7], [4, 9, 2]])
    True

    >>> is_magic_square([[8, 1, 7], [3, 5, 6], [4, 9, 2]])
    False
    """
    pass


if __name__ == '__main__':
    print(f"{sum_row([[8, 1, 6], [3, 5, 7], [4, 9, 2]], 0)=}")
    print(f"{sum_row([[8, 1, 7], [3, 5, 6], [4, 9, 2]], 1)=}")
    print()
    print(f"{sum_column([[8, 1, 6], [3, 5, 7], [4, 9, 2]], 2)=}")
    print(f"{sum_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0)=}")
    print()
    print(f"{sum_diagonal([[8, 1, 7], [3, 5, 6], [4, 9, 2]], 0)=}")
    print(f"{sum_diagonal([[8, 1, 7], [3, 5, 6], [4, 9, 2]], 1)=}")
    print()
    print(f"{is_magic_square([[8, 1, 6], [3, 5, 7], [4, 9, 2]])=}")
    print(f"{is_magic_square([[8, 1, 7], [3, 5, 6], [4, 9, 2]])=}")
