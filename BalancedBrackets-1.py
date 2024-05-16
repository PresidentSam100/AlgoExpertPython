# Balanced Brackets (Python)
# https://www.algoexpert.io/questions/balanced-brackets
# Time Complexity: O(n) n is the length of string
# Space Complexity: O(n)

def balancedBrackets(string):
    stack = []
    for bracket in string:
        if stack and stack[-1] == '(' and bracket == ')':
            stack.pop()
        elif stack and stack[-1] == '[' and bracket == ']':
            stack.pop()
        elif stack and stack[-1] == '{' and bracket == '}':
            stack.pop()
        elif bracket in "()[]{}":
            stack.append(bracket)
    return len(stack) == 0
