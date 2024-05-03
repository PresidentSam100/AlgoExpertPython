# Nth Fibonacci (Python)
# https://www.algoexpert.io/questions/nth-fibonacci
# Time Complexity: O(n) n is the input
# Space Complexity: O(1)

def getNthFib(n):
    a = 0
    b = 1
    while n > 1:
        n -= 1
        c = a + b
        a = b
        b = c
    return a
