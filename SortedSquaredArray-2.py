# Sorted Squared Array (Python)
# https://www.algoexpert.io/questions/sorted-squared-array
# Time Complexity: O(n * log(n)) n is length of array
# Space Complexity: O(n)
def sortedSquaredArray(array):
    arr = []
    for num in array:
        arr.append(num * num)
    arr.sort()
    return arr
