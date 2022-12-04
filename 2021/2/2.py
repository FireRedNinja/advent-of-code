import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    horizontal = 0
    depth = 0
    for line in data:
        [direction, distance] = line.split()
        distance = int(distance)
        if direction == "forward":
            horizontal += distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance

    return f"horizontal * depth = {horizontal} * {depth} : {horizontal * depth}"


def part2(data):
    """Solve part 2"""
    horizontal = 0
    depth = 0
    aim = 0
    for line in data:
        [direction, distance] = line.split()
        distance = int(distance)
        if direction == "forward":
            horizontal += distance
            depth += aim * distance
        elif direction == "down":
            aim += distance
            # depth += distance
        elif direction == "up":
            aim -= distance

    return f"horizontal * depth = {horizontal} * {depth} : {horizontal * depth}"


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
        print("\nSolutions:")
        print(f"\tPart 1: {solutions[0]}\n\tPart 2: {solutions[1]}")
