# Transpose Matrix (Python)
# https://www.algoexpert.io/questions/transpose-matrix
# Time Complexity: O(w * h) w is the width of matrix, h is the height of matrix
# Space Complexity: O(w * h)
def transposeMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            transpose[col][row] = matrix[row][col]
    return transpose
