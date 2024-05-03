# Caesar Cipher Encryptor (Python)
# https://www.algoexpert.io/questions/caesar-cipher-encryptor
# Time Complexity: O(n) n is the length of string
# Space Complexity: O(1)

def caesarCipherEncryptor(string, key):
    caesarString = ""
    for character in string:
        caesarString += chr((ord(character) + key - 97) % 26 + 97)
    return caesarString
