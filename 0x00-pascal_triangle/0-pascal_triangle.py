#!/usr/bin/env python3
"""
module that generates a Pascal's triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers making up the Pascal’s triangle of n
    Returns an empty list if n <= 0
    assume n will be always an integer
    """
    if (n <= 0):
        return []

    pascal = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if (j == 0 or j == i):
                row.append(1)
            else:
                row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        pascal.append(row)
    return (pascal)
