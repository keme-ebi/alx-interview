#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(3, [4, 5, 1])))
print("Winner: {}".format(isWinner(4, [2, 5, 2, 6])))
print("Winner: {}".format(isWinner(0, [])))
print("Winner: {}".format(isWinner(0, [4, 2, 5])))
print("Winner: {}".format(isWinner(2, 0)))
print("Winner: {}".format(isWinner(None, [3, 4])))
print("Winner: {}".format(isWinner(4, None)))
print("Winner: {}".format(isWinner(-3, [4, 5, 5])))
