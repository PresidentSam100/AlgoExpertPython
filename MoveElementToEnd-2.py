# Move Element To End (Python)
# https://www.algoexpert.io/questions/move-element-to-end
# Time Complexity: O(n) n is the length of array
# Space Complexity: O(1)

def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] == toMove and array[right] != toMove:
            array[left], array[right] = array[right], array[left]
        if array[left] != toMove:
            left += 1
        if array[right] == toMove:
            right -= 1
    return array
