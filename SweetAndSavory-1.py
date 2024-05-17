# Sweet And Savory (Python)
# https://www.algoexpert.io/questions/sweet-and-savory
# Time Complexity: O(n * log(n)) n is the number of dishes
# Space Complexity: O(1)

def sweetAndSavory(dishes, target):
    dishes.sort()
    sweetIndex = 0
    savoryIndex = len(dishes) - 1
    flavorProfile = [0, 0]
    bestFlavor = float('-inf')
    while sweetIndex < savoryIndex:
        sweetDish = dishes[sweetIndex]
        savoryDish = dishes[savoryIndex]
        if sweetDish >= 0 or savoryDish <= 0:
            break
        flavor = sweetDish + savoryDish
        if flavor <= target and flavor > bestFlavor:
            flavorProfile = [sweetDish, savoryDish]
            bestFlavor = flavor
        if flavor <= target:
            sweetIndex += 1
        else:
            savoryIndex -= 1
    return flavorProfile
