# Bubble Sort (Python)
# https://www.algoexpert.io/questions/bubble-sort
# Best Time Complexity: O(n) n is length of array
# Average Time Complexity: O(n^2)
# Worst Time Complexity: O(n^2)
# Best Space Complexity: O(1)
# Average Space Complexity: O(1)
# Worst Space Complexity: O(1)

def bubbleSort(array):
    for i in range(len(array)):
        sorted = True
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                sorted = False
        if sorted:
            break
    return array
