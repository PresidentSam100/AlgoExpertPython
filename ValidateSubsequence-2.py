# Validate Subsequence (Python)
# https://www.algoexpert.io/questions/validate-subsequence
# Time Complexity: O(n) n is length of array
# Space Complexity: O(1)
def isValidSubsequence(array, sequence):
    sequenceIndex = 0
    for num in array:
        if num == sequence[sequenceIndex]:
            sequenceIndex += 1
        if sequenceIndex == len(sequence):
            return True
    return False
