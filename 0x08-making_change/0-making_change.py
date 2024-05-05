#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    """determines the fewest number of coins needed to meet the total
    Args:
        coins: a list of the values of coins
        total: amount to be met
    Return:
        fewest number of coins needed to meet total
    """
    maxi = total + 1
    table = [total + 1 for i in range(maxi)]
    table[0] = 0

    length = len(coins)

    for i in range(1, maxi):
        for j in range(length):
            if (coins[j] <= i):
                sub = table[i - coins[j]]
                if (sub != maxi and sub + 1 < table[i]):
                    table[i] = sub + 1

    if (table[total] == maxi):
        return -1

    return table[total]
