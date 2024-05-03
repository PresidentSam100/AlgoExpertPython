# Palindrom Check (Python)
# https://www.algoexpert.io/questions/palindrome-check
# Time Complexity: O(n) n is the length of string
# Space Complexity: O(1)

def isPalindrome(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True
