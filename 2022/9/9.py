import numpy as np

from utils import get_input

DAY = "9"
YEAR = "2022"


def parse(puzzle_input: str):
    """Parse input"""
    return [
        [step for step in line.split(" ")] for line in puzzle_input.strip().splitlines()
    ]


def is_same_row(head, tail) -> bool:
    return tail[1] == head[1]


def is_same_col(head, tail) -> bool:
    return tail[0] == head[0]


def is_touching(head, tail):
    directions = [
        [0, 1],
        [0, -1],
        [-1, 0],
        [1, 0],
        [-1, -1],
        [1, -1],
        [-1, 1],
        [1, 1],
        [0, 0],
    ]
    return tail in [list(np.add(head, d)) for d in directions]


def lead_and_follow(direction: str, unit: int, rope, visited: set):
    directions = {
        "U": [0, 1],
        "D": [0, -1],
        "L": [-1, 0],
        "R": [1, 0],
    }

    for i in range(unit):
        head = list(np.add(rope[0], directions[direction]))
        rope[0] = head

        for j in range(1, len(rope)):
            tail = rope[j]

            if not is_touching(head, tail):
                if not is_same_row(head, tail) and not is_same_col(
                    head, tail
                ):  # diagnal
                    if tail[0] - head[0] < 0:
                        tail = list(np.add(tail, [1, 0]))
                    else:
                        tail = list(np.add(tail, [-1, 0]))

                    if tail[1] - head[1] < 0:
                        tail = list(np.add(tail, [0, 1]))
                    else:
                        tail = list(np.add(tail, [0, -1]))

                elif not is_same_row(head, tail) and is_same_col(head, tail):  # L/R
                    if tail[1] - head[1] < 0:
                        tail = list(np.add(tail, [0, 1]))
                    else:
                        tail = list(np.add(tail, [0, -1]))

                else:  # U/D
                    if tail[0] - head[0] < 0:
                        tail = list(np.add(tail, [1, 0]))
                    else:
                        tail = list(np.add(tail, [-1, 0]))

                rope[j] = tail

                if j == len(rope) - 1:
                    visited.add(tuple(tail))
            head = tail

    return rope, visited


def part1(data):
    """Solve part 1"""
    visited = set()
    rope = [[0, 0]] * 2

    visited.add(tuple(rope[-1]))

    for step in data:
        direction, unit = step
        unit = int(unit)

        rope, visited = lead_and_follow(direction, unit, rope, visited)

    return len(visited)


def part2(data):
    """Solve part 2"""
    visited = set()
    rope = [[0, 0]] * 10

    visited.add(tuple(rope[-1]))

    for step in data:
        direction, unit = step
        unit = int(unit)

        rope, visited = lead_and_follow(direction, unit, rope, visited)

    return len(visited)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    # assert test_solutions[0] == 13
    assert test_solutions[1] == 36

    solutions = solve(puzzle_input)
    assert solutions[0] == 6098
    assert solutions[1] == 2597

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
