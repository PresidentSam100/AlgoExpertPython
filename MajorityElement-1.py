# Majority Element (Python)
# https://www.algoexpert.io/questions/majority-element
# Time Complexity: O(n) n is length of array
# Space Complexity: O(1)

def majorityElement(array):
    majorityElem = array[0]
    majorityCount = 1
    for index in range(1, len(array)):
        currElem = array[index]
        if majorityCount == 0:
            majorityElem = currElem
            majorityCount = 1
        elif currElem == majorityElem:
            majorityCount += 1
        else:
            majorityCount -= 1
    return majorityElem
