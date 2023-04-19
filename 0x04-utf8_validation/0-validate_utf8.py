#!/usr/bin/python3
"""
module for function `validUTF8`
`validUTF8` determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    args:   data
    return: bool
    """
    if not data:
        return (False)
    elif not (all(isinstance(x, int) for x in data)):
        return (False)
    else:
        for number in data:
            if (number < 0) or (number > 255):
                return (False)
    return (True)
