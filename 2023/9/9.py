import numpy as np

from utils import get_input

DAY = "9"
YEAR = "2023"


def parse(puzzle_input: str):
    """Parse input"""
    return [
        np.array(list(map(int, line.split(" "))))
        for line in puzzle_input.strip().splitlines()
    ]


def part1(data):
    """Solve part 1"""
    ans = 0
    for line in data:
        # for making the while loop pass on the first run
        seq = [1]
        iter_line = line
        line_seq = line[-1]

        while not all([i == 0 for i in seq]):
            seq = np.diff(iter_line)

            if len(seq) == 0:
                break

            line_seq += seq[-1]
            iter_line = seq

        ans += line_seq

    return ans


def part2(data):
    """Solve part 2"""
    ans = 0
    for line in data:
        # for making the while loop pass on the first run
        seq = [1]
        line = line[::-1]
        iter_line = line
        line_seq = line[-1]

        while not all([i == 0 for i in seq]):
            seq = np.diff(iter_line)

            if len(seq) == 0:
                break

            line_seq += seq[-1]
            iter_line = seq

        ans += line_seq

    return ans


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 114
    assert test_solutions[1] == 2

    solutions = solve(puzzle_input)
    assert solutions[0] == 1641934234
    assert solutions[1] == 975

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
