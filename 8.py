from collections import defaultdict
import pathlib
import sys
from pdb import set_trace


def parse(puzzle_input):
    """Parse input"""
    return [[segment.split(' ') for segment in line.split(' | ')]
            for line in puzzle_input.split('\n')]


def part1(data):
    """Solve part 1"""
    counter = 0
    for i in data:
        for j in i[1]:
            if len(j) in [2, 3, 4, 7]:
                counter += 1
    return f'Counter: {counter}'


def part2(data):
    """Solve part 2"""
    output_values = []
    for i in data:
        len_to_val = {2: 1, 3: 7, 4: 4, 7: 8}
        str_to_val = {}
        val_lookup = defaultdict(lambda: '')
        len_lookup = defaultdict(list)
        for j in i[0]:
            if len(j) in len_to_val:
                val_lookup[len_to_val[len(j)]] = j
                str_to_val[j] = len_to_val[len(j)]
            len_lookup[len(j)].append(j)

        for j in len_lookup[5]:
            if len(set(j) - set(val_lookup[4])) == 3:
                val_lookup[2] = j
                str_to_val[j] = 2
            elif len(set(j) - set(val_lookup[7])) == 2:
                val_lookup[3] = j
                str_to_val[j] = 3
            elif len(set(j) - set(val_lookup[7])) == 3:
                val_lookup[5] = j
                str_to_val[j] = 5

        for j in len_lookup[6]:
            if len(set(j) - set(val_lookup[4])) == 2:
                val_lookup[9] = j
                str_to_val[j] = 9
            elif len(set(j) - set(val_lookup[7])) == 3:
                val_lookup[0] = j
                str_to_val[j] = 0
            elif len(set(j) - set(val_lookup[7])) == 4:
                val_lookup[6] = j
                str_to_val[j] = 6

        output = ''
        for j in i[1]:
            for k in str_to_val:
                if set(j) == set(k):
                    output += f'{str_to_val[k]}'

        output_values.append(int(output))
    return f'Output Sum Values: {sum(output_values)}'


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"Input Data: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print('\nSolutions:')
        print(f'\tPart 1: {solutions[0]}\n\tPart 2: {solutions[1]}')
