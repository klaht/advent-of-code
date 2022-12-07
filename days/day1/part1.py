highest = 0
second_highest = 0
third_highest = 0
current = 0

with open("calories", "r") as file:
    for i in file.readlines():
        if i.strip() != "":
            current += int(i.strip())
        else:
            if current > highest:
                highest = current
            current = 0
    file.close()
print(highest)