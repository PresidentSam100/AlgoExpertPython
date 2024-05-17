# Missing Numbers (Python)
# https://www.algoexpert.io/questions/missingNumbers
# Time Complexity: O(n) n is length of nums array
# Space Complexity: O(n)

def missingNumbers(nums):
    setNums = set(nums)
    missing = []
    for num in range(1, len(nums) + 3):
        if num not in setNums:
            missing.append(num)
    return missing
