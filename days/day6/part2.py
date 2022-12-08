marker = []


def find_marker():
    with open("input", "r") as file:
        for i in file.readlines():
            for index, c in enumerate(i):
                if len(marker) == 14:
                    # add new value to marker and swipe other values to the left
                    for x in range(13):
                        marker[x] = marker[x + 1]
                    marker[13] = c

                    for z in marker:
                        if marker.count(z) > 1:  # if count of any value > 1
                            valid = False
                            break
                        valid = True

                    if valid:
                        return index

                else:
                    marker.append(c)


answer = find_marker()
print(answer + 1)
