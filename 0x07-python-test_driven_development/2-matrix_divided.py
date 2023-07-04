#!/usr/bin/python3
"""Matrix division function"""


def matrix_divided(matrix, div):
    """All elements of a matrix are divided by a input number
    Args:
    - matrix(A list containing lists)- content can be type of ints or floats
    - div: the number to be used to divide
    Raises:
    - TypeError: when matrix contains no numbers
    - TypeError: when matrix contains rows with different sizes
    - TypeError: when div is not int or float
    - ZeroDivisionError: if the div is 0
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
