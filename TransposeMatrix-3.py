# Transpose Matrix (Python)
# https://www.algoexpert.io/questions/transpose-matrix
# Time Complexity: O(w * h) w is the width of matrix, h is the height of matrix
# Space Complexity: O(w * h)
def transposeMatrix(matrix):
    return list(zip(*matrix))
