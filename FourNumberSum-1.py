# Four Number Sum (Python)
# https://www.algoexpert.io/questions/four-number-sum
# Time Complexity: O(n^4) n is the length of array
# Space Complexity: O(n^4)

def fourNumberSum(array, targetSum):
    fourSum = []
    for index1 in range(len(array) - 3):
        for index2 in range(index1 + 1, len(array) - 2):
            for index3 in range(index2 + 1, len(array) - 1):
                for index4 in range(index3 + 1, len(array)):
                    if array[index1] + array[index2] + array[index3] + array[index4] == targetSum:
                        fourSum.append([array[index1], array[index2], array[index3], array[index4]])
    return fourSum
