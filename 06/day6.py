
def load_example():
    return list(map(int, """3,4,3,1,2""".split(',')))


def load_input():
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            return list(map(int, line.split(',')))


# OBSOLETED
# def part1(state, max_days):
#     """ Straight forward simulation """
#     day = 0
#     while day < max_days:
#         # print('day', day, ','.join(map(str, state)))
#         new_fishes = []
#         for i in range(len(state)):
#             if state[i] > 0:
#                 state[i] -= 1
#             else:
#                 state[i] = 6
#                 new_fishes += [8]
#         state += new_fishes
#         day += 1
#     return len(state)


def part2(fishes, max_days):
    """ Group per generation.

    This is a sort of IIR filter.
    """
    state = [
        fishes.count(age)
        for age in range(9)
    ]
    for day in range(max_days):
        state = [
            state[1],  # 0
            state[2],  # 1
            state[3],  # 2
            state[4],  # 3
            state[5],  # 4
            state[6],  # 5
            state[7] + state[0],  # 6
            state[8],  # 7
            state[0],  # 8
        ]
    return sum(state)


assert part2(load_example(), 18) == 26
assert part2(load_example(), 80) == 5934
print('part 1', part2(load_input(), 80))


assert part2(load_example(), 256) == 26984457539
print('part 2', part2(load_input(), 256))
