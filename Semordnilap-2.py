# Semordnilap (Python)
# https://www.algoexpert.io/questions/semordnilap
# Time Complexity: O(n * m) n is the number of words, m is the length of the longest word
# Space Complexity: O(n * m)

def semordnilap(words):
    wordSet = set(words)
    pairs = []
    for word in words:
        reverse = word[::-1]
        if reverse in wordSet and word != reverse:
            pairs.append([word, reverse])
            wordSet.remove(word)
            wordSet.remove(reverse)
    return pairs
