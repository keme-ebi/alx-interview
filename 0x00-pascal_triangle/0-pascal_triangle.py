#!/usr/bin/python3
"""
Pascal triangle module
"""
from math import factorial

def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal's triangle of n
    Args:
        n(int): number of list combination
    Return:
        a list of list of integers
        empty list if n <= 0
    """
    if (n <= 0):
        return []

    pascal_list = []
    for i in range(n):
        row =  [(factorial(i) // (factorial(j) * factorial(i - j))) for j in range(i + 1)]
        pascal_list.append(row)
    return pascal_list