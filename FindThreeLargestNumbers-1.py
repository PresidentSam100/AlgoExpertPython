# Find Three Largest Numbers (Python)
# https://www.algoexpert.io/questions/find-three-largest-numbers
# Time Complexity: O(n) n is the length of array
# Space Complexity: O(1)

def findThreeLargestNumbers(array):
    largestThree = [float('-inf')] * 3
    for number in array:
        if number > largestThree[0]:
            largestThree[0] = number
        if largestThree[0] > largestThree[1]:
            largestThree[0], largestThree[1] = largestThree[1], largestThree[0] 
        if largestThree[1] > largestThree[2]:
            largestThree[1], largestThree[2] = largestThree[2], largestThree[1] 
    return largestThree
