#!/usr/bin/python3

"""
prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
"""


def makeChange(coins, total):
    """
    args:   coins: list
            total: int
    return: counter: int
    """
    if total < 1:
        return 0
    elif not coins:
        return -1
    elif total in coins:
        return 1
    elif total < min(coins):
        return -1
    elif total == sum(coins):
        return len(coins)
    else:
        counter = 0
        for coin in sorted(coins, reverse=True):
            while total >= coin:
                total -= coin
                counter += 1
        if total == 0:
            return counter
        else:
            return -1
