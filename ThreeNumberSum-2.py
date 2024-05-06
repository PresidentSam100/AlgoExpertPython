# Three Number Sum (Python)
# https://www.algoexpert.io/questions/three-number-sum
# Time Complexity: O(n^3) n is the length of array
# Space Complexity: O(n)

def threeNumberSum(array, targetSum):
    array.sort()
    threeNumSums = []
    for index in range(len(array) - 2):
        left = index + 1
        right = len(array) - 1
        while left < right:
            tempSum = array[index] + array[left] + array[right]
            if tempSum < targetSum:
                left += 1
            elif tempSum > targetSum:
                right -= 1
            else:
                threeNumSums.append([array[index], array[left], array[right]])
                left += 1
                right -= 1
    return threeNumSums
