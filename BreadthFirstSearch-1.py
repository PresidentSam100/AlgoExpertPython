# Breadth-first Search (Python)
# https://www.algoexpert.io/questions/breadth-first-search
# Time Complexity: O(v + e) v is the number of vertices, e is the number of edges
# Space Complexity: O(v)


# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while queue:
            node = queue.pop(0)
            array.append(node.name)
            for child in node.children:
                queue.append(child)
        return array
