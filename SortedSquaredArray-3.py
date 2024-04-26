# Sorted Squared Array (Python)
# https://www.algoexpert.io/questions/sorted-squared-array
# Time Complexity: O(n) n is length of array
# Space Complexity: O(n)
def sortedSquaredArray(array):
    arr = [0 for _ in array]
    index = len(array) - 1
    negIndex = 0
    posIndex = len(array) - 1
    while index >= 0:
        if (abs(array[negIndex]) < abs(array[posIndex])):
            arr[index] = array[posIndex] ** 2
            posIndex -= 1
        else:
            arr[index] = array[negIndex] ** 2
            negIndex += 1
        index -= 1
    return arr
