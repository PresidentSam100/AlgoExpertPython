# Sorted Squared Array (Python)
# https://www.algoexpert.io/questions/sorted-squared-array
# Time Complexity: O(nlogn) n is length of array
# Space Complexity: O(n)
def sortedSquaredArray(array):
    return sorted(list(map(lambda num: num ** 2, array)))
