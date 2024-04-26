# Tournament Winner (Python)
# https://www.algoexpert.io/questions/tournament-winner
# Time Complexity: O(n) n is the number of competitions
# Space Complexity: O(k) k is the number of teams
def tournamentWinner(competitions, results):
    tournament = {}
    for i, competition in enumerate(competitions):
        if results[i]:
            tournament[competition[0]] = tournament.get(competition[0], 0) + 1
        else:
            tournament[competition[1]] = tournament.get(competition[1], 0) + 1
    return max(tournament, key=tournament.get)
