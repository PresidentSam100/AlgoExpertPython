# Kadane's Algorithm (Python)
# https://www.algoexpert.io/questions/kadane's-algorithm
# Time Complexity: O(n) n is the length of array
# Space Complexity: O(1)

def kadanesAlgorithm(array):
    bestSum = float('-inf')
    currSum = 0
    for num in array:
        currSum += num
        if currSum > bestSum:
            bestSum = currSum
        if currSum < 0:
            currSum = 0
    return bestSum
