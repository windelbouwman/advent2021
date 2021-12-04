EXAMPLE = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


def get_blobs(lines):
    blob = []
    for line in lines:
        line = line.strip()
        if line:
            blob.append(line)
        else:
            yield blob
            blob = []
    if blob:
        yield blob


class Board:
    def __init__(self, rows):
        rows = [list(map(int, r.split())) for r in rows]
        self.rows = rows
        self.n_columns = len(rows[0])
        self.n_rows = len(rows)
        # print(self.rows)
        self.unmarked = set()
        self.marked = set()
        for row in rows:
            for num in row:
                self.unmarked.add(num)

    def mark(self, number):
        if number in self.unmarked:
            self.unmarked.remove(number)
            self.marked.add(number)

    def wins(self):
        for row in range(self.n_rows):
            if all(self.rows[row][col] in self.marked for col in range(self.n_columns)):
                return True
        for col in range(self.n_columns):
            if all(self.rows[row][col] in self.marked for row in range(self.n_rows)):
                return True


def parse_lines(lines):
    blobs = get_blobs(lines)
    # print(list(blobs))
    numbers = next(blobs)[0]
    numbers = list(map(int, numbers.split(',')))
    boards = list(map(Board, blobs))
    return numbers, boards


def load_example():
    return parse_lines(EXAMPLE.split('\n'))


def load_input():
    with open('input.txt', 'r') as f:
        return parse_lines(f)


def part1(numbers, boards):
    for number in numbers:
        # print(number)
        for board in boards:
            board.mark(number)
            if board.wins():
                s = sum(board.unmarked)
                return number * s


assert part1(*load_example()) == 4512
print('part 1', part1(*load_input()))


def part2(numbers, boards):
    boards_done = []
    for number in numbers:
        # print(number)
        for board in boards:
            board.mark(number)
            if board.wins():
                boards_done.append(board)
                if len(boards_done) == len(boards):
                    s = sum(board.unmarked)
                    return number * s
        while boards_done:
            boards.remove(boards_done.pop())


assert part2(*load_example()) == 1924
print('part 2', part2(*load_input()))
