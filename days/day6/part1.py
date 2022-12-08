def find_marker():
    buffer = []

    with open("input", "r") as file:
        for i in file.readlines():
            for index, c in enumerate(i):
                if len(buffer) == 4:
                    # add new value to buffer and swipe other values to the left
                    for x in range(3):
                        buffer[x] = buffer[x + 1]
                    buffer[3] = c

                    for z in buffer:
                        if buffer.count(z) > 1:  # if count of any value > 1
                            valid = False
                            break
                        valid = True

                    if valid:
                        return index

                else:
                    buffer.append(c)


answer = find_marker()
print(answer + 1)
