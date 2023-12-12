#!/usr/bin/python3
"""
Function that calculates the min operations to copy and paste letters
"""


def minOperations(n):
    t = 0
    m = 2
    while n > 1:
        while not n % m:
            t += m
            n /= m
        m += 1
    return t
