# Class Photos (Python)
# https://www.algoexpert.io/questions/class-photos
# Time Complexity: O(n * log(n)) n is the number of students
# Space Complexity: O(1)

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    condition = "redShirt >= blueShirt" if redShirtHeights[0] < blueShirtHeights[0] else "redShirt <= blueShirt"
    for redShirt, blueShirt in zip(redShirtHeights, blueShirtHeights):
        if eval(condition):
            return False
    return True
