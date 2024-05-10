# Min Number Of Coins For Change (Python)
# https://www.algoexpert.io/questions/min-number-of-coins-for-change
# Time Complexity: O(n * d) n is the target amount, d is the number of coin denominations
# Space Complexity: O(n)

def minNumberOfCoinsForChange(n, denoms):
    coinCounts = [float("inf")] * (n + 1)
    coinCounts[0] = 0
    
    for denom in denoms:
        for index in range(len(coinCounts)):
            if index - denom >= 0:
                coinCounts[index] = min(coinCounts[index], coinCounts[index - denom] + 1)
    
    return coinCounts[n] if coinCounts[n] != float("inf") else -1
