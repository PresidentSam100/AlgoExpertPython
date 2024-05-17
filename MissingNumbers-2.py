# Missing Numbers (Python)
# https://www.algoexpert.io/questions/missingNumbers
# Time Complexity: O(n) n is number of nums
# Space Complexity: O(1)

def missingNumbers(nums):
    n = len(nums) + 2
    expectedSum = n * (n + 1) / 2
    arraySum = sum(nums)
    totalMissing = expectedSum - arraySum
    averageMissing = totalMissing // 2
    expectedLower = averageMissing * (averageMissing + 1) / 2
    expectedUpper = expectedSum - expectedLower
    for num in nums:
        if num <= averageMissing:
            expectedLower -= num
        else:
            expectedUpper -= num
    return [expectedLower, expectedUpper]
