#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide elements of a matrix by an integer in a new matrix
    """

    if (
        not isinstance(matrix, list)
        or any(not isinstance(row, list) for row in matrix)
        or any(not isinstance(elem, (int, float)) for row in matrix for elem in row)
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
