import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [[int(cal) for cal in line.split('\n')] for line in puzzle_input.split('\n\n')]


def part1(data):
    """Solve part 1"""
    for i in range(len(data)):
        data[i] = sum(data[i])
    data.sort()
    return f'Most Calories: {data[-1]}'


def part2(data):
    """Solve part 2"""
    return f'Most Calories: {sum(data[-3:])}'


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    path = "./2022/1/input.txt"
    print(f"Input Data: {path}")
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print('\nSolutions:')
    print(f'\tPart 1: {solutions[0]}\n\tPart 2: {solutions[1]}')
