# Generate Document (Python)
# https://www.algoexpert.io/questions/generate-document
# Time Complexity: O(n + m + c) n is the number of characters, m is the length of document, c is the number of unique characters across the inputs
# Space Complexity: O(c)

def generateDocument(characters, document):
    letterCounts = {}
    for charLetter in characters:
        letterCounts[charLetter] = letterCounts.get(charLetter, 0) + 1
    for docLetter in document:
        letterCounts[docLetter] = letterCounts.get(docLetter, 0) - 1
    for count in letterCounts.values():
        if count < 0:
            return False
    return True
