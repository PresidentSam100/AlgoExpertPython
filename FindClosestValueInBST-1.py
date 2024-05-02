# Find Closest Value in BST (Python)
# https://www.algoexpert.io/questions/find-closest-value-in-bst
# Average Time Complexity: O(log(n)) n is the number of nodes in BST
# Worst Time Complexity: O(n)
# Average Space Complexity: O(log(n))
# Worst Space Complexity: O(n)

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - tree.value) < abs(target - closest):
        closest = tree.value
    if target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    elif target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    else:
        return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
