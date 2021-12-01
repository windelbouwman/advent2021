
def load_example():
    inp = """
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263
    """
    depths = []
    for line in inp.split('\n'):
        line = line.strip()
        if line:
            # print('a', line)
            depths.append(int(line))
    return depths


def part1(depths):
    deltas = [
        b - a
        for a, b in zip(depths[:-1], depths[1:])
    ]
    # print(deltas)
    increments = [a for a in deltas if a > 0]
    # print(increments)
    # print(len(increments))
    return len(increments)


def load_input():
    depths = []
    with open('input_part1.txt', 'r') as f:
        for line in f:
            depths.append(int(line.strip()))
    return depths


def example_part1():
    depths = load_example()
    assert part1(depths) == 7


def real_part1():
    depths = load_input()
    print('part 1: ', part1(depths))


example_part1()
real_part1()


def part2(depths):
    sums = [
        a + b + c
        for a, b, c in zip(depths[:-2], depths[1:-1], depths[2:])
    ]
    return part1(sums)


def example_part2():
    depths = load_example()
    assert part2(depths) == 5


def real_part2():
    depths = load_input()
    print('part 2: ', part2(depths))


example_part2()
real_part2()
