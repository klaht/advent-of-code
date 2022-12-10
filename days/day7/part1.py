from Directory import *

dirs = [Directory("/", None)]  # set root as default first element of array of directories

current_dir = dirs[0]  # set current directory to root (dir /)
match = False

with open("input", "r") as file:
    for i in file.readlines():
        current = i.strip().split()

        if current[0] != "$":  # current line is a listed file or directory
            if current[0].isnumeric():  # current listed item is a file
                if current_dir.files.count(current) < 1:  # append file to files if first time
                    # listing files
                    current_dir.add_file(current)
                    temp_dir = current_dir
                    while True:
                        if temp_dir.parent is None:
                            break
                        temp_dir.parent.file_size += int(current[0])
                        temp_dir = temp_dir.parent

            else:  # current listed item is directory
                name = current[1]
                child_dir = Directory(name, current_dir)

                for child in current_dir.children:
                    if child.name == name:
                        match = True
                        break

                if not match:  # if current dir is listed for first time.
                    current_dir.children.append(child_dir)
                    dirs.append(child_dir)
                    match = False

        elif current[1] == "cd":  # current command is to change directory
            if current[2] == "..":  # change to outer directory of current directory
                if current_dir.parent is not None:
                    current_dir = current_dir.parent
            else:  # change to child directory of current directory
                for directory in dirs:
                    if directory.name == current[2] and directory.parent == current_dir:
                        current_dir = directory
                        break

answer = 0

for i in dirs:
    if i.file_size <= 100000:
        answer += i.file_size

print(answer)
