#  trying to golf it a bit. Still can't get down to one line :(

list = sorted([sum([int(y) for y in x.split("\n")]) for x in "".join(list(open("/storage/emulated/0/Download/input.txt", "r+"))).rstrip().split("\n\n")], reverse=True)
print(f"Top:{list[0]}\nTop 3:{sum(list[:3])}")
