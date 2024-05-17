# Missing Numbers (Python)
# https://www.algoexpert.io/questions/missingNumbers
# Time Complexity: O(n) n is number of nums
# Space Complexity: O(1)

def missingNumbers(nums):
    n = len(nums) + 2
    expectedXOR = 0
    for i in range(n + 1):
        expectedXOR ^= i
        if i < len(nums):
            expectedXOR ^= nums[i]
    missing = [0, 0]
    setBit = -expectedXOR & expectedXOR
    for i in range(n + 1):
        if i & setBit == 0:
            missing[0] ^= i
        else:
            missing[1] ^= i
        if i < len(nums):
            if nums[i] & setBit == 0:
                missing[0] ^= nums[i]
            else:
                missing[1] ^= nums[i]
    return sorted(missing)
