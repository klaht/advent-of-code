victory = {'C': 'A',
           'A': 'B',
           'B': 'C'
           }

draw = {'A': 'A',
        'B': 'B',
        'C': 'C'}

lose = {'A': 'C',
        'B': 'A',
        'C': 'B'}

# A = rock, 1p. B = paper, 2p. C = scissors, 3p.
# X = lose, Y = draw, Z = win
# Lost = 0. Draw = 3. Victory = 6.

total_score = 0

with open("tournament", "r") as file:
    for i in file.readlines():
        current_game = (i.strip()[0], i.strip()[2])

        # victory
        if current_game[1] == "Z":
            chosen_shape = victory[current_game[0]]
            total_score += 6
        # draw
        elif current_game[1] == "Y":
            chosen_shape = draw[current_game[0]]
            total_score += 3
        # lose
        else:
            chosen_shape = lose[current_game[0]]

        if chosen_shape == "A":
            total_score += 1
        elif chosen_shape == "B":
            total_score += 2
        else:
            total_score += 3

print(total_score)
