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
    size = len(data)
    bits = []
    too_many_ones = '11111'
    two_byte_prefix = '110'
    three_byte_prefix = '1110'
    four_byte_prefix = '11110'
    continuation_bits = '10'

    if not data:
        return (False)
    elif not (all(isinstance(x, int) for x in data)):
        return (False)
    for datum in data:
        bit = format(datum, '08b')[-8:]
        bits.append(bit)

    for i in range(size):
        # check if bytes is a single byte character
        if (bits[i][:1] == '0'):
            continue
        # check if byte has more than the max number of leading on bits
        elif (bits[i][:5] == too_many_ones):
            return (False)
        # check for a valid four-byte character
        elif (bits[i][:5] == four_byte_prefix and (i + 3) < size):
            if ((bits[i + 1][:2] == continuation_bits) and
                (bits[i + 2][:2] == continuation_bits) and
                    (bits[i + 3][:2] == continuation_bits)):
                i += 3
                continue
            else:
                return (False)
        # check for a valid three-byte character
        elif (bits[i][:4] == three_byte_prefix and (i + 2) < size):
            if ((bits[i + 1][:2] == continuation_bits) and
                    (bits[i + 2][:2] == continuation_bits)):
                i += 2
                continue
            else:
                return (False)
        # check for a valid two-byte character
        elif ((bits[i][:3] == two_byte_prefix) and ((i + 1) < size)):
            if (bits[i + 1][:2] == continuation_bits):
                i += 1
                continue
            else:
                return (False)
        # check if a byte with continuation_bits is preceded by a start
        # or continuation byte
        elif (bits[i][:2] == continuation_bits):
            if ((bits[i - 1][:3] != two_byte_prefix) and
                    (bits[i - 2][:2] != continuation_bits)):
                return (False)

    return (True)
