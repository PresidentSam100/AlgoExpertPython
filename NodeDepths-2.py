# Node Depths (Python)
# https://www.algoexpert.io/questions/node-depths
# Time Complexity: O(n) n is the number of nodes in BinaryTree
# Space Complexity: O(h) h is the height of BinaryTree
def nodeDepths(root, depth = 0):
    if not root:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
