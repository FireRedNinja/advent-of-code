import pathlib
import sys
from collections import Counter


def parse(puzzle_input):
    """Parse input"""
    data = [line for line in puzzle_input.split('\n')]
    data = [line.split(' -> ') for line in data]
    for i, line in enumerate(data):
        for j, coords in enumerate(line):
            x, y = coords.split(',')
            data[i][j] = (int(x), int(y))
    return data


def part1(data):
    """Solve part 1"""
    data = list(filter(lambda coords: coords[0][0] == coords[1][0] or coords[0][1] == coords[1][1], data))

    intersects = []
    for start, end in data:
        y_values = list(range(min(start[1], end[1]), max(start[1], end[1]) + 1))
        x_values = list(range(min(start[0], end[0]), max(start[0], end[0]) + 1))
        for x in x_values:
            for y in y_values:
                intersects.append((x, y))

    counter = len([count for (coords, count) in Counter(intersects).items() if count >= 2])
    return f'No. of Overlaps: {counter}'


def part2(data):
    """Solve part 2"""

    intersects = []
    for start, end in data:
        min_y = min(start[1], end[1])
        max_y = max(start[1], end[1])
        decreasing = False
        increasing = False

        if start[0] > end[0]:
            y = end[1]
            if y is max_y and y is not min_y:
                decreasing = True
            elif y is min_y and y is not max_y:
                increasing = True
        elif start[0] < end[0]:
            y = start[1]
            if y is max_y and y is not min_y:
                decreasing = True
            elif y is min_y and y is not max_y:
                increasing = True


        y_values = list(range(min(start[1], end[1]), max(start[1], end[1]) + 1))
        x_values = list(range(min(start[0], end[0]), max(start[0], end[0]) + 1))
        for x in x_values:
            if decreasing:
                intersects.append((x, y_values[-1]))
                y_values.pop()
            elif increasing:
                intersects.append((x, y_values[0]))
                y_values.pop(0)
            else:
                for y in y_values:
                    intersects.append((x, y))


    counter = len([count for (coords, count) in Counter(intersects).items() if count >= 2])
    return f'No. of Overlaps: {counter}'


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
