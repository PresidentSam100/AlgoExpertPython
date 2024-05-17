# Majority Element (Python)
# https://www.algoexpert.io/questions/majority-element
# Time Complexity: O(n) n is length of array
# Space Complexity: O(1)

def majorityElement(array):
    majorityElem = 0
    for currBit in range(32):
        currBitVal = 1 << currBit
        oneBitCount = 0
        for num in array:
            if num & currBitVal != 0:
                oneBitCount += 1
        if oneBitCount > len(array) / 2:
            majorityElem += currBitVal
    return majorityElem
