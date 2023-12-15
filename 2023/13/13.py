from utils import get_input
import numpy as np

DAY = "13"
YEAR = "2023"


def parse(puzzle_input: str):
    """Parse input"""
    return [
        np.array([list(line) for line in pattern.splitlines()])
        for pattern in puzzle_input.strip().split("\n\n")
    ]


def part1(data):
    """Solve part 1"""

    ans = 0
    for pattern in data:
        reflect_found = False
        # horiz scan
        for i in range(len(pattern[0]) - 1):
            if np.array_equal(pattern[:, i], pattern[:, i + 1]):
                length_to_end = min(i + 1, len(pattern[0]) - (i + 1))
                if np.array_equal(
                    pattern[:, i - length_to_end + 1 : i + 1],
                    np.fliplr(pattern[:, i + 1 : i + 1 + length_to_end]),
                ):
                    ans += i + 1
                    reflect_found = True
                    break

        if reflect_found:
            continue

        # vert scan
        for i in range(len(pattern) - 1):
            if np.array_equal(pattern[i, :], pattern[i + 1, :]):
                length_to_end = min(i + 1, len(pattern) - (i + 1))
                if np.array_equal(
                    pattern[i - length_to_end + 1 : i + 1, :],
                    np.flipud(pattern[i + 1 : i + 1 + length_to_end, :]),
                ):
                    ans += 100 * (i + 1)
                    break
    return ans


def diffed(a, b):
    diff = a == b
    values, counts = np.unique(diff, return_counts=True)
    if False in values:
        return counts[np.where(values == False)[0]][0] == 1
    return False


def part2(data):
    """Solve part 2"""

    ans = 0
    for pattern in data:
        reflect_found = False
        # horiz scan
        for i in range(len(pattern[0]) - 1):
            length_to_end = min(i + 1, len(pattern[0]) - (i + 1))
            diff = diffed(
                pattern[:, i - length_to_end + 1 : i + 1],
                np.fliplr(pattern[:, i + 1 : i + 1 + length_to_end]),
            )
            if diff:
                ans += i + 1
                reflect_found = True
                break

        if reflect_found:
            continue

        # vert scan
        for i in range(len(pattern) - 1):
            length_to_end = min(i + 1, len(pattern) - (i + 1))
            diff = diffed(
                pattern[i - length_to_end + 1 : i + 1, :],
                np.flipud(pattern[i + 1 : i + 1 + length_to_end, :]),
            )
            if diff:
                ans += 100 * (i + 1)
                break
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
    assert test_solutions[0] == 405
    assert test_solutions[1] == 400

    solutions = solve(puzzle_input)
    assert solutions[0] == 30575
    assert solutions[1] == 37478

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
