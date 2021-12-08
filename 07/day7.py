
def load_example():
    line = '16,1,2,0,4,2,7,1,2,14'
    return list(map(int, line.split(',')))


def load_input():
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            return list(map(int, line.split(',')))


def cost_part1(pos, crabs):
    return sum(abs(pos - c) for c in crabs)


def hill_climber(crabs, cost_func):
    pos = sum(crabs) // len(crabs)
    while True:
        # print(pos)
        # TODO: could be improved by taking larger steps?
        p1 = pos + 1
        p2 = pos - 1
        c0 = cost_func(pos, crabs)
        c1 = cost_func(p1, crabs)
        c2 = cost_func(p2, crabs)
        if c2 < c0:
            pos = p2
        elif c1 < c0:
            pos = p1
        else:
            break

    return cost_func(pos, crabs)


def part1(crabs):
    return hill_climber(crabs, cost_part1)


assert part1(load_example()) == 37
print('part 1', part1(load_input()))


def cost_part2(pos, crabs):
    return sum(fuel_func(pos, c) for c in crabs)


def fuel_func(p1, p2):
    distance = abs(p2 - p1)
    n = distance
    return n * (n + 1) // 2


assert fuel_func(16, 5) == 66
assert fuel_func(1, 5) == 10
assert fuel_func(2, 5) == 6
assert fuel_func(0, 5) == 15
assert fuel_func(4, 5) == 1
assert fuel_func(7, 5) == 3
assert fuel_func(14, 5) == 45


def part2(crabs):
    return hill_climber(crabs, cost_part2)


assert part2(load_example()) == 168
print('part 2', part2(load_input()))
