# Two Number Sum (Python)
# https://www.algoexpert.io/questions/two-number-sum
# Time Complexity: O(nlogn) n is length of array
# Space Complexity: O(1)
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        sum = array[left] + array[right]
        if sum < targetSum:
            left += 1
        elif sum > targetSum:
            right -= 1
        else:
            return [array[left], array[right]]
    return []
