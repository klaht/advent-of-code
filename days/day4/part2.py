values = [(0, 0), (0, 0)]
amount = 0

with open("sections", "r") as file:
    for i in file.readlines():
        i = i.strip().split(',')
        values[0] = (i[0].split('-'))
        values[1] = i[1].split('-')

        # first starts before second starts and ends after it
        if int(values[0][0]) <= int(values[1][0]) <= int(values[0][1]):
            amount += 1

        # first starts before second ends, and ends before first starts
        elif int(values[0][0]) <= int(values[1][1]) and int(values[0][1]) >= int(values[1][0]):
            amount += 1


print(amount)