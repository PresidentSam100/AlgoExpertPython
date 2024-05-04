# Two Number Sum (Python)
# https://www.algoexpert.io/questions/two-number-sum
# Time Complexity: O(n^2) n is length of array
# Space Complexity: O(1)
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []
