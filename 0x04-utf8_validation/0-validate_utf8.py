#!/usr/bin/python3
"""
module for function `validUTF8`
`validUTF8` determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    args:   data
    return: True | False
    """
    VALID_RANGE = range(256)
    size = len(data)

    if not data:
        return (False)
    elif not (all(isinstance(x, int) for x in data)):
        return (False)
    else:
        for number in data:
            if (number not in VALID_RANGE):
                return (False)
    i = 0
    while (i < size):
        if (data[i] < 128):
            i += 1
        elif (data[i] < 192):
            return (False)
        elif (data[i] < 224):
            if (i+1 >= size) or not (192 <= data[i+1] < 224):
                return (False)
            i += 2
        elif (data[i] < 240):
            if (i+2 >= size) or not (192 <= data[i+1] < 224 and
                                     192 <= data[i+2] < 224):
                return (False)
            i += 3
        elif (data[i] < 248):
            if (i+3 >= size) or not (192 <= data[i+1] < 224 and
                                     192 <= data[i+2] < 224 and
                                     192 <= data[i+3] < 224):
                return (False)
            i += 4
        else:
            return (False)
    return (True)
