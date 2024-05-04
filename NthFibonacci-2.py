# Nth Fibonacci (Python)
# https://www.algoexpert.io/questions/nth-fibonacci
# Time Complexity: O(n) n is the input number
# Space Complexity: O(n)

def getNthFib(n, memoize = {1: 0, 2: 1}):
    if n not in memoize:
        memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
    return memoize[n]
