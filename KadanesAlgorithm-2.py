# Kadane's Algorithm (Python)
# https://www.algoexpert.io/questions/kadane's-algorithm
# Time Complexity: O(n) n is the length of array
# Space Complexity: O(1)

def kadanesAlgorithm(array):
    bestSum = float('-inf')
    currSum = 0
    for num in array:
        currSum += num
        bestSum = max(currSum, bestSum)
        currSum = max(currSum, 0)
    return bestSum
