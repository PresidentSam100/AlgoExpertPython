# Max Subset Sum No Adjacent (Python)
# https://www.algoexpert.io/questions/max-subset-sum-no-adjacent
# Time Complexity: O(n) n is length of array
# Space Complexity: O(n)

def maxSubsetSumNoAdjacent(array):
    maxSums = array[:]
    for i in range(3):
        maxSums.insert(0, 0)
    for index in range(3, len(maxSums)):
        maxSums[index] += max(maxSums[index - 3], maxSums[index - 2])
    return max(maxSums[-1], maxSums[-2])
