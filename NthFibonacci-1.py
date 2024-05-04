# Nth Fibonacci (Python)
# https://www.algoexpert.io/questions/nth-fibonacci
# Time Complexity: O(2^n) n is the input number
# Space Complexity: O(n)

def getNthFib(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    return getNthFib(n - 1) + getNthFib(n - 2)
