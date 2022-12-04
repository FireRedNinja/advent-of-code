import pathlib
import sys
from functools import reduce


def parse(puzzle_input):
    """Parse input"""
    return [[int(char) for char in list(line)] for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    risk_levels = []
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            adjacent = []
            if j is 0:
                adjacent.append(data[i][j + 1])
            elif j is len(row) - 1:
                adjacent.append(data[i][j - 1])
            else:
                adjacent.append(data[i][j - 1])
                adjacent.append(data[i][j + 1])

            if i is 0:
                adjacent.append(data[i + 1][j])
            elif i is len(data) - 1:
                adjacent.append(data[i - 1][j])
            else:
                adjacent.append(data[i - 1][j])
                adjacent.append(data[i + 1][j])

            if all(k > col for k in adjacent):
                risk_levels.append(col + 1)
    return f"Risk Levels: {sum(risk_levels)}"


def connect_basins(basins, point):
    points = [point]

    if (point[0] - 1, point[1]) in basins:
        basins.remove((point[0] - 1, point[1]))
        basins, adj_points = connect_basins(basins, (point[0] - 1, point[1]))
        points += adj_points
    if (point[0] + 1, point[1]) in basins:
        basins.remove((point[0] + 1, point[1]))
        basins, adj_points = connect_basins(basins, (point[0] + 1, point[1]))
        points += adj_points
    if (point[0], point[1] - 1) in basins:
        basins.remove((point[0], point[1] - 1))
        basins, adj_points = connect_basins(basins, (point[0], point[1] - 1))
        points += adj_points
    if (point[0], point[1] + 1) in basins:
        basins.remove((point[0], point[1] + 1))
        basins, adj_points = connect_basins(basins, (point[0], point[1] + 1))
        points += adj_points

    return basins, points


def part2(data):
    """Solve part 2"""
    basins = set()
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            adjacent = []
            if j is 0:
                adjacent.append([data[i][j + 1], (i, j + 1)])
            elif j is len(row) - 1:
                adjacent.append([data[i][j - 1], (i, j - 1)])
            else:
                adjacent.append([data[i][j - 1], (i, j - 1)])
                adjacent.append([data[i][j + 1], (i, j + 1)])

            if i is 0:
                adjacent.append([data[i + 1][j], (i + 1, j)])
            elif i is len(data) - 1:
                adjacent.append([data[i - 1][j], (i - 1, j)])
            else:
                adjacent.append([data[i - 1][j], (i - 1, j)])
                adjacent.append([data[i + 1][j], (i + 1, j)])

            for val, point in adjacent:
                if val is not 9:
                    basins.add(point)

    basin_sizes = []
    while len(basins) > 0:
        point = basins.pop()
        basins, basin_points = connect_basins(basins, point)
        basin_sizes.append(basin_points)

    basin_sizes = [len(sizes) for sizes in basin_sizes]
    basin_sizes.sort(reverse=True)

    return f"Largest Basin Sizes: {reduce((lambda x, y: x*y), basin_sizes[:3])}"


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
