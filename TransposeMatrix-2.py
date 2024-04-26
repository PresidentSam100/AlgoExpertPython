# Transpose Matrix (Python)
# https://www.algoexpert.io/questions/transpose-matrix
# Time Complexity: O(w * h) w is the width of matrix, h is the height of matrix
# Space Complexity: O(w * h)
def transposeMatrix(matrix):
    transpose = []
    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        transpose.append(newRow)
    return transpose
