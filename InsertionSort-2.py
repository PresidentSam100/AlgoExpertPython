# Insertion Sort (Python)
# https://www.algoexpert.io/questions/insertion-sort
# Best Time Complexity: O(n) n is length of array
# Average Time Complexity: O(n^2)
# Worst Time Complexity: O(n^2)
# Best Space Complexity: O(1)
# Average Space Complexity: O(1)
# Worst Space Complexity: O(1)

def insertionSort(array):
    for i in range(len(array) - 1):
        j = i + 1
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array
