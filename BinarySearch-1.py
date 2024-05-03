# Binary Search (Python)
# https://www.algoexpert.io/questions/binary-search
# Time Complexity: O(log(n)) n is the length of array
# Space Complexity: O(1)

def binarySearch(array, target):
    lo = 0
    hi = len(array) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if array[mid] < target:
            lo = mid + 1
        elif array[mid] > target:
            hi = mid - 1
        else:
            return mid
    return -1
