# Number Of Ways To Traverse Graph (Python)
# https://www.algoexpert.io/questions/number-of-ways-to-traverse-graph
# Time Complexity: O(w + h) w is the graph width, h is the graph height
# Space Complexity: O(1)

import math
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    return math.comb(width + height - 2, width - 1)
