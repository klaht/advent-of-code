lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = lowercase.upper()

group_rucksacks = ["", "", ""]
priority_value = 0
group_divider = 0

with open("items", "r") as file:
    for i in file.readlines():
        length = len(i.strip())

        # save rucksacks to groups of 3
        if group_divider < 3:
            group_rucksacks[group_divider] = i.strip()
        else:  # group is full
            group_divider = 0
            group_rucksacks[group_divider] = i.strip()

        # when group is full, get the common item from it
        if group_divider == 2:

            for char in group_rucksacks[0]:
                if char in group_rucksacks[1] and char in group_rucksacks[2]:
                    alphabet_location = lowercase.index(char.lower()) + 1
                    if char.islower():
                        priority_value += alphabet_location
                    else:
                        priority_value += alphabet_location + 26
                    break

        group_divider += 1

print(priority_value)
