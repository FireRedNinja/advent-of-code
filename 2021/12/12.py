import pathlib
import sys
from collections import Counter, defaultdict


def parse(puzzle_input):
    """Parse input"""
    graph = defaultdict(set)
    data = [tuple(line.split("-")) for line in puzzle_input.split("\n")]
    for start, end in data:
        graph[start].update([end])
        graph[end].update([start])
    return graph


def find_paths(graph, start, path=[]) -> list:
    end = "end"
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if (node.islower() and node in path) or node == "start":
            continue

        newpaths = find_paths(graph, node, path)
        paths += newpaths
    return paths


def part1(data):
    """Solve part 1"""
    paths = find_paths(data, "start")
    return f"Paths: {len(paths)}"


def find_paths2(graph, start, path=[]) -> list:
    end = "end"
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node.islower():
            lower_counts = Counter(
                list(filter(lambda n: n.islower() and n != "start", path))
            )
            if (
                len(list(filter(lambda n: n > 1, lower_counts.values()))) > 0
                and node in lower_counts.keys()
            ) or node == "start":
                continue

        newpaths = find_paths2(graph, node, path)
        paths += newpaths
    return paths


def part2(data):
    """Solve part 2"""
    paths = find_paths2(data, "start")

    return f"Paths: {len(paths)}"


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
