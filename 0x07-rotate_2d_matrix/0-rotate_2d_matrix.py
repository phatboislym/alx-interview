#!/usr/bin/python3

"""
module for function that rotates a 2D Matrix
"""


def rotate_2d_matrix(matrix) -> None:
    """
    rotate a 2D matrix 90° clockwise
    args:   matrix: List[List[int]]
    return: None
    """
    size = len(matrix)

    for i in range(size):
        for j in range(i, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(size):
        matrix[i] = matrix[i][::-1]

    return
