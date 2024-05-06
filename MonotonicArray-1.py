# Monotonic Array (Python)
# https://www.algoexpert.io/questions/monotonic-array
# Time Complexity: O(n) n is length of array
# Space Complexity: O(1)

def isMonotonic(array):
    nonIncrease = True
    nonDecrease = True
    for index in range(len(array) - 1):
        if array[index] < array[index + 1]:
            nonIncrease = False
        if array[index] > array[index + 1]:
            nonDecrease = False
    return nonIncrease or nonDecrease
