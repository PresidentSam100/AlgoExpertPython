# Palindrom Check (Python)
# https://www.algoexpert.io/questions/palindrome-check
# Time Complexity: O(n) n is the length of string
# Space Complexity: O(1)

def isPalindrome(string):
    n = len(string)
    for index in range(n // 2):
        if string[index] != string[n - 1 - index]:
            return False
    return True
