# Caesar Cipher Encryptor (Python)
# https://www.algoexpert.io/questions/caesar-cipher-encryptor
# Time Complexity: O(n) n is the length of string
# Space Complexity: O(n)

def caesarCipherEncryptor(string, key):
    return ''.join(chr((ord(character) + key - 97) % 26 + 97) for character in string)
    
