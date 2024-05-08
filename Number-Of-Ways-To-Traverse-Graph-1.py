# Number Of Ways To Traverse Graph (Python)
# https://www.algoexpert.io/questions/number-of-ways-to-traverse-graph
# Time Complexity: O(w + h) w is the graph width, h is the graph height
# Space Complexity: O(1)

def numberOfWaysToTraverseGraph(width, height):
    x = width - 1
    y = height - 1
    numerator = factorial(x + y)
    denominator = factorial(x) * factorial(y)
    return numerator // denominator

def factorial(num):
    ans = 1
    while num > 1:
        ans *= num
        num -= 1
    return ans
