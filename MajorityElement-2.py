# Majority Element (Python)
# https://www.algoexpert.io/questions/majority-element
# Time Complexity: O(n) n is length of array
# Space Complexity: O(1)

def majorityElement(array):
    majorityElem = None
    majorityCount = 0
    for currElem in array:
        if majorityCount == 0:
            majorityElem = currElem
        if currElem == majorityElem:
            majorityCount += 1
        else:
            majorityCount -= 1
    return majorityElem
