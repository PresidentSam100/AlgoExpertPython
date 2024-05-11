# Max Subset Sum No Adjacent (Python)
# https://www.algoexpert.io/questions/max-subset-sum-no-adjacent
# Time Complexity: O(n) n is length of array
# Space Complexity: O(1)

def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    prevSum = array[0]
    currSum = max(array[0], array[1])
    for index in range(2, len(array)):
        prevSum, currSum = currSum, max(currSum, prevSum + array[index])
    return currSum
