def move(inst, m, c):
    if c == '1':
        for moves in range(inst[0]):         
m[inst[2]].append(m[inst[1]].pop(-1))
    else:
        i = inst[0]
        m[inst[1]], load = m[inst[1]][:-i], m[inst[1]][-i:]
        m[inst[2]].extend(load)
    return m
 
with open("/storage/emulated/0/Download/input_5.txt", "r+") as input_file:
    indices = list(range(1,34,4))
    blocks = [x.split("\n") for x in "".join(input_file).split("\n\n")]
    matrixt = [[x for x in line if x != ' '] for line in [list(reversed(col)) for col in zip(*[[x for y, x in enumerate(line) if y in indices] for line  in blocks[0][:-1]])]]
    instructions = [[int(s.split()[1]), int(s.split()[3]) - 1, int(s.split()[5]) - 1] for s in blocks[1][:-1]]
    matrixt_two = [x.copy() for x in matrixt]
    for instruction in instructions:
        matrixt = move(instruction, matrixt, "1")
        matrixt_two = move(instruction, matrixt_two, "2")
    print("".join([x[-1] for x in matrixt]), "".join([x[-1] for x in matrixt_two]), sep = '\n')
