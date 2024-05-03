# Product Sum (Python)
# https://www.algoexpert.io/questions/product-sum
# Time Complexity: O(n) n is the number of elements in array and "special" arrays
# Space Complexity: O(d) d is the greatest depth of the "special" arrays

# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth = 1):
    sum = 0
    for elem in array:
        if type(elem) is list:
            sum += productSum(elem, depth + 1) * depth
        else:
            sum += elem * depth
    return sum
