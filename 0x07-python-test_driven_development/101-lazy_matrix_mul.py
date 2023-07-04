#!/usr/bin/python3

"""contains function that multiplies 2 matrices"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns the mul of two matrices.
    Args:
        m_a (list containing lists of ints/floats): The first matrix.
        m_b (list/lists of ints/floats): The second matrix.
    Returns:
        list/lists of ints/floats: The result of the matrix mul.
    """

    result = []
    for row_a in m_a:
        result_row = []
        for col_b in zip(*m_b):
            dot_product = sum(a * b for a, b in zip(row_a, col_b))
            result_row.append(dot_product)
        result.append(result_row)

    return result
