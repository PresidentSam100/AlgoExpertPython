# Common Characters (Python)
# https://www.algoexpert.io/questions/common-characters
# Time Complexity: O(n * m) n is the number of strings, m is the length of the longest word
# Space Complexity: O(m)

def commonCharacters(strings):
    smallestString = strings[0]
    common = set(smallestString)
    for string in strings:
        if len(smallestString) > len(string):
            smallestString = string
    for string in strings:
        for character in list(common):
            if character not in set(string):
                common.remove(character)
    return list(common)
