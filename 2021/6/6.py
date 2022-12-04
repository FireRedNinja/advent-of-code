import pathlib
import sys
from pdb import set_trace

import numpy as np


def parse(puzzle_input):
    """Parse input"""
    return [int(age) for age in puzzle_input.split(",")]


def part1(data):
    """Solve part 1"""
    data = np.array(data)
    days = 80
    for _ in range(days):
        data = data - 1
        zeros = np.where(data == -1)
        data[zeros] = 6
        data = np.append(data, np.full(len(zeros[0]), 8))
    return f"Fishes: {len(data)}"


def part2(data: list):
    """Solve part 2"""
    data = np.array(data)
    days = 256
    data = {
        0: len(np.where(data == 0)[0]),
        1: len(np.where(data == 1)[0]),
        2: len(np.where(data == 2)[0]),
        3: len(np.where(data == 3)[0]),
        4: len(np.where(data == 4)[0]),
        5: len(np.where(data == 5)[0]),
        6: len(np.where(data == 6)[0]),
        7: len(np.where(data == 7)[0]),
        8: len(np.where(data == 8)[0]),
    }

    for _ in range(days):
        newData = {
            0: data[1],
            1: data[2],
            2: data[3],
            3: data[4],
            4: data[5],
            5: data[6],
            6: data[7] + data[0],
            7: data[8],
            8: data[0],
        }
        data = newData

    return f"Fishes: {sum(data.values())}"


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
