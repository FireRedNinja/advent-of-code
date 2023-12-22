from utils import get_input
import re
import numpy as np
from pprint import pprint
from collections import Counter, deque

DAY = "22"
YEAR = "2023"


def parse(puzzle_input: str):
    """Parse input"""
    return [
        [list(map(int, re.findall(r"\d+", coords))) for coords in line.split("~")]
        for line in puzzle_input.strip().splitlines()
    ]


def printx(data):
    p = []

    for i in range(len(data)):
        row = []
        for j in range(len(data[0][0])):
            if j == 0:
                row.append("-")
                continue

            x = [k for k in data[i, :, j] if k != 0]
            if x == []:
                row.append(".")
            else:
                row.append(int(x[0]))
        p.append(row)
    p = np.array(p)
    p = np.rot90(p)
    print("x x z")
    pprint(p.tolist())


def printy(data):
    p = []

    for i in range(len(data[0])):
        row = []
        for j in range(len(data[0][0])):
            if j == 0:
                row.append("-")
                continue

            x = [k for k in data[:, i, j] if k != 0]
            if x == []:
                row.append(".")
            else:
                row.append(int(x[0]))
        p.append(row)
    p = np.array(p)
    p = np.rot90(p)
    print("y x z")
    pprint(p.tolist())


def part1(data):
    """Solve part 1"""
    data = np.array(data)

    """
        x = data[0]
        y = data[0][0]
        z = data[0][0][0]
    """
    bricks_grid = np.zeros(
        (
            max(max(data[:, 0, 0]), max(data[:, 1, 0])) + 1,
            max(max(data[:, 0, 1]), max(data[:, 1, 1])) + 1,
            max(max(data[:, 0, 2]), max(data[:, 1, 2])) + 1,
        )
    )
    bricks_dict = {}

    for i, [b_start, b_end] in enumerate(data):
        bricks_grid[
            b_start[0] : b_end[0] + 1,
            b_start[1] : b_end[1] + 1,
            b_start[2] : b_end[2] + 1,
        ] = i + 1
        bricks_dict[i + 1] = (b_start, b_end)

    # make all the bricks in the air fall to rest
    prev_state = bricks_grid.copy()
    while True:
        for i in range(1, len(bricks_dict.keys()) + 1):
            b_start, b_end = bricks_dict[i]
            if b_start[2] == 0 or b_end[2] == 0:
                continue

            j = 1
            while True:
                if b_start[2] - j <= 0 or b_end[2] - j <= 0:
                    break

                new_loc = bricks_grid[
                    b_start[0] : b_end[0] + 1,
                    b_start[1] : b_end[1] + 1,
                    b_start[2] - j : b_end[2] + 1 - j,
                ]

                # see if the location is only empty and the brick itself
                space = np.unique(new_loc)
                bricks_below = [k for k in space if k not in [0, i]]
                if len(bricks_below) > 0:
                    break

                # set its last location to air
                bricks_grid[
                    b_start[0] : b_end[0] + 1,
                    b_start[1] : b_end[1] + 1,
                    b_start[2] - j + 1 : b_end[2] + 1 - j + 1,
                ] = 0

                # set new position of brick
                bricks_grid[
                    b_start[0] : b_end[0] + 1,
                    b_start[1] : b_end[1] + 1,
                    b_start[2] - j : b_end[2] + 1 - j,
                ] = i

                # update dict
                bricks_dict[i] = (
                    [b_start[0], b_start[1], b_start[2] - j],
                    [b_end[0], b_end[1], b_end[2] - j],
                )

                j += 1
        pass
        if np.array_equal(prev_state, bricks_grid):
            break
        prev_state = bricks_grid.copy()

    # for each brick see if there is a brick occupyin in a space z + 1
    supporting_bricks = {}
    for i, bricks in bricks_dict.items():
        (b_start, b_end) = bricks
        new_loc = bricks_grid[
            b_start[0] : b_end[0] + 1,
            b_start[1] : b_end[1] + 1,
            b_start[2] + 1 : b_end[2] + 1 + 1,
        ]

        space = np.unique(new_loc)
        adjacent_bricks = [j for j in space if j not in [0, i]]
        supporting_bricks[i] = adjacent_bricks

    ans = 0
    # for each supporting brick if that has a brick supporting it then this one can be deleted
    for i, bricks in supporting_bricks.items():
        can_disintegrate = True

        for b in bricks:
            if len([True for j in supporting_bricks.values() if b in j]) <= 1:
                can_disintegrate = False
                break

        if can_disintegrate:
            ans += 1

    return ans


def part2(data):
    """Solve part 2"""
    data = np.array(data)

    """
        x = data[0]
        y = data[0][0]
        z = data[0][0][0]
    """
    bricks_grid = np.zeros(
        (
            max(max(data[:, 0, 0]), max(data[:, 1, 0])) + 1,
            max(max(data[:, 0, 1]), max(data[:, 1, 1])) + 1,
            max(max(data[:, 0, 2]), max(data[:, 1, 2])) + 1,
        )
    )
    bricks_dict = {}

    for i, [b_start, b_end] in enumerate(data):
        bricks_grid[
            b_start[0] : b_end[0] + 1,
            b_start[1] : b_end[1] + 1,
            b_start[2] : b_end[2] + 1,
        ] = i + 1
        bricks_dict[i + 1] = (b_start, b_end)

    # make all the bricks in the air fall to rest
    prev_state = bricks_grid.copy()
    while True:
        for i in range(1, len(bricks_dict.keys()) + 1):
            b_start, b_end = bricks_dict[i]
            if b_start[2] == 0 or b_end[2] == 0:
                continue

            j = 1
            while True:
                if b_start[2] - j <= 0 or b_end[2] - j <= 0:
                    break

                new_loc = bricks_grid[
                    b_start[0] : b_end[0] + 1,
                    b_start[1] : b_end[1] + 1,
                    b_start[2] - j : b_end[2] + 1 - j,
                ]

                # see if the location is only empty and the brick itself
                space = np.unique(new_loc)
                bricks_below = [k for k in space if k not in [0, i]]
                if len(bricks_below) > 0:
                    break

                # set its last location to air
                bricks_grid[
                    b_start[0] : b_end[0] + 1,
                    b_start[1] : b_end[1] + 1,
                    b_start[2] - j + 1 : b_end[2] + 1 - j + 1,
                ] = 0

                # set new position of brick
                bricks_grid[
                    b_start[0] : b_end[0] + 1,
                    b_start[1] : b_end[1] + 1,
                    b_start[2] - j : b_end[2] + 1 - j,
                ] = i

                # update dict
                bricks_dict[i] = (
                    [b_start[0], b_start[1], b_start[2] - j],
                    [b_end[0], b_end[1], b_end[2] - j],
                )

                j += 1
        pass
        if np.array_equal(prev_state, bricks_grid):
            break
        prev_state = bricks_grid.copy()

    # for each brick see if there is a brick occupyin in a space z + 1
    supporting_bricks = {}
    for i, bricks in bricks_dict.items():
        (b_start, b_end) = bricks
        new_loc = bricks_grid[
            b_start[0] : b_end[0] + 1,
            b_start[1] : b_end[1] + 1,
            b_start[2] + 1 : b_end[2] + 1 + 1,
        ]

        space = np.unique(new_loc)
        adjacent_bricks = [j for j in space if j not in [0, i]]
        supporting_bricks[i] = adjacent_bricks

    ans = 0
    # for each supporting brick if that has a brick supporting it then this one can be deleted
    for key, bricks in supporting_bricks.items():
        counts = Counter([item for i in supporting_bricks.values() for item in i])

        q = deque()
        q.append(key)

        while len(q) > 0:
            name = q.popleft()
            if supporting_bricks[name] == []:
                continue

            for b in supporting_bricks[name]:
                counts[b] -= 1
                if counts[b] == 0:
                    q.append(b)
                    ans += 1

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
    assert test_solutions[0] == 5
    assert test_solutions[1] == 7

    solutions = solve(puzzle_input)
    assert solutions[0] == 503
    assert solutions[1] == 98431

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
