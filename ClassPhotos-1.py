# Class Photos (Python)
# https://www.algoexpert.io/questions/class-photos
# Time Complexity: O(n * log(n)) n is the number of students
# Space Complexity: O(1)

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    result = 0
    for redShirt, blueShirt in zip(redShirtHeights, blueShirtHeights):
        if redShirt < blueShirt:
            result += 1
        elif redShirt > blueShirt:
            result -= 1
    return abs(result) == len(redShirtHeights)
