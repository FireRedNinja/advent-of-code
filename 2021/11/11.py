import pathlib
import sys

import numpy as np


def parse(puzzle_input):
    """Parse input"""
    return [[int(char) for char in list(line)] for line in puzzle_input.split("\n")]


def adjacent_points(start_point, grid):
    """Return the adjacent points"""
    x, y = start_point
    points = []
    points.append((x - 1, y))
    points.append((x + 1, y))
    points.append((x, y - 1))
    points.append((x, y + 1))
    points.append((x - 1, y - 1))
    points.append((x + 1, y + 1))
    points.append((x - 1, y + 1))
    points.append((x + 1, y - 1))

    points = list(
        filter(
            lambda point: point[0] >= 0
            and point[0] <= len(grid[0]) - 1
            and point[1] >= 0
            and point[1] <= len(grid) - 1,
            points,
        )
    )
    return points


def increase_adjacents(point, grid):
    """Increase the value of the adjacent points"""
    adjacents = adjacent_points(point, grid)
    for adj in adjacents:
        if grid[adj] > 9:
            continue

        grid[adj] += 1
        if grid[adj] > 9:
            grid = increase_adjacents(adj, grid)
    return grid


def part1(data):
    """Solve part 1"""
    data = np.array(data)
    i = 100
    flashes = 0
    for _ in range(i):
        data += 1
        ready = list(zip(*np.where(data > 9)))

        while ready:
            point = ready.pop()
            data = increase_adjacents(point, data)

        ready = np.where(data > 9)
        flashes += len(ready[0])
        data[ready] = 0

    return f"Flashes: {flashes}"


def part2(data):
    """Solve part 2"""
    data = np.array(data)
    first_sync_flash = None
    i = 0
    while first_sync_flash is None:
        data += 1
        ready = list(zip(*np.where(data > 9)))

        while ready:
            point = ready.pop()
            data = increase_adjacents(point, data)

        ready = np.where(data > 9)
        flashes_now = len(ready[0])
        if flashes_now == len(data) * len(data[0]):
            first_sync_flash = i
        data[ready] = 0
        i += 1

    return f"Sync Flash Step: {i}"


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
