# Largest Range (Python)
# https://www.algoexpert.io/questions/largest-range
# Time Complexity: O(n) n is the length of array
# Space Complexity: O(n)

def largestRange(array):
    nums = set(array)
    range = [0, float('-inf')]
    for num in nums:
        if num - 1 not in nums:
            next = num
            while next + 1 in nums:
                next += 1
            if next - num > range[1] - range[0]:
                range = [num, next]
    return range
