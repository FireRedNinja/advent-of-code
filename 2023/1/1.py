import re

from utils import get_input

DAY = "1"
YEAR = "2023"

nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def parse(puzzle_input: str):
    """Parse input"""
    return [line for line in puzzle_input.strip().splitlines()]


def part1(data):
    """Solve part 1"""
    digits = [[i for i in line if i.isdigit()] for line in data]
    digits = [int(line[0] + line[-1]) for line in digits]

    return sum(digits)


def part2(data):
    """Solve part 2"""
    digits = []
    # [[i for i in line if i.isdigit()] for line in data]
    for line in data:
        letters = []
        digs = []
        for char in line:
            if char.isdigit():
                digs.append(char)
                letters = []
            else:
                letters.append(char)
                for key in nums.keys():
                    if key in "".join(letters):
                        digs.append(nums[key])
                        letters = letters[-1:]

        digits.append(digs)

    digits = [int(line[0] + line[-1]) for line in digits]

    return sum(digits)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    # solution1 = part1(data)
    solution1 = ""
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    # assert test_solutions[0] == 142
    assert test_solutions[1] == 281

    solutions = solve(puzzle_input)
    # assert solutions[0] == 54390
    # assert solutions[1] ==

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
