# Nth Fibonacci (Python)
# https://www.algoexpert.io/questions/nth-fibonacci
# Time Complexity: O(n) n is the input
# Space Complexity: O(1)

def getNthFib(n):
    previousTwo = [0, 1]
    while n > 1:
        n -= 1
        nextFib = previousTwo[0] + previousTwo[1]
        previousTwo[0] = previousTwo[1]
        previousTwo[1] = nextFib
    return previousTwo[0]
