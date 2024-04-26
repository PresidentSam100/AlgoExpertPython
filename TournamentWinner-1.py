# Tournament Winner (Python)
# https://www.algoexpert.io/questions/tournament-winner
# Time Complexity: O(n) n is the number of competitions
# Space Complexity: O(k) k is the number of teams
def tournamentWinner(competitions, results):
    tournament = {}
    for i in range(len(competitions)):
        if results[i] == 0:
            tournament[competitions[i][1]] = tournament.get(competitions[i][1], 0) + 1
        elif results[i] == 1:
            tournament[competitions[i][0]] = tournament.get(competitions[i][0], 0) + 1
    return max(tournament, key=tournament.get)
