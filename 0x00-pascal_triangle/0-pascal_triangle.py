#!/usr/bin/python3
"""
Pascal triangle module
"""

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

    pascal_list = [[1]]
    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            row.append(pascal_list[i-1][j-1] + pascal_list[i-1][j])
        row.append(1)  # Last element of each row is always 1
        pascal_list.append(row)
    return pascal_list