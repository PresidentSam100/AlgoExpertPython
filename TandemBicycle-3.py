# Tandem Bicycle (Python)
# https://www.algoexpert.io/questions/tandem-bicycle
# Time Complexity: O(n * log(n)) n is the number of tandem bicycles
# Space Complexity: O(1)

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse = fastest)
    return sum(max(red, blue) for red, blue in zip(redShirtSpeeds, blueShirtSpeeds))
