# Middle Node (Python)
# https://www.algoexpert.io/questions/middle-node
# Time Complexity: O(n) n is number of nodes in linkedList
# Space Complexity: O(1)

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    fast = linkedList
    slow = linkedList
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
