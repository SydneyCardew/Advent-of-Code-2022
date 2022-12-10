move_table = {
    '[-1, 2]': [1, -1],
    '[0, 2]': [0, -1],
    '[1, 2]': [-1, -1],
    '[-2, 1]': [1, -1],
    '[2, 1]': [-1, -1],
    '[-2, 0]': [1, 0],
    '[2, 0]': [-1, 0],
    '[-2, -1]': [1, 1],
    '[2, -1]': [-1, 1],
    '[-1, -2]': [1, 1],
    '[0, -2]': [0, 1],
    '[1, -2]': [-1, 1],
    '[2, 2]': [-1, -1],
    '[-2, 2]': [1, -1],
    '[-2, -2]': [1, 1],
    '[2, -2]': [-1, 1]
}

head_pos = [0, 0]
tail_pos = [0, 0]
two_pos = [[0, 0] for x in range(10)]
tail_table = [tail_pos]
tail_table_two = [two_pos[-1]]


def move_parser_one(move, head_pos, tail_pos, tail_table):
    direction, extent = move.split()[0], int(move.split()[1])
    for x in range(extent):
        if direction == 'U':
            head_pos[1] += 1
        elif direction == 'D':
            head_pos[1] -= 1
        elif direction == 'R':
            head_pos[0] += 1
        elif direction == 'L':
            head_pos[0] -= 1
        relative_tail = [tail_pos[0] - head_pos[0], tail_pos[1] - head_pos[1]]
        distance = [abs(tail_pos[0] - head_pos[0]), abs(tail_pos[1] - head_pos[1])]
        if distance[0] > 1 or distance[1] > 1:
            adj = move_table[str(relative_tail)]
            tail_pos = [tail_pos[0] + adj[0], tail_pos[1] + adj[1]]
            tail_table.append(tail_pos)
    return head_pos, tail_pos, tail_table


def move_parser_two(move, two_pos, tail_table_two):
    direction, extent = move.split()[0], int(move.split()[1])
    for x in range(extent):
        if direction == 'U':
            two_pos[0][1] += 1
        elif direction == 'D':
            two_pos[0][1] -= 1
        elif direction == 'R':
            two_pos[0][0] += 1
        elif direction == 'L':
            two_pos[0][0] -= 1
        for i, entry in enumerate(two_pos):
            if i > 0:
                relative_tail = [two_pos[i][0] - two_pos[i-1][0],
                                 two_pos[i][1] - two_pos[i-1][1]]
                distance = [abs(two_pos[i][0] - two_pos[i-1][0]),
                            abs(two_pos[i][1] - two_pos[i-1][1])]
                if distance[0] > 1 or distance[1] > 1:
                    adj = move_table[str(relative_tail)]
                    two_pos[i] = [two_pos[i][0] + adj[0],
                                  two_pos[i][1] + adj[1]]
                tail_table_two.append(two_pos[-1])
    return two_pos, tail_table_two


with open("input_9.txt", "r+")as input_file:
    instructions = []
    for line in input_file:
        instructions.append(line.strip("\n"))

for instruction in instructions:
    head_pos, tail_pos, tail_table = move_parser_one(instruction, head_pos, tail_pos, tail_table)
print(len(set([str(x) for x in tail_table])))
for instruction in instructions:
    two_pos, tail_table_two = move_parser_two(instruction, two_pos, tail_table_two)
print(len(set([str(x) for x in tail_table_two])))



