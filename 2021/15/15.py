from typing import Tuple
import pathlib
import sys
from pdb import set_trace as st
import numpy as np

DIRECTIONS = [
    [-1, 0],
    [0, -1],
    [1, 0],
    [0, 1],
]


def parse(puzzle_input):
    """Parse input"""
    return [[int(i) for i in list(line)] for line in puzzle_input.split('\n')]


def search(grid, start: Tuple[int, int], goal: Tuple[int, int]):
    shortest_path = {}

    shortest_path[start] = 0

    current_cell = start
    queue = [(0, current_cell)]
    while queue:
        cost, current_cell = queue[0]
        if current_cell == goal:
            break

        queue = queue[1:]
        for i in range(len(DIRECTIONS)):
            neighbor_x = current_cell[0] + DIRECTIONS[i][0]
            neighbor_y = current_cell[1] + DIRECTIONS[i][1]
            neighbor = (neighbor_x, neighbor_y)

            if neighbor_x >= 0 and neighbor_x < len(grid[0]) and neighbor_y >= 0 and neighbor_y < len(grid):
                new_cost = cost + grid[neighbor_y][neighbor_x]

                if neighbor in shortest_path and new_cost >= shortest_path[
                        neighbor]:
                    continue

                shortest_path[neighbor] = new_cost
                queue.append((new_cost, neighbor))

        queue = sorted(queue, key=lambda x: x[0])
    return shortest_path[goal]


def part1(data):
    """Solve part 1"""
    start = (0, 0)
    goal = tuple([len(data) - 1, len(data[0]) - 1])

    cost = search(data, start, goal)

    return f'Cost: {cost}'


def part2(data):
    """Solve part 2"""
    data = np.array(data)

    row = [data]
    for _ in range(4):
        new_data = row[-1] + 1
        new_data[new_data > 9] = 1
        row.append(new_data)
    data = np.concatenate(row, axis=1)
    col = [data]
    for _ in range(4):
        new_data = col[-1] + 1
        new_data[new_data > 9] = 1
        col.append(new_data)
    data = np.concatenate(col, axis=0)

    start = (0, 0)
    goal = tuple([len(data) - 1, len(data[0]) - 1])
    cost = search(data, start, goal)

    return f'Cost: {cost}'


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
        print('\nSolutions:')
        print(f'\tPart 1: {solutions[0]}\n\tPart 2: {solutions[1]}')
