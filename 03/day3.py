
EXAMPLE = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def load_example():
    nums = []
    for line in EXAMPLE.split('\n'):
        nums.append(line.strip())
    return nums


def load_puzzle_input():
    lines = []
    with open('input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def get_ones_and_zeros(codes):
    W = len(codes[0])
    print('W=', W)
    ones = [0] * W
    zeros = [0] * W
    for code in codes:
        for bit in range(W):
            val = code[bit]
            if val == '1':
                ones[bit] += 1
            else:
                assert val == '0'
                zeros[bit] += 1

    print('ones', ones, 'zeros', zeros)
    return ones, zeros


def part1(codes):
    ones, zeros = get_ones_and_zeros(codes)
    gamma = ''
    epsilon = ''
    W = len(codes[0])
    for bit in range(W):
        if ones[bit] > zeros[bit]:
            gamma += '1'
            epsilon += '0'
        else:
            # elif zeros[bit] > ones[bit]:
            gamma += '0'
            epsilon += '1'
            # else:
            # print('same!')
            # 217 , 3878
    print('gamma=', gamma, 'epsilon=', epsilon)
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print('gamma=', gamma, 'epsilon=', epsilon)

    return gamma * epsilon


assert part1(load_example()) == 198
print('part 1', part1(load_puzzle_input()))


def filter_codes(codes, criteria):
    pos = 0
    while len(codes) > 1:
        ones, zeros = get_ones_and_zeros(codes)
        bit = criteria(ones, zeros, pos)
        codes = [c for c in codes if c[pos] == bit]
        pos += 1
    return codes[0]


def part2(codes):
    def oxygen_criteria(ones, zeros, pos):
        return '1' if ones[pos] >= zeros[pos] else '0'

    def co2_criteria(ones, zeros, pos):
        return '0' if zeros[pos] <= ones[pos] else '1'

    oxygen = filter_codes(codes, oxygen_criteria)
    co2 = filter_codes(codes, co2_criteria)
    print("oxygen", oxygen, "co2", co2)
    oxygen = int(oxygen, 2)
    co2 = int(co2, 2)
    print("oxygen", oxygen, "co2", co2)
    return oxygen * co2


assert part2(load_example()) == 230
print('part 2', part2(load_puzzle_input()))
