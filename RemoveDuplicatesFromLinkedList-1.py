# Remove Duplicates From Linked List (Python)
# https://www.algoexpert.io/questions/remove-duplicates-from-linked-list
# Time Complexity: O(n) n is number of nodes in linkedList
# Space Complexity: O(1)

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    current = linkedList
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return linkedList
