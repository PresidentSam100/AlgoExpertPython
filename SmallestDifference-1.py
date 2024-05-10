# Smallest Difference (Python)
# https://www.algoexpert.io/questions/smallest-difference
# Time Complexity: O(n * m) n is the length of arrayOne, m is the length of arrayTwo
# Space Complexity: O(1)

def smallestDifference(arrayOne, arrayTwo):
    diff = float('inf')
    pair = [-1, -1]
    for num1 in arrayOne:
        for num2 in arrayTwo:
            if abs(num1 - num2) < diff:
                pair = [num1, num2]
                diff = abs(num1 - num2)
    return pair
