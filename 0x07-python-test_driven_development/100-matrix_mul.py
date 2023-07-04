#!/usr/bin/python3
"""Module defining a function for matrix multiplication"""


def matrix_mul(matrix_a, matrix_b):
    """This function multiplies two matrices.
    Args:
        matrix_a (list of lists of int/float): The first matrix to be multiplied.
        matrix_b (list of lists of int/float): The second matrix to be multiplied.
    Raises:
        TypeError: If matrix_a or matrix_b is not a list.
        TypeError: If matrix_a or matrix_b is not a list of lists.
        TypeError: If any element of the lists is not int/float.
        ValueError: If matrix_a or matrix_b is empty.
        ValueError: If matrix_a and matrix_b cannot be multiplied.
    Returns:
        list of lists: A new matrix that is the result of the multiplication.
    """

    if not isinstance(matrix_a, list):
        raise TypeError("matrix_a must be a list.")
    if not isinstance(matrix_b, list):
        raise TypeError("matrix_b must be a list.")

    if not all(isinstance(row, list) for row in matrix_a):
        raise TypeError("matrix_a must be a list of lists.")
    if not all(isinstance(row, list) for row in matrix_b):
        raise TypeError("matrix_b must be a list of lists.")

    if len(matrix_a) == 0 or all(len(row) == 0 for row in matrix_a):
        raise ValueError("matrix_a cannot be empty.")
    if len(matrix_b) == 0 or all(len(row) == 0 for row in matrix_b):
        raise ValueError("matrix_b cannot be empty.")

    if not all((isinstance(element, int) or isinstance(element, float))
               for row in matrix_a for element in row):
        raise TypeError("matrix_a should contain only integers or floats.")
    if not all((isinstance(element, int) or isinstance(element, float))
               for row in matrix_b for element in row):
        raise TypeError("matrix_b should contain only integers or floats.")

    if not all(len(row) == len(matrix_a[0]) for row in matrix_a):
        raise ValueError("Each row of matrix_a must have the same size.")
    if not all(len(row) == len(matrix_b[0]) for row in matrix_b):
        raise ValueError("Each row of matrix_b must have the same size.")

    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("matrix_a and matrix_b cannot be multiplied.")

    transposed_b = []
    for i in range(len(matrix_b[0])):
        row = []
        for j in range(len(matrix_b)):
            row.append(matrix_b[j][i])
        transposed_b.append(row)

    result = []
    for row in matrix_a:
        result_row = []
        for column in transposed_b:
            product = sum(a * b for a, b in zip(row, column))
            result_row.append(product)
        result.append(result_row)

    return result
