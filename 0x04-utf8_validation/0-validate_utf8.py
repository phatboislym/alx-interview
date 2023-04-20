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
    bits = []

    if not data:
        return (False)
    elif not (all(isinstance(x, int) for x in data)):
        return (False)
    for datum in data:
        if (datum not in VALID_RANGE):
            return (False)
        bit = format(datum, '08b')
        bits.append(bit)

    for i in range(size):
        if bits[i][:5] == '11110':
            if (bits[i + 1][:2] == '10' and bits[i + 2][:2] == '10' and
                    bits[i + 3][:2] == '10'):
                i += 3
            else:
                return (False)
        elif bits[i][:4] == '1110':
            if bits[i + 1][:2] == '10' and bits[i + 2][:2] == '10':
                i += 2
            else:
                return (False)
        elif bits[i][:3] == '110':
            if bits[i + 1][:2] == '10':
                i += 1
            else:
                return (False)
        elif bits[i][:2] == '10':
            if (bits[i - 1][:3] != '110' and bits[i - 2][:4] != '1110' and
                    bits[i - 3][:5] != '1110'):
                return (False)

    return (True)
