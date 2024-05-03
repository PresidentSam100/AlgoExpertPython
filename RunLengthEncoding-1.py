# Run-Length Encoding (Python)
# https://www.algoexpert.io/questions/run-length-encoding
# Time Complexity: O(n) n is the length of string
# Space Complexity: O(n)

def runLengthEncoding(string):
    current = string[0]
    count = 0
    encoding = ""
    for character in string:
        if count >= 9 or character != current:
            encoding += str(count) + str(current)
            current = character
            count = 1
        else:
            count += 1
    return encoding + str(count) + str(current)
