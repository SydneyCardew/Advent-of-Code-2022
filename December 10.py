targets = [x for x in range(221) if (x + 20) % 40 == 0]


def check(cycles, answers, register):
    if cycles in targets:
        answers.append(cycles * register)
    return answers


def draw(register, cycle, screen):
    sprite_pos = [register - 1, register, register + 1]
    row = cycle // 40
    column = cycle % 40 - 1
    if column in sprite_pos:
        screen[row][column] = '#'
    return screen


def cycler(cycle, register, answers, screen):
    cycle += 1
    screen = draw(register, cycle, screen)
    answers = check(cycle, answers, register)
    return cycle, register, answers, screen


def parser(instruction, cycle, register, answers, screen):
    if instruction == 'noop':
        cycle, register, answers, screen = cycler(cycle, register, answers, screen)
    else:
        cycle, register, answers, screen = cycler(cycle, register, answers, screen)
        register += int(instruction.split()[1])
        cycle, register, answers, screen = cycler(cycle, register, answers, screen)
    return cycle, register, answers, screen


with open("input_10.txt", "r+")as input_file:
    cycle = 1
    register = 1
    answers = []
    screen = [['.' for x in range(40)] for y in range(6)]
    for line in input_file:
        cycle, register, answers, screen = parser(line.strip("\n"), cycle, register, answers, screen)
    print(sum(answers))
    for line in screen:
        print("".join(line))



