# Semordnilap (Python)
# https://www.algoexpert.io/questions/semordnilap
# Time Complexity: O(n * m) n is the number of words, m is the length of the longest word
# Space Complexity: O(n * m)

def semordnilap(words):
    wordSet = set()
    pairs = []
    for word in words:
        if word in wordSet:
            pairs.append([word, word[::-1]])
        wordSet.add(word[::-1])
    return pairs
