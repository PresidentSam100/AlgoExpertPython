# Selection Sort (Python)
# https://www.algoexpert.io/questions/selection-sort
# Best Time Complexity: O(n^2) n is length of array
# Average Time Complexity: O(n^2)
# Worst Time Complexity: O(n^2)
# Best Space Complexity: O(1)
# Average Space Complexity: O(1)
# Worst Space Complexity: O(1)

def selectionSort(array):
    for i in range(len(array) - 1):
        index = i
        for j in range(i + 1, len(array)):
            if array[index] > array[j]:
                index = j
        array[i], array[index] = array[index], array[i]
    return array
