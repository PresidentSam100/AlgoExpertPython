# Subarray Sort (Python)
# https://www.algoexpert.io/questions/subarray-sort
# Time Complexity: O(n) n is the length of array
# Space Complexity: O(1)

def subarraySort(array):
    n = len(array)
    unordered_max = float("-inf")
    unordered_min = float("inf")
    for i in range(n):
        if i > 0 and array[i - 1] > array[i] or i < n - 1 and array[i] > array[i + 1]:
            unordered_max = max(unordered_max, array[i])
            unordered_min = min(unordered_min, array[i])
    if unordered_max == float("-inf") and unordered_min == float("inf"):
        return [-1, -1]
    left = 0
    right = n - 1
    while unordered_min >= array[left]:
        left += 1
    while unordered_max <= array[right]:
        right -= 1
    return [left, right]
