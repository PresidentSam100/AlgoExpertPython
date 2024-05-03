# Tandem Bicycle (Python)
# https://www.algoexpert.io/questions/tandem-bicycle
# Time Complexity: O(n * log(n)) n is the number of tandem bicycles
# Space Complexity: O(1)

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    totalTandemSpeed = 0
    if fastest:
        for redShirtSpeed, blueShirtSpeed in zip(sorted(redShirtSpeeds), sorted(blueShirtSpeeds, reverse = True)):
            totalTandemSpeed += max(redShirtSpeed, blueShirtSpeed)
    else:
        for redShirtSpeed, blueShirtSpeed in zip(sorted(redShirtSpeeds), sorted(blueShirtSpeeds)):
            totalTandemSpeed += max(redShirtSpeed, blueShirtSpeed)
    return totalTandemSpeed
