# Zero Sum Subarray (Python)
# https://www.algoexpert.io/questions/zero-sum-subarray
# Time Complexity: O(n) n is the length of nums
# Space Complexity: O(n)

def zeroSumSubarray(nums):
    sums = set([0])
    currSum = 0
    for num in nums:
        currSum += num
        if currSum in sums:
            return True
        sums.add(currSum)
    return False
