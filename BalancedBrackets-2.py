# Balanced Brackets (Python)
# https://www.algoexpert.io/questions/balanced-brackets
# Time Complexity: O(n) n is the length of string
# Space Complexity: O(n)

def balancedBrackets(string):
    stack = []
    open = "([{"
    close = ")]}"
    for bracket in string:
        if bracket in open:
            stack.append(bracket)
        elif bracket in close:
            if not stack or stack[-1] != open[close.index(bracket)]:
                return False
            else:
                stack.pop()
    return len(stack) == 0
