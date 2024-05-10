# Levenshtein Distance (Python)
# https://www.algoexpert.io/questions/levenshtein-distance
# Time Complexity: O(n * m) n is the length of str1, m is the length of str2
# Space Complexity: O(n * m)

def levenshteinDistance(str1, str2):
    n = len(str1) + 1
    m = len(str2) + 1
    edits = [[(x + y) for x in range(m)] for y in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if str1[i - 1] == str2[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = 1 + min(edits[i - 1][j - 1], edits[i - 1][j], edits[i][j - 1])
    return edits[-1][-1]
