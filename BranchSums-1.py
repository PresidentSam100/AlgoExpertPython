# Branch Sums (Python)
# https://www.algoexpert.io/questions/branch-sums
# Time Complexity: O(n) n is the number of nodes in BinaryTree
# Space Complexity: O(n)


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    dfs = [[root, 0]]
    while dfs:
        curr = dfs.pop()
        node = curr[0]
        sum = curr[1]
        if not node.left and not node.right:
            sums.append(sum + node.value)
            continue
        if node.right:
            dfs.append([node.right, sum + node.value])
        if node.left:
            dfs.append([node.left, sum + node.value])
    return sums
    
