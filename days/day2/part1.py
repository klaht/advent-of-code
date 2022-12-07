victory = [('C', 'X'), ('A', 'Y'), ('B', 'Z')]
draw = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]


# A = rock, 1p. B = paper, 2p. C = scissors, 3p.
# X = rock, Y = paper, Z = scissors
# Lost = 0. Draw = 3. Victory = 6.

total_score = 0

with open("tournament", "r") as file:
    for i in file.readlines():
        current_game = (i.strip()[0], i.strip()[2])

        if current_game in victory:
            total_score += 6
        elif current_game in draw:
            total_score += 3

        if current_game[1] == "X":
            total_score += 1
        elif current_game[1] == "Y":
            total_score += 2
        else:
            total_score += 3

print(total_score)
