from collections import defaultdict
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [[segment.split(' ') for segment in line.split(' | ')]
            for line in puzzle_input.split('\n')]


def part1(data):
    """Solve part 1"""
    counter = 0
    for _, output_values in data:
        for output_value in output_values:
            if len(output_value) in [2, 3, 4, 7]:
                counter += 1
    return f'Counter: {counter}'


def part2(data):
    """Solve part 2"""
    output_int_values = []
    for signal_patterns, output_values in data:
        signal_patterns = [set(pattern) for pattern in signal_patterns]
        output_values = [set(output_value) for output_value in output_values]
        len_to_val = {2: 1, 3: 7, 4: 4, 7: 8}
        val_lookup = defaultdict(lambda: set(''))
        for pattern in signal_patterns:
            if len(pattern) in len_to_val:
                val_lookup[len_to_val[len(pattern)]] = pattern

        for pattern in [pattern for pattern in signal_patterns if len(pattern) is 5]:
            if len(pattern - val_lookup[4]) == 3:
                val_lookup[2] = pattern
            elif len(pattern - val_lookup[7]) == 2:
                val_lookup[3] = pattern
            elif len(pattern - val_lookup[7]) == 3:
                val_lookup[5] = pattern

        for pattern in [pattern for pattern in signal_patterns if len(pattern) is 6]:
            if len(pattern - val_lookup[4]) == 2:
                val_lookup[9] = pattern
            elif len(pattern - val_lookup[7]) == 3:
                val_lookup[0] = pattern
            elif len(pattern - val_lookup[7]) == 4:
                val_lookup[6] = pattern

        output_string = ''
        for output_value in output_values:
            for val, string in val_lookup.items():
                if output_value == string:
                    output_string += f'{val}'
                    break

        output_int_values.append(int(output_string))
    return f'Output Sum Values: {sum(output_int_values)}'


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
