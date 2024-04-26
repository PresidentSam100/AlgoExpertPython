# Two Number Sum (Python)
# https://www.algoexpert.io/questions/two-number-sum
# Time Complexity: O(n) n is length of array
# Space Complexity: O(n)
def twoNumberSum(array, targetSum):
    numSet = set()
    for num in array:
        if (targetSum - num in numSet):
            return [num, targetSum - num]
        else:
            numSet.add(num)
    return []
