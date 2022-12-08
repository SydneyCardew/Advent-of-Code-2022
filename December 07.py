import re
from itertools import chain


class Directory:

    def __init__(self, identity, parent=None):
        self.identity = identity
        self.contents = []
        self.parent = parent
        self.size = 0
        if self.identity == "/":
            Directory.root = self

    def add(self, identity, type, parent, size=None):
        if type == 'file':
            self.contents.append(File(identity, size))
        else:
            self.contents.append(Directory(identity, self))
        size = self.get_size()

    def get_size(self):
        size = 0
        for item in self.contents:
            if isinstance(item, File):
                size += int(item.size)
            else:
                size += int(item.get_size())
        return size

    def iterable_of_sizes(self):
        children = filter(lambda thing: isinstance(thing, Directory),
                          self.contents)
        return chain([self.get_size()],
                     *[child.iterable_of_sizes() for child in children])

    def cd(self, command):
        if command == '..':
            return self.parent
        elif command == '/':
            return Directory(command)
        else:
            for i in self.contents:
                if i.identity == command:
                    return i


class File:

    def __init__(self, identity, size):
        self.identity = identity
        self.size = size

    def iterable_of_sizes(self):
        return chain([self.size])


with open("input_7.txt", "r+")as input_file:
    blocks = [x.rstrip().split("\n") for x in re.split(r"(?=\$)", input_file.read())]
    location = None
    for block in blocks:
        if block[0] == "$ ls":
            for entry in block[1:]:
                    if entry.split()[0].isnumeric():
                        location.add(entry.split()[-1], 'file', location, entry.split()[0])
                    else:
                        location.add(entry.split()[-1], 'directory', location)
        elif "$ cd" in block[0]:
            directory = block[0].split()[-1]
            if not location:
                location = Directory(directory)
            else:
                location = location.cd(directory)
    disk_space = 70000000 - list(Directory.root.iterable_of_sizes())[0]
    day_one = sum([x for x in list(Directory.root.iterable_of_sizes()) if x < 100000])
    day_two = min([x for x in list(Directory.root.iterable_of_sizes()) if (disk_space + x) > 30000000])
    print(day_one, day_two, sep="\n")





