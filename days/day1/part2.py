highest = 0
second_highest = 0
third_highest = 0
current = 0

with open("calories", "r") as file:
    for i in file.readlines():
        if i.strip() != "":
            current += int(i.strip())
        else:
            if current > third_highest:
                third_highest = current
                if third_highest > second_highest:
                    current = second_highest
                    second_highest = third_highest
                    third_highest = current
                    if second_highest > highest:
                        current = highest
                        highest = second_highest
                        second_highest = current
            current = 0
    file.close()

print(highest + second_highest + third_highest)
