# Node Depths (Python)
# https://www.algoexpert.io/questions/node-depths
# Time Complexity: O(n) n is the number of nodes in BinaryTree
# Space Complexity: O(h) h is the height of BinaryTree
def nodeDepths(root):
    depthSum = 0
    stack = [[root, 0]]
    while stack:
        curr = stack.pop()
        node = curr[0]
        depth = curr[1]
        if node.right:
            stack.append([node.right, depth + 1])
        if node.left:
            stack.append([node.left, depth + 1])
        depthSum += depth
    return depthSum


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
