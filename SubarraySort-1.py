# Subarray Sort (Python)
# https://www.algoexpert.io/questions/subarray-sort
# Time Complexity: O(n * log(n)) n is the length of array
# Space Complexity: O(n)

def subarraySort(array):
    arraySorted = array[:]
    arraySorted.sort()
    ans = [-1, -1]
    for i in range(len(array)):
        if array[i] != arraySorted[i]:
            if ans[0] == -1:
                ans[0] = i
            ans[1] = i
    return ans
