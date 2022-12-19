from collections import deque

import numpy as np

from utils import get_input

DAY = "8"
YEAR = "2022"


def parse(puzzle_input: str):
    """Parse input"""
    return [
        [int(tree) for tree in list(line)] for line in puzzle_input.strip().splitlines()
    ]


def part1(data):
    """Solve part 1"""
    rows, cols = len(data), len(data[0])
    scores = np.zeros_like(data)

    scores[0, :] = 1
    scores[-1, :] = 1
    scores[:, 0] = 1
    scores[:, -1] = 1

    visible = set()
    visible.update([(0, c) for c in range(cols)])
    visible.update([(rows - 1, c) for c in range(cols)])
    visible.update([(r, 0) for r in range(rows)])
    visible.update([(r, cols - 1) for r in range(rows)])

    for r in range(1, rows - 1):
        max = data[r][0]
        for c in range(1, cols - 1):
            if data[r][c] > max:
                max = data[r][c]
                scores[r][c] = scores[r][c] + max
                visible.add((r, c))
        max = data[r][cols - 1]
        for c in range(cols - 2, 0, -1):
            if data[r][c] > max:
                max = data[r][c]
                visible.add((r, c))

    for c in range(1, cols - 1):
        max = data[0][c]
        for r in range(1, rows - 1):
            if data[r][c] > max:
                max = data[r][c]
                visible.add((r, c))
        max = data[rows - 1][c]
        for r in range(rows - 2, 0, -1):
            if data[r][c] > max:
                max = data[r][c]
                visible.add((r, c))

    return len(visible)


def part2(data):
    """Solve part 2"""
    data = np.array(data)
    rows, cols = len(data), len(data[0])

    max_score = 0
    for r in range(rows):
        for c in range(cols):
            tree = data[r][c]
            left = data[r, :c][::-1]
            right = data[r, c + 1 :]
            up = data[:r, c][::-1]
            down = data[r + 1 :, c]

            curr_score = 1
            for direction in [left, right, up, down]:
                visible = 0
                for i in direction:
                    if i < tree:
                        visible += 1
                    elif i >= tree:
                        visible += 1
                        break
                    else:
                        break

                curr_score *= visible
            max_score = max(max_score, curr_score)

    return max_score


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 21
    # assert test_solutions[1] == 8

    solutions = solve(puzzle_input)
    assert solutions[0] == 1792
    # assert solutions[1] ==

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
