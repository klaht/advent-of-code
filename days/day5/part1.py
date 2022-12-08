# return array of stacks from the input file
def create_stacks():
    stacks = []
    line_index = 0

    with open("input", "r") as file:
        for i in file.readlines():
            if i.strip()[0] == "1":
                break
            for a in i:
                if a.isalpha(): # fill up the array of stacks with char values from input
                    while line_index // 4 > len(stacks) - 1:
                        stacks.append([])
                    stacks[line_index // 4].append(a)

                line_index += 1

            line_index = 0
        file.close()
    for i in stacks:
        i.reverse() # reverse the stacks so the first ones added are on the top

    return stacks

# move the values around the stacks from the commands from input file
def conf_stacks(stacks):
    with open("input", "r") as file:
        for i in file.readlines():
            if i[0:4] == "move":
                splitted = i.strip().split(" ")

                amount = splitted[1]
                sender_stack = splitted[3]
                receiver_stack = splitted[5]

                for value in range(int(amount)):
                    current = stacks[int(sender_stack) - 1].pop()
                    stacks[int(receiver_stack) - 1].append(current)

    return stacks


stacks = conf_stacks(create_stacks())

answer = ""
for i in stacks: # get the values from top of the stack
    answer += i[-1]

print(answer)
