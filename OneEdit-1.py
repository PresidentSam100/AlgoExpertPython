# One Edit (Python)
# https://www.algoexpert.io/questions/one-edit
# Time Complexity: O(min(n, m)) n is the length of stringOne, m is the length of stringTwo
# Space Complexity: O(1)

def oneEdit(stringOne, stringTwo):
    if abs(len(stringOne) - len(stringTwo)) > 1:
        return False
    if stringOne == stringTwo:
        return True
    index1 = 0
    index2 = 0
    edited = False
    while index1 < len(stringOne) and index2 < len(stringTwo):
        if stringOne[index1] != stringTwo[index2]:
            if edited:
                return False
            edited = True
            if len(stringOne) == len(stringTwo) + 1:
                index2 -= 1
            elif len(stringOne) + 1 == len(stringTwo):
                index1 -= 1
        index1 += 1
        index2 += 1
    return True
