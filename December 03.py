def priority(item):
    return (ord(item) - 96) if item.islower() else (ord(item) - 38)

with open("/storage/emulated/0/Download/input_3.txt", "r+") as input_file:
    score_one = 0
    score_two = 0
    group = []
    for index, line in enumerate(input_file):
        sline = line.strip("\n")
        h = len(sline)//2
        group.append(sline)
        split_line = [sline[:h], sline[h:]]
        common = list(set(split_line[0]) & set(split_line[1]))[0]
        score_one += priority(common)
        if (index + 1) % 3 == 0:
            badge = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
            score_two += priority(badge)
            group.clear()
    print(score_one, score_two, sep="\n")
		
