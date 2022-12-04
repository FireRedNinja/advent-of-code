from utils import get_input

# TODO
# - add testing

DAY = "0"
YEAR = "2022"
P1_TEST_DATA = ""
P2_TEST_DATA = ""


def parse(puzzle_input: str):
    """Parse input"""
    return [line for line in puzzle_input.splitlines()]


def part1(data):
    """Solve part 1"""

    return f"Not implemented"


def part2(data):
    """Solve part 2"""

    return f"Not implemented"


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = get_input(DAY, YEAR)

    solutions = solve(puzzle_input)
    print("\nSolutions:")
    print(f"\tPart 1: {solutions[0]}\n\tPart 2: {solutions[1]}")
