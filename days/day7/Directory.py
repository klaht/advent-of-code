class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.children = []
        self.file_size = 0

    def add_file(self, file):
        self.files.append(file)
        self.file_size += int(file[0])

    def __str__(self):
        return self.name
