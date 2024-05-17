#!/usr/bin/python3
"""prime game"""


def soe(n):
    """SieveOfEratosthenes
    gets all the prime numbers to n
    Arg:
        n(int): number given
    Return:
        a list of prime numbers
    """
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    nums = [p for p in range(2, n + 1) if prime[p]]
    return nums


def isWinner(x, nums):
    """gets the player that wins the most rounds
    Args:
        x(int): number of rounds
        nums(int): an array of n
    Return:
        name of player that won most rounds
    """
    Maria = 0  # score for maria
    Ben = 0  # score for ben
    winner = None

    # if the array is not empty
    if nums and x and x > 0:
        for i in range(x):
            primes = soe(nums[i])
            maria = primes[0::2]  # gets primes for maria
            ben = primes[1::2]  # gets primes for ben
            if len(maria) > len(ben):
                Maria += 1
            if len(maria) == len(ben):
                Ben += 1
        winner = 'Maria' if Maria > Ben else 'Ben'

    return winner
