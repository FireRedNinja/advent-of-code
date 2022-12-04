import requests
from pathlib import Path
import sys

from dotenv import dotenv_values

config = dotenv_values(".env")
session_token = config["AOC_TOKEN"]


def get_input(day, year):
    puzzle_input = Path(f"./{year}/{day}/{day}.txt")
    print(f"Input Data: {puzzle_input}")

    if puzzle_input.is_file():
        return Path(puzzle_input).read_text(encoding="utf-8").strip()

    url = "https://adventofcode.com/2022/day/" + str(day) + "/input"
    headers = {"Cookie": "session=" + session_token}
    req = requests.get(url, headers=headers, timeout=5)
    if req.status_code == 200:
        puzzle_input.write_text(req.text, encoding="utf-8")
        return req.text
    else:
        sys.exit(
            f"/api/alerts response: {req.status_code}: {req.reason} \n{req.content}"
        )


def parse(puzzle_input):
    """Parse input"""
    return [[[int(section) for section in sections.split('-')] for sections in line.split(',')] for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    count = 0
    for [a, b] in data:
        if [max(a[0], b[0]), min(a[1], b[1])] in [a, b]:
            count += 1
    return f"Fully Contain: {count}"


def part2(data):
    """Solve part 2"""
    count = 0
    for i in data:
        i.sort(key=lambda x: x[0])
        i1 = i[0]
        i2 = i[1]
        if i1[1] >= i2[0]:
            count += 1
    return f"Overlaps: {count}"


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    DAY = "4"
    YEAR = "2022"

    puzzle_input = get_input(DAY, YEAR)

    solutions = solve(puzzle_input)
    print("\nSolutions:")
    print(f"\tPart 1: {solutions[0]}\n\tPart 2: {solutions[1]}")
