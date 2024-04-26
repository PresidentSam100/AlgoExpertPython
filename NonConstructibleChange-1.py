# Non-Constructible Change (Python)
# https://www.algoexpert.io/questions/non-constructible-change
# Time Complexity: O(nlogn) n is number of coins
# Space Complexity: O(1)
def nonConstructibleChange(coins):
    coins.sort()
    change = 0
    for coin in coins:
        if coin > change + 1:
            break
        change += coin
    return change + 1
