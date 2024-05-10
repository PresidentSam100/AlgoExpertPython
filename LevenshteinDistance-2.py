# Levenshtein Distance (Python)
# https://www.algoexpert.io/questions/levenshtein-distance
# Time Complexity: O(n * m) n is the length of str1, m is the length of str2
# Space Complexity: O(min(n, m))

def levenshteinDistance(str1, str2):
    bigger = str1 if len(str1) > len(str2) else str2
    smaller = str1 if len(str1) <= len(str2) else str2
    editsEven = [x for x in range(len(smaller) + 1)]
    editsOdd = [x for x in range(len(smaller) + 1)]
    for i in range(1, len(bigger) + 1):
        editCurr = editsOdd if i % 2 == 1 else editsEven
        editPrev = editsEven if i % 2 == 1 else editsOdd
        editCurr[0] = i
        for j in range(1, len(smaller) + 1):
            if bigger[i - 1] == smaller[j - 1]:
                editCurr[j] = editPrev[j - 1]
            else:
                editCurr[j] = 1 + min(editPrev[j - 1], editPrev[j], editCurr[j - 1])
    return editsEven[-1] if len(bigger) % 2 == 0 else editsOdd[-1]
