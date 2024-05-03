# Binary Search (Python)
# https://www.algoexpert.io/questions/binary-search
# Time Complexity: O(log(n)) n is the length of array
# Space Complexity: O(log(n))

def binarySearch(array, target):
    return binarySearchHelper(array, 0, len(array) - 1, target)

def binarySearchHelper(array, lo, hi, target):
    mid = (lo + hi) // 2
    if lo > hi:
        return -1
    elif array[mid] < target:
        return binarySearchHelper(array, mid + 1, hi, target)
    elif array[mid] > target:
        return binarySearchHelper(array, lo, mid - 1, target)
    else:
        return mid
