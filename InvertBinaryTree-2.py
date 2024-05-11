# Invert Binary Tree (Python)
# https://www.algoexpert.io/questions/invert-binary-tree
# Time Complexity: O(n) n is the number of nodes in tree
# Space Complexity: O(d) d is the depth of tree

def invertBinaryTree(tree):
    if tree:
        tree.left, tree.right = tree.right, tree.left
        invertBinaryTree(tree.right)
        invertBinaryTree(tree.left)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
