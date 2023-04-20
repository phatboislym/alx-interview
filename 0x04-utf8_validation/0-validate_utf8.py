#!/usr/bin/python3

"""
Lorem ipsum dolor sit amet, qui minim labore adipisicing minim
    sint cillum sint consectetur cupidatat.
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing a UTF-8 encoded string

    Returns:
        True if the data is a valid UTF-8 encoding, False otherwise.
    """
    # Define some constants for the bit patterns used in UTF-8 encoding
    CONTINUATION_BIT = '10'
    TWO_BYTE_PREFIX = '110'
    THREE_BYTE_PREFIX = '1110'
    FOUR_BYTE_PREFIX = '11110'

    for datum in data:
        x = format(datum, '08b')
        print(f'{datum}: {x}')

    # Check if the data is empty or contains non-integer values
    if not data or not all(isinstance(x, int) for x in data):
        return False

    # Iterate through the data and check if each byte is valid
    i = 0
    while i < len(data):
        byte = format(data[i], '08b')

        # Check for a four-byte sequence
        if byte.startswith(FOUR_BYTE_PREFIX):
            if i+3 >= len(data) or \
               not all(format(data[j], '08b').startswith(CONTINUATION_BIT)
                       for j in range(i+1, i+4)):
                return False
            i += 4

        # Check for a three-byte sequence
        elif byte.startswith(THREE_BYTE_PREFIX):
            if i+2 >= len(data) or \
               not all(format(data[j], '08b').startswith(CONTINUATION_BIT)
                       for j in range(i+1, i+3)):
                return False
            i += 3

        # Check for a two-byte sequence
        elif byte.startswith(TWO_BYTE_PREFIX):
            if i+1 >= len(data) or \
               not format(data[i+1], '08b').startswith(CONTINUATION_BIT):
                return False
            i += 2

        # Check for a single-byte character
        elif byte.startswith('0'):
            i += 1

        # Invalid byte sequence
        else:
            return False

    return True
