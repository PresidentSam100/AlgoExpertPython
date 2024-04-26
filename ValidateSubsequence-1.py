# Validate Subsequence (Python)
# https://www.algoexpert.io/questions/validate-subsequence
# Time Complexity: O(n) n is length of array
# Space Complexity: O(1)
def isValidSubsequence(array, sequence):
    sequenceIndex = 0
    arrayIndex = 0
    while arrayIndex < len(array) and sequenceIndex < len(sequence):
        if array[arrayIndex] == sequence[sequenceIndex]:
            sequenceIndex += 1
        arrayIndex += 1
    return sequenceIndex == len(sequence)
