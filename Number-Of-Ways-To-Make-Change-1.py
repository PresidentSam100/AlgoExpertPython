# Number Of Ways To Make Change (Python)
# https://www.algoexpert.io/questions/number-of-ways-to-make-change
# Time Complexity: O(n * d) n is the target amount, d is the number of coin denominations
# Space Complexity: O(n)

def numberOfWaysToMakeChange(n, denoms):
    coinCounts = [0] * (n + 1)
    coinCounts[0] = 1
    
    for denom in denoms:
        for index in range(1, n + 1):
            if index - denom >= 0:
                coinCounts[index] += coinCounts[index - denom]

    return coinCounts[n]
