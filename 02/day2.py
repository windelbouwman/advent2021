
EXAMPLE = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def load_example():
    commands = [cmd.split(' ') for cmd in EXAMPLE.split('\n')]
    commands = [(cmd, int(op)) for cmd, op in commands]
    return commands


def load_input():
    commands = []
    with open('puzzle_input.txt', 'r') as f:
        for line in f:
            cmd, op = line.split(' ')
            op = int(op)
            commands.append((cmd, op))
    return commands


def part1(commands):
    depth = 0
    position = 0
    for cmd, operand in commands:
        if cmd == 'forward':
            position += operand
        elif cmd == 'down':
            depth += operand
        elif cmd == 'up':
            depth -= operand
        else:
            raise NotImplementedError(cmd)
    return depth * position


assert part1(load_example()) == 150
print('part 1', part1(load_input()))


def part2(commands):
    aim = 0
    depth = 0
    position = 0
    for cmd, operand in commands:
        if cmd == 'forward':
            position += operand
            depth += aim * operand
        elif cmd == 'down':
            aim += operand
        elif cmd == 'up':
            aim -= operand
        else:
            raise NotImplementedError(cmd)
    return depth * position


assert part2(load_example()) == 900
print('part 2', part2(load_input()))
