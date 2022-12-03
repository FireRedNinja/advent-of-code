import requests
from pathlib import Path
import sys
import string

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
    return [line for line in puzzle_input.split("\n")]

alphabet = string.ascii_letters


def part1(data):
    """Solve part 1"""
    prio = 0
    for i in data:
        errors = set(i[:len(i)//2]).intersection(set(i[len(i)//2:]))
        prio += sum([alphabet.index(e)+1 for e in errors])
    return f"Total Priorities: {prio}"


def part2(data):
    """Solve part 2"""
    prio = 0
    for i in range(0, len(data), 3):
        items = set()
        for elf in data[i:i+3]:
            items = set(elf) if len(items) == 0 else set(items).intersection(set(elf))
        prio += alphabet.index(list(items)[0])+1
    return f"Total Priorities: {prio}"


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    DAY = "3"
    YEAR = "2022"

    puzzle_input = get_input(DAY, YEAR)

    solutions = solve(puzzle_input)
    print("\nSolutions:")
    print(f"\tPart 1: {solutions[0]}\n\tPart 2: {solutions[1]}")
