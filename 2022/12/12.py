from utils import get_input
from string import ascii_lowercase
from collections import deque

DAY = "12"
YEAR = "2022"


def parse(puzzle_input: str):
    """Parse input"""
    return [list(line) for line in puzzle_input.strip().splitlines()]


def get_height(el: str) -> int:
    alphabet = list(ascii_lowercase)

    if el == "S":
        return alphabet.index("a")
    elif el == "E":
        return alphabet.index("z")

    return alphabet.index(el)


def part1(data):
    """Solve part 1"""

    START = None
    END = None

    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "S":
                START = (col, row)
            elif data[row][col] == "E":
                END = (col, row)

    def bfs(node: tuple):

        q = deque()
        q.append((0, node[0], node[1]))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while len(q) > 0:
            distance, x, y = q.popleft()

            if (x, y) == START:
                return distance

            for d in directions:
                d_x, d_y = d

                if (
                    0 > y + d_y
                    or y + d_y >= len(data)
                    or 0 > x + d_x
                    or x + d_x >= len(data[0])
                ):
                    continue

                d_h = get_height(data[y + d_y][x + d_x])
                n_h = get_height(data[y][x])

                if n_h - d_h > 1:
                    continue
                if (distance + 1, x + d_x, y + d_y) not in q:
                    q.append((distance + 1, x + d_x, y + d_y))

    res = bfs(END)
    return res


def part2(data):
    """Solve part 2"""
    END = None
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "E":
                END = (col, row)

    def bfs(node: tuple):

        q = deque()
        q.append((0, node[0], node[1]))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while len(q) > 0:
            distance, x, y = q.popleft()

            if data[y][x] == "a":
                return distance

            for d in directions:
                d_x, d_y = d

                if (
                    0 > y + d_y
                    or y + d_y >= len(data)
                    or 0 > x + d_x
                    or x + d_x >= len(data[0])
                ):
                    continue

                d_h = get_height(data[y + d_y][x + d_x])
                n_h = get_height(data[y][x])

                if n_h - d_h > 1:
                    continue
                if (distance + 1, x + d_x, y + d_y) not in q:
                    q.append((distance + 1, x + d_x, y + d_y))

    res = bfs(END)
    return res


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 31
    assert test_solutions[1] == 29

    solutions = solve(puzzle_input)
    assert solutions[0] == 437
    assert solutions[1] == 430

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
