# Max Subset Sum No Adjacent (Python)
# https://www.algoexpert.io/questions/max-subset-sum-no-adjacent
# Time Complexity: O(n) n is length of array
# Space Complexity: O(1)

def maxSubsetSumNoAdjacent(array):
    currSum, prevSum = 0, 0
    for num in array:
        prevSum, currSum = currSum, max(currSum, prevSum + num)
    return currSum
