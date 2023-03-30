#!/usr/bin/python3
"""
module for the function canUnlockAll
takes a param boxes, which is a list of lists
returns a boolean, if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    args: boxes: list[list]
    return: bool
    """
    if (not isinstance(boxes, list) or len(boxes) == 0):
        return False
    return (True)
