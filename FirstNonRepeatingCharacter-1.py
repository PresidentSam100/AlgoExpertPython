# First Non-Repeating Character (Python)
# https://www.algoexpert.io/questions/first-non-repeating-character
# Time Complexity: O(n) n is the length of string
# Space Complexity: O(1)

def firstNonRepeatingCharacter(string):
    for characterIndex in range(len(string)):
        unique = True
        for checkIndex in range(len(string)):
            if characterIndex != checkIndex and string[characterIndex] == string[checkIndex]:
                unique = False
                break
        if unique:
            return characterIndex
    return -1
