# Longest Peak (Python)
# https://www.algoexpert.io/questions/longest-peak
# Time Complexity: O(n) n is the length of array
# Space Complexity: O(1)

def longestPeak(array):
    increaseLen = 0
    decreaseLen = 0
    longestPeak = 0
    for index in range(1, len(array)):
        if array[index - 1] < array[index]:
            if decreaseLen != 0:
                increaseLen = 0
                decreaseLen = 0
            increaseLen += 1
        elif array[index - 1] > array[index] and increaseLen > 0:
            decreaseLen += 1
            longestPeak = max(longestPeak, increaseLen + decreaseLen + 1)
        else:
            increaseLen = 0
            decreaseLen = 0
    return longestPeak
