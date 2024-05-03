# First Non-Repeating Character (Python)
# https://www.algoexpert.io/questions/first-non-repeating-character
# Time Complexity: O(n) n is the length of string
# Space Complexity: O(1)

def firstNonRepeatingCharacter(string):
    counts = {} 
    for character in string:
        counts[character] = counts.get(character, 0) + 1
    for letterIndex in range(len(string)):
        if counts[string[letterIndex]] == 1:
            return letterIndex
    return -1
