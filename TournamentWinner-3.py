# Tournament Winner (Python)
# https://www.algoexpert.io/questions/tournament-winner
# Time Complexity: O(n) n is the number of competitions
# Space Complexity: O(k) k is the number of teams
def tournamentWinner(competitions, results):
    tournament = {}
    for i, competition in enumerate(competitions):
        winner = competition[results[i] ^ 1]
        tournament[winner] = tournament.get(winner, 0) + 1
    return max(tournament, key=tournament.get)
