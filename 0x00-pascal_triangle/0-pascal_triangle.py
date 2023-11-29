#!/usr/bin/python3
'''Module to find Pascal's Triangle integers'''


def pascal_triangle(n):
    '''Function to find Pascal's Triangle integers'''
    triangle = list()

    if n <= 0:
        return triangle

    if n > 0:
        triangle.append([1])

    if n > 1:
        triangle.append([1, 1])

    for x in range(3, n+1):
        triangle.append([0] * x)
        triangle[x-1][0] = 1
        triangle[x-1][x-1] = 1

        for y in range(1, x-1):
            triangle[x-1][y] = triangle[x-2][y-1] + triangle[x-2][y]

    return triangle
