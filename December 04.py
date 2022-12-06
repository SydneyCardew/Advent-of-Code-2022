with open("/storage/emulated/0/Download/input_4.txt", "r+") as input_file:
	score_one = 0
	score_two = 0
	for line in input_file:
		pline = [x.split("-") for x in line.strip("\n").split(",")]
		pline = [list(range(int(x[0]), int(x[1]) + 1)) for x in pline]
		if all(i in pline[0] for in pline[1]) or all(i in pline[1] for i in pline[0]):
			score_one += 1
		if any(i in pline[0] for in pline[1]) or any(i in pline[1] for i in pline[0]):
			score_two += 1
		print(score_one, score_two, sep='\n')
