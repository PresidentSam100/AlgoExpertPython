# Generate Document (Python)
# https://www.algoexpert.io/questions/generate-document
# Time Complexity: O(n + m) n is the number of characters, m is the length of document
# Space Complexity: O(c) c is the number of unique characters in characters string

def generateDocument(characters, document):
    letterCounts = {}
    for charLetter in characters:
        letterCounts[charLetter] = letterCounts.get(charLetter, 0) + 1
    for docLetter in document:
        if letterCounts.get(docLetter, 0) < 1:
            return False
        letterCounts[docLetter] -= 1
    return True
