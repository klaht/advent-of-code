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



x_index = 1
y_index = 1

tree_visibility_directions = 0

visibility = False

for i in trees[1:-1]:
    visible += 2
    for tree in i[1:-1]:

        #Check upwards
        current_y = y_index - 1
        for _ in range(0, y_index):
            if int(tree) > int(trees[current_y][x_index]):
                current_y -= 1
                if current_y - 1 < -1:
                    tree_visibility_directions += 1
                    break
            else:
                break

        #Check downwards
        current_y = y_index + 1
        for _ in range(y_index, length-1):
            if int(tree) > int(trees[current_y][x_index]):
                current_y += 1
                if current_y + 1 > length:
                    tree_visibility_directions += 1
                    break
            else:
                break

        #Check to left
        current_x = x_index - 1
        for _ in range(0, x_index):
            if int(tree) > int(trees[y_index][current_x]):
                current_x -= 1
                if current_x < 0:
                    tree_visibility_directions += 1
                    break
            else:
                break

        #Check to right
        current_x = x_index + 1
        for _ in range(x_index, len(trees[0])-1):
            if int(tree) > int(trees[y_index][current_x]):
                current_x += 1
                if current_x + 1 > len(trees[0]):
                    tree_visibility_directions += 1
                    break
            else:
                break

        if tree_visibility_directions > 0:
            visible += 1
            tree_visibility_directions = 0

        x_index += 1
        visibility = False


    y_index += 1
    x_index = 1


print(visible)
