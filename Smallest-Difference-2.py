# Smallest Difference (Python)
# https://www.algoexpert.io/questions/smallest-difference
# Time Complexity: O(n * log(n) + m * log(m)) n is the length of arrayOne, m is the length of arrayTwo
# Space Complexity: O(1)

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    left = 0
    right = 0
    pair = [0, float('inf')]
    while left < len(arrayOne) and right < len(arrayTwo):
        diff = arrayOne[left] - arrayTwo[right]
        if abs(diff) < abs(pair[1] - pair[0]):
            pair[0] = arrayOne[left]
            pair[1] = arrayTwo[right]
        if diff < 0:
            left += 1
        elif diff > 0:
            right += 1
        else:
            return [arrayOne[left], arrayTwo[right]]
    return pair
