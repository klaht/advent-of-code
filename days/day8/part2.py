visible = 0
index = 0

trees = []

with open("input", "r") as file:
    for i in file.readlines():
        trees.append([])
        for tree in i.strip():
            trees[index].append(tree)
        index += 1

index = 0
length = len(trees)
visible = length * 2

x_index = 0
y_index = 0


visibility = False

ideal_tree_score = 0
current_tree_scores = [0, 0, 0, 0]
current_total_score = 0



for i in trees:
    for tree in i:

        #Check upwards
        current_y = y_index - 1
        for _ in range(0, y_index):
            if int(tree) > int(trees[current_y][x_index]):
                current_y -= 1
                current_tree_scores[0] += 1
            else:
                current_tree_scores[0] += 1
                break

        #Check downwards
        current_y = y_index + 1
        for _ in range(y_index, length-1):
            if int(tree) > int(trees[current_y][x_index]):
                current_y += 1
                current_tree_scores[1] += 1
            else:
                current_tree_scores[1] += 1
                break

        #Check to left
        current_x = x_index - 1
        for _ in range(0, x_index):
            if int(tree) > int(trees[y_index][current_x]):
                current_x -= 1
                current_tree_scores[2] += 1
            else:
                current_tree_scores[2] += 1
                break

        #Check to right
        current_x = x_index + 1
        for _ in range(x_index, len(trees[0])-1):
            if int(tree) > int(trees[y_index][current_x]):
                current_x += 1
                current_tree_scores[3] += 1
            else:
                current_tree_scores[3] += 1
                break

        current_total_score = current_tree_scores[0] * current_tree_scores[1] * current_tree_scores[2] * current_tree_scores[3]

        if current_total_score > ideal_tree_score:
            ideal_tree_score = current_total_score

        current_total_score = 0
        current_tree_scores = [0, 0, 0, 0]

        x_index += 1

    y_index += 1
    x_index = 0

print(ideal_tree_score)
