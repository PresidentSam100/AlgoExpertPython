# Invert Binary Tree (Python)
# https://www.algoexpert.io/questions/invert-binary-tree
# Time Complexity: O(n) n is the number of nodes in tree
# Space Complexity: O(n)

def invertBinaryTree(tree):
    queue = [tree]
    while queue:
        current = queue.pop(0)
        if current:
            current.left, current.right = current.right, current.left
            queue.append(current.right)
            queue.append(current.left)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
