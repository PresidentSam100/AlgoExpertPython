# Four Number Sum (Python)
# https://www.algoexpert.io/questions/four-number-sum
# Average Time Complexity: O(n^2) n is the length of array
# Average Space Complexity: O(n^2)
# Worst Time Complexity: O(n^3)
# Worst Space Complexity: O(n^2)

def fourNumberSum(array, targetSum):
    fourSum = []
    pairs = {}
    for index1 in range(1, len(array) - 1):
        for index2 in range(index1 + 1, len(array)):
            tempSum = array[index1] + array[index2]
            if targetSum - tempSum in pairs:
                for pair in pairs[targetSum - tempSum]:
                    fourSum.append(pair + [array[index1], array[index2]])
        for index3 in range(index1):
            currSum = array[index1] + array[index3]
            if currSum not in pairs:
                pairs[currSum] = [[array[index1], array[index3]]]
            else:
                pairs[currSum].append([array[index1], array[index3]])
    return fourSum
