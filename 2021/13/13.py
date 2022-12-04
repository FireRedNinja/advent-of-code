import pathlib
import sys
from pdb import set_trace as st

import numpy as np

np.set_printoptions(threshold=sys.maxsize)


def parse(dots, instructions):
    """Parse input"""
    dots = [[int(i) for i in line.split(",")] for line in dots.split("\n")]
    instructions = [
        tuple(line.split(" ")[-1].split("=")) for line in instructions.split("\n")
    ]

    return dots, instructions


def part1(data):
    """Solve part 1"""
    dots, instructions = data
    dots = np.array(dots)
    paper = np.empty((max(dots[:, 1]) + 1, max(dots[:, 0]) + 1))
    paper[dots[:, 1], dots[:, 0]] = 1

    for axis, index in instructions[:1]:
        bigger_side = None
        smaller_side = None
        if axis == "x":
            l = paper[:, : int(index)]
            r = paper[:, int(index) + 1 :]
            bigger_side = l if l.shape[1] > r.shape[1] else r
            smaller_side = l if np.all(bigger_side == r) else r

            smaller_side = np.pad(
                smaller_side,
                ((0, 0), (0, bigger_side.shape[1] - smaller_side.shape[1])),
                "constant",
                constant_values=0,
            )
            smaller_side = np.fliplr(smaller_side)
        elif axis == "y":
            t = paper[: int(index), :]
            b = paper[int(index) + 1 :, :]
            bigger_side = t if t.shape[0] > b.shape[0] else b
            smaller_side = t if np.all(bigger_side == b) else b

            smaller_side = np.pad(
                smaller_side,
                ((0, bigger_side.shape[0] - smaller_side.shape[0]), (0, 0)),
                "constant",
                constant_values=0,
            )
            smaller_side = np.flipud(smaller_side)

        paper = smaller_side + bigger_side

    return f"Number of Dots: {paper[paper[:] > 0].size}"


def part2(data):
    """Solve part 2"""
    dots, instructions = data
    dots = np.array(dots)
    paper = np.empty((max(dots[:, 1]) + 1, max(dots[:, 0]) + 1))
    paper[dots[:, 1], dots[:, 0]] = 1

    for axis, index in instructions:
        bigger_side = None
        smaller_side = None
        if axis == "x":
            l = paper[:, : int(index)]
            r = paper[:, int(index) + 1 :]
            bigger_side = l if l.shape[1] > r.shape[1] else r
            smaller_side = l if np.all(bigger_side == r) else r

            smaller_side = np.pad(
                smaller_side,
                ((0, 0), (0, bigger_side.shape[1] - smaller_side.shape[1])),
                "constant",
                constant_values=0,
            )
            smaller_side = np.fliplr(smaller_side)
        elif axis == "y":
            t = paper[: int(index), :]
            b = paper[int(index) + 1 :, :]
            bigger_side = t if t.shape[0] > b.shape[0] else b
            smaller_side = t if np.all(bigger_side == b) else b

            smaller_side = np.pad(
                smaller_side,
                ((0, bigger_side.shape[0] - smaller_side.shape[0]), (0, 0)),
                "constant",
                constant_values=0,
            )
            smaller_side = np.flipud(smaller_side)

        paper = smaller_side + bigger_side

    paper[paper[:] > 0] = 1

    paper = np.flipud(paper)
    paper = np.fliplr(paper)

    code = ""
    for i in paper:
        for j in i:
            if j == 1:
                code += "# "
            else:
                code += "  "
        code += "\n"

    return f"Code: \n{code}"


def solve(dots, instructions):
    """Solve the puzzle for the given input"""
    data = parse(dots, instructions)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    dot_path = "13_dots.txt"
    instructions_path = "13_instructions.txt"
    print(f"Input Data: {dot_path}, {instructions_path}")
    dots = pathlib.Path(dot_path).read_text().strip()
    instructions = pathlib.Path(instructions_path).read_text().strip()
    solutions = solve(dots, instructions)
    print("\nSolutions:")
    print(f"\tPart 1: {solutions[0]}\n\tPart 2: {solutions[1]}")
