# Three Number Sum (Python)
# https://www.algoexpert.io/questions/three-number-sum
# Time Complexity: O(n^3) n is the length of array
# Space Complexity: O(n)

def threeNumberSum(array, targetSum):
    array.sort()
    threeNumSums = []
    for index1 in range(len(array) - 2):
        for index2 in range(index1 + 1, len(array) - 1):
            for index3 in range(index2 + 1, len(array)):
                if array[index1] + array[index2] + array[index3] == targetSum:
                    threeNumSums.append([array[index1], array[index2], array[index3]])
    return threeNumSums
