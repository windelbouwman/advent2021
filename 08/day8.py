SHORT_EXAMPLE = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

EXAMPLE = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


def parse_entry(line):
    patterns, output_digits = line.split(' | ')
    patterns = patterns.split(' ')
    output_digits = output_digits.split(' ')
    return (patterns, output_digits)


def load_entries(lines):
    return [
        parse_entry(line.strip())
        for line in lines
    ]


def load_example():
    return load_entries(EXAMPLE.split('\n'))


def load_input():
    with open('input.txt', 'r') as f:
        return load_entries(f)


def part1(entries):
    N = 0
    for patterns, outputs in entries:
        # print(outputs)
        for output in outputs:
            # Check for numbers:
            # 1 (2 segments),
            # 4 (4 segments),
            # 7 (3 segments)
            # and 8 (7 segments)
            if len(output) in [2, 4, 3, 7]:
                N += 1
    return N


assert part1(load_example()) == 26
print('part 1', part1(load_input()))


def solve_entry(entry):
    patterns, outputs = entry

    # First, determine segment to digit map
    mapping = {}
    while patterns:
        pattern = patterns.pop(0)
        pattern = frozenset(pattern)
        # print(pattern)
        if pattern in mapping.values():
            print('known pattern')
            continue

        if len(pattern) == 2:
            mapping[1] = pattern
        elif len(pattern) == 3:
            mapping[7] = pattern
        elif len(pattern) == 4:
            mapping[4] = pattern
        elif len(pattern) == 7:
            mapping[8] = pattern
        elif len(pattern) == 6:  # 0, 6 or 9
            if (1 in mapping) and (4 in mapping):
                if mapping[4].issubset(pattern):  # 9
                    mapping[9] = pattern
                elif mapping[1].issubset(pattern):  # 0
                    mapping[0] = pattern
                else:  # 6
                    mapping[6] = pattern
            else:
                patterns.append(pattern)
        elif len(pattern) == 5:  # 2, 3 or 5
            if (1 in mapping) and (6 in mapping):
                if mapping[1].issubset(pattern):  # 3
                    mapping[3] = pattern
                elif pattern.issubset(mapping[6]):  # 5
                    mapping[5] = pattern
                else:  # 2
                    mapping[2] = pattern
            else:
                patterns.append(pattern)
        else:
            raise ValueError('Arg')
    # print(mapping)

    # Stage 2, determine output:
    new_map = {d: str(v) for v, d in mapping.items()}
    # print(new_map)
    text = ''
    for output in outputs:
        output = frozenset(output)
        text += new_map[output]

    value = int(text)
    return value


def part2(entries):
    return sum(solve_entry(e) for e in entries)


assert solve_entry(parse_entry(SHORT_EXAMPLE)) == 5353
assert part2(load_example()) == 61229
print('part 2', part2(load_input()))
