values = [(0, 0), (0, 0)]
amount = 0

with open("sections", "r") as file:
    for i in file.readlines():
        i = i.strip().split(',')
        values[0] = (i[0].split('-'))
        values[1] = i[1].split('-')

        if int(values[0][0]) >= int(values[1][0]) and int(values[0][1]) <= int(values[1][1]): # second includes first
            amount += 1
        elif int(values[1][0]) >= int(values[0][0]) and int(values[1][1]) <= int(values[0][1]): # first includes second
            amount += 1

print(amount)