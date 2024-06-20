# Largest Range (Python)
# https://www.algoexpert.io/questions/largest-range
# Time Complexity: O(n) n is the length of array
# Space Complexity: O(n)

def largestRange(array):
    nums = {}
    range = [-1, -1]
    for num in array:
        nums[num] = False
    for num in array:
        if not nums[num]:
            left = num
            right = num
            nums[num] = True
            while left - 1 in nums and nums[left - 1]:
                nums[left - 1] = True
                left -= 1
            while right + 1 in nums and nums[right + 1]:
                nums[right + 1] = True
                right += 1
            if right - left >= range[1] - range[0]:
                range = [left, right]
    return range
