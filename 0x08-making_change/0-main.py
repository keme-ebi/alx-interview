#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

print(makeChange([9, 6, 5, 1], 11))

print(makeChange([1, 2, 5], 11))

print(makeChange([1, 3, 4], 0))

print(makeChange([2, 4, 5], -2))