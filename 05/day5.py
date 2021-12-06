import re
EXAMPLE = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def load_lines(text_lines):
    prog = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
    lines = []
    for line in text_lines:
        line = line.strip()
        if not line:
            continue
        mo = prog.match(line)
        # print(mo)
        assert mo
        x1 = int(mo.group(1))
        y1 = int(mo.group(2))
        x2 = int(mo.group(3))
        y2 = int(mo.group(4))
        lines.append((x1, y1, x2, y2))
    return lines


def load_example():
    return load_lines(EXAMPLE.split('\n'))


def load_input():
    with open('input.txt', 'r') as f:
        return load_lines(f)


def mark(grid, x, y):
    # print('marking', x, y)
    point = (x, y)
    if point in grid:
        grid[point] += 1
    else:
        grid[point] = 1


def draw_grid(grid, width, height):
    for y in range(height):
        row = ''.join(str(grid.get((x, y), '.')) for x in range(width))
        print(row)


def part1(lines):
    grid = {}

    for x1, y1, x2, y2 in lines:
        # print('line', x1, y1, x2, y2)
        if x1 == x2:
            if y2 < y1:
                y1, y2 = y2, y1
            for y in range(y1, y2+1):
                mark(grid, x1, y)
        elif y1 == y2:
            if x2 < x1:
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                mark(grid, x, y1)
        else:
            pass
            # Skip diagonal lines for now.
            # raise NotImplementedError('line not vertical or horizontal')

    # print(grid)
    values = [v for v in grid.values() if v > 1]
    # print(values)
    return len(values)


assert part1(load_example()) == 5
print('part 1', part1(load_input()))


def part2(lines):
    grid = {}

    for x1, y1, x2, y2 in lines:
        # print('line', x1, y1, x2, y2)
        if x1 == x2:
            if y2 < y1:
                y1, y2 = y2, y1
            for y in range(y1, y2+1):
                mark(grid, x1, y)
        elif y1 == y2:
            if x2 < x1:
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                mark(grid, x, y1)
        else:
            dx = x2 - x1
            dy = y2 - y1
            N = abs(dx)
            assert abs(dx) == abs(dy)
            assert N > 0
            dx = dx // N
            dy = dy // N
            for n in range(N + 1):
                mark(grid, x1 + n * dx, y1 + n * dy)

            # Skip diagonal lines for now.
            # raise NotImplementedError('line not vertical or horizontal')

    # draw_grid(grid, 12, 12)
    # print(grid)
    values = [v for v in grid.values() if v > 1]
    # print(values)
    return len(values)


assert part2(load_example()) == 12
print('part 2', part2(load_input()))
