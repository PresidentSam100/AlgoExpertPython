# Common Characters (Python)
# https://www.algoexpert.io/questions/common-characters
# Time Complexity: O(n * m) n is the number of strings, m is the length of the longest word
# Space Complexity: O(c) c is the number of unique characters across all the strings

def commonCharacters(strings):
    letterCounts = {}
    commonCharacters = []
    for string in strings:
        for character in set(string):
            letterCounts[character] = letterCounts.get(character, 0) + 1
    for letter, count in letterCounts.items():
        if count == len(strings):
            commonCharacters.append(letter)
    return commonCharacters
