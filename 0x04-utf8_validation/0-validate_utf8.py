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
    blank = []
    if data:
        if (all(isinstance(x, int) for x in data)):
            for number in data:
                if (number < 0) or (number > 255):
                    return (False)
                else:
                    if (number == 0):
                        blank.append(number)
                    else:
                        blank.clear()
                if len(blank) == 8:
                    return (False)
    return (True)
