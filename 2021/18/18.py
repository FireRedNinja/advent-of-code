import json
import math
import pathlib
from copy import deepcopy


def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split("\n")]


def set_left(val, data):
    left_set = False
    for i in range(len(data) - 1, -1, -1):
        if isinstance(data[i], int):
            left_set = True
            data[i] = val + data[i]
            return left_set, data
        else:
            left_set, data[i] = set_left(val, data[i])
            return left_set, data
    return False, None


def set_right(val, data):
    right_set = False
    for i in range(len(data)):
        if isinstance(data[i], int):
            right_set = True
            data[i] = val + data[i]
            return right_set, data
        else:
            right_set, data[i] = set_right(val, data[i])
            return right_set, data
    return False, None


def explode(depth: int, data: list):
    """Explode the data"""
    depth += 1

    exploded = False
    left_set = False
    left_val = None
    right_set = False
    right_val = None

    for i in range(len(data)):
        if isinstance(data[i], list):

            if all(isinstance(item, int) for item in data[i]) and depth >= 4:
                exploded = True
                left_val, right_val = data[i]

                new_left = None
                new_right = None

                if not left_set:
                    left_set, new_left = set_left(left_val, data[:i])

                if not right_set and i + 1 < len(data):
                    right_set, new_right = set_right(right_val, data[i + 1 :])

                if left_set:
                    data = new_left
                else:
                    data = [0]

                if right_set:
                    data += new_right
                else:
                    data.append(0)
            else:
                (
                    exploded,
                    new_data,
                    (left_set, left_val),
                    (right_set, right_val),
                ) = explode(depth, data[i])
                data[i] = new_data

                if exploded:
                    if not left_set:
                        left_set, new_left = set_left(left_val, data[:i])

                        if left_set:
                            data[:i] = new_left

                    if not right_set and i + 1 < len(data):
                        right_set, new_right = set_right(right_val, data[i + 1 :])

                        if right_set:
                            data[i + 1 :] = new_right

            if exploded:
                return exploded, data, (left_set, left_val), (right_set, right_val)
    return exploded, data, (left_set, left_val), (right_set, right_val)


def split(data):
    has_split = False

    for i in range(len(data)):
        if isinstance(data[i], list):
            has_split, data[i] = split(data[i])

            if has_split:
                break
        else:
            if data[i] > 9:
                data[i] = [math.floor(data[i] / 2), math.ceil(data[i] / 2)]
                has_split = True
                break

    return has_split, data


def add(a, b):
    snailfish = [a, b]

    exploded = False
    has_split = False

    while True:
        exploded, snailfish, *_ = explode(0, snailfish)

        if exploded:
            exploded = False
            continue

        has_split, snailfish = split(snailfish)

        if has_split:
            has_split = False
            continue

        if not exploded and not has_split:
            break

    return snailfish


def magnitude(data):
    """Calculate the magnitude of the data"""
    if isinstance(data, int):
        return data
    else:
        return (3 * magnitude(data[0])) + (2 * magnitude(data[1]))


def part1(data):
    """Solve part 1"""
    data = list(map(json.loads, data))
    snailfish = data[0]

    for line in data[1:]:
        snailfish = add(snailfish, line)
    return f"Magnitude: {magnitude(snailfish)}"


def part2(data):
    """Solve part 2"""
    data = list(map(json.loads, data))
    max_magnitude = 0

    for i, i_data in enumerate(data):
        other_data = data[:i] + data[i + 1 :]

        for j in other_data:
            a = deepcopy(i_data)
            b = deepcopy(j)

            snailfish = add(a, b)

            max_magnitude = max(magnitude(snailfish), max_magnitude)
    return f"Largest Magnitude: {max_magnitude}"


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    path = "./18/18.txt"
    print(f"Input Data: {path}")
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\nSolutions:")
    print(f"\tPart 1: {solutions[0]}\n\tPart 2: {solutions[1]}")
