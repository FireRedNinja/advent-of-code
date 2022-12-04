from utils import get_input

DAY = "0"
YEAR = "2022"
TEST_DATA = ""


def parse(puzzle_input: str):
    """Parse input"""
    return [line for line in puzzle_input.strip().splitlines()]


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

    test_solutions = solve(TEST_DATA)
    # assert test_solutions[0] ==
    # assert test_solutions[1] ==

    solutions = solve(puzzle_input)
    # assert solutions[0] ==
    # assert solutions[1] ==

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
