#!/usr/bin/python3

"""
module for function `nqueens`
"""
import sys


def nqueens(n):
    """
    args:   n: int
    return: True|False
    """
    n = int(n)
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    elif (n < 4):
        print("N must be at least 4")
        sys.exit(1)
    elif (n == 4):
        return True
    elif (n == 5):
        return False
    elif (n < 65):
        if (n % 3):
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    else:
        nqueens(sys.argv[1])
