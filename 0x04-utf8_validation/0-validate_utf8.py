#!/usr/bin/python3
"""
This module contains a method that determines if a given data set
is valid UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determine if a given data set is valid UTF-8 encoding.
    - Returns: True if data is valid UTF-8 encoding, False otherwise.
    """
    number_of_bytes = 0
    mask = 255

    for byte in data:
        if number_of_bytes == 0:
            byte = byte & mask
            if (byte >> 5) == 0b110:
                number_of_bytes = 1
            elif (byte >> 4) == 0b1110:
                number_of_bytes = 2
            elif (byte >> 3) == 0b11110:
                number_of_bytes = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            number_of_bytes -= 1

    return number_of_bytes == 0
