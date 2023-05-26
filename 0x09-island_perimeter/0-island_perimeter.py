#!/usr/bin/python3
"""
module for island perimeter function
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid:
    args:   grid: list[list[int]]
    return: perimeter: int
    """
    perimeter = 0
    for rows in range(len(grid)):
        for columns in range(len(grid[rows])):
            if grid[rows][columns]:
                perimeter += 4
                if rows and grid[rows - 1][columns]:
                    perimeter -= 2
                if columns and grid[rows][columns - 1]:
                    perimeter -= 2
    return perimeter
