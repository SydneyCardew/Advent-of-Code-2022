score_dict = {
    'A X':(4,3),
    'A Y': (8,4),
    'A Z': (3,8),
    'B X': (1,1),
    'B Y': (5,5),
    'B Z': (9,9),
    'C X': (7,2),
    'C Y': (2,6),
    'C Z': (6,7)
    }
score_1 = 0
score_2 = 0
with open("/storage/emulated/0/Download/input_2.txt", "r+") as input_file:
    for line in input_file:
        score_1 += score_dict[line.strip("\n")][0]
        score_2 += score_dict[line.strip("\n")][1]
print(score_1, score_2)
