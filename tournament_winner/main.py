def tournamentWinner(competitions, results):
    # each array in competitions is of the form: [home_team, away_team]
    # if results[i] = 1 => home team won
    # if results[i] = 0 => away team won

    points_table = {}
    winner_team, max_points = None, 0
    for (competition, result) in zip(competitions, results):

        # updating points table
        (winner, loser) = (competition[0], competition[1]) if result == 1 else (competition[1], competition[0])
        points_table[winner] = points_table.get(winner,0) + 3
        points_table[loser] = points_table.get(loser,0)

        # current winning team so far
        if points_table[winner] > max_points:
            winner_team, max_points = winner, points_table[winner]

    # final_winner, max_points = None, 0
    # for (winner,points) in points_table.items():
    #     if points > max_points: 
    #         final_winner,max_points = winner, points
    
    return winner_team


competitions = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"]
]

results = [0,1,1]

print(tournamentWinner(competitions, results))