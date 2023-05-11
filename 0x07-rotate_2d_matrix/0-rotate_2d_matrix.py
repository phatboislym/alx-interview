#!/usr/bin/python3

"""
module for function that rotates a 2D Matrix
"""
from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """
    Rotate a 2D matrix 90 degrees clockwise.
    args:   matrix: List[List[int]]
    return: None
    """
    size: int = len(matrix)

    for i in range(size):
        for j in range(i, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(size):
        matrix[i] = matrix[i][::-1]
