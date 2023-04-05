#!/usr/bin/python3

"""
module for a function that returns the minimum number of operations
    needed to transform a character H into exactly n H
    while being able to execute only two operations, Copy All and Paste
Prototype: def minOperations(n)
takes an integer, n
returns an integer, minimum
if n is impossible to achieve, return 0
"""


def is_prime(number):
    """
    helper function checks for primality
    args: number: int
    return: True | False: bool
    """
    if (number == 0 or number == 1):
        return False
    elif (number == 2 or number == 3):
        return True
    elif (number > 3):
        for i in range(2, number):
            if (number % i == 0):
                return False
    return True


def prime_factors(n):
    """
    helper function gets a list of prime factors
    args: n: int
    return: factors: List[int]
    """
    factors = []
    for i in range(2, (n + 1)):
        while ((n % i) == 0):
            n = (n // i)
            factors.append(i)
        if n == 1:
            break
    if n > 1:
        factors.append(n)
    return factors


def minOperations(n):
    """
    task function calculates minimum number operations
    args: n: int
    return: minimum: int
    """
    primality: bool = is_prime(n)
    if primality:
        return (n)
    factors = prime_factors(n)
    minimum = sum(factors)
    return (minimum)
