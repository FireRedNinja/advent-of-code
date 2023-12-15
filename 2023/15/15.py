from utils import get_input
from collections import defaultdict

DAY = "15"
YEAR = "2023"


def parse(puzzle_input: str):
    """Parse input"""
    return [line for line in puzzle_input.strip().split(",")]


def part1(data):
    """Solve part 1"""
    ans = 0
    for line in data:
        curr_val = 0
        for char in line:
            curr_val += ord(char)
            curr_val *= 17
            curr_val %= 256
        ans += curr_val
    return ans


def part2(data):
    """Solve part 2"""

    boxes = defaultdict(list)

    for step in data:
        if "=" in step:
            [label, focal_length] = step.split("=")
            box = 0
            for char in label:
                box += ord(char)
                box *= 17
                box %= 256

            contains_lense = False
            for i, lense in enumerate(boxes[box]):
                if lense[0] == label:
                    contains_lense = True
                    boxes[box][i] = (label, focal_length)
            if not contains_lense:
                boxes[box].append((label, focal_length))

        elif "-" in step:
            label = step.split("-")[0]
            box = 0
            for char in label:
                box += ord(char)
                box *= 17
                box %= 256

            for i, lense in enumerate(boxes[box]):
                if lense[0] == label:
                    del boxes[box][i]

    focusing_power = 0
    for box in sorted(boxes.keys()):
        for i, lense in enumerate(boxes[box]):
            label, focal_length = lense
            focusing_power += (box + 1) * (i + 1) * (int(focal_length))

    return focusing_power


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 1320
    assert test_solutions[1] == 145

    solutions = solve(puzzle_input)
    assert solutions[0] == 521341
    assert solutions[1] == 252782

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
