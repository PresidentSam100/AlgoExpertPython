# Minimum Waiting Time (Python)
# https://www.algoexpert.io/questions/minimum-waiting-time
# Time Complexity: O(n) n is the number of queries
# Space Complexity: O(1)

def minimumWaitingTime(queries):
    queries.sort()
    waiting = 0
    temp = len(queries)
    for query in queries:
        temp -= 1
        waiting += query * temp
    return waiting
