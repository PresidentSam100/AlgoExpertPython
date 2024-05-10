# Move Element To End (Python)
# https://www.algoexpert.io/questions/move-element-to-end
# Time Complexity: O(n) n is the length of array
# Space Complexity: O(1)

def moveElementToEnd(array, toMove):
    left = 0
    for index in range(len(array)):
        if array[index] != toMove:
            array[index], array[left] = array[left], array[index]
            left += 1
    return array
