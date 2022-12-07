lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = lowercase.upper()

current_contents = ["", ""]
priority_value = 0
with open("items", "r") as file:
    for i in file.readlines():
        length = len(i.strip())

        current_contents[0] = i.strip()[0:int(length / 2)]
        current_contents[1] = i.strip()[int(length / 2):length]

        for char in current_contents[1]:
            if char in current_contents[0]:
                alphabet_location = lowercase.index(char.lower())+1
                if char.islower():
                    priority_value += alphabet_location
                else:
                    priority_value += alphabet_location+26
                break

print(priority_value)


