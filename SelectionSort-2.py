# Selection Sort (Python)
# https://www.algoexpert.io/questions/selection-sort
# Best Time Complexity: O(n^2) n is length of array
# Average Time Complexity: O(n^2)
# Worst Time Complexity: O(n^2)
# Best Space Complexity: O(1)
# Average Space Complexity: O(1)
# Worst Space Complexity: O(1)

def selectionSort(array):
    currIndex = 0
    while currIndex < len(array) - 1:
        swapIndex = currIndex
        for index in range(currIndex, len(array)):
            if array[index] < array[swapIndex]:
                swapIndex = index
        array[currIndex], array[swapIndex] = array[swapIndex], array[currIndex] 
        currIndex += 1
    return array
