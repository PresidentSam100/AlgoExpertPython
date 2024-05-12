# Three Number Sum (Python)
# https://www.algoexpert.io/questions/three-number-sum
# Time Complexity: O(n^2) n is the length of array
# Space Complexity: O(n)

def threeNumberSum(array, targetSum):
    n = len(array)
    array.sort()
    threeSums = []
    for index in range(len(array) - 2):
        num1 = array[index]
        left = index + 1
        right = n - 1
        while left < right:
            num2 = array[left]
            num3 = array[right]
            tempSum = num1 + num2 + num3
            if tempSum < targetSum:
                left += 1
            elif tempSum > targetSum:
                right -= 1
            else:
                left += 1
                right -= 1
                threeSums.append([num1, num2, num3])
    return threeSums
