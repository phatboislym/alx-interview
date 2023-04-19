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
    bits = []
    bit_sequence = ''
    for datum in data:
        bit = bin(datum)
        bit = bit[2:]
        bit_sequence += bit
        bits.append(bit)
    for i in range(len(bit_sequence)):
        if bit_sequence[i:(i + 8)] == '00000000':
            return (False)
    for i in range(len(bits)):
        if bits[i][:2] == '10' and bits[-1][:2] != '11':
            return (False)
        elif bits[i][:2] == '11' and bits[(i + 1)][:2] != '10':
            return (False)
        elif bits[i][:3] == '111' and bits[(i + 2)][:2] != '10':
            return (False)
        elif bits[i][:4] == '1111' and bits[(i + 3)][:2] != '10':
            return (False)
    return (True)
