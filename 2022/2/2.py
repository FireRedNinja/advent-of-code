import sys
from pathlib import Path

import requests
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


opponent = ["A", "B", "C"]
me = ["X", "Y", "Z"]


def parse(puzzle_input):
    """Parse input"""
    return [[choice for choice in line.split(" ")] for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    score = 0
    for i in range(len(data)):
        opponent_i = opponent.index(data[i][0])
        me_i = me.index(data[i][1])
        if opponent_i - me_i == 0:  # draw
            score += (me_i + 1) + 3
        elif me_i - opponent_i == 1 or opponent_i - me_i == 2:  # win
            score += (me_i + 1) + 6
        elif opponent_i - me_i == 1 or me_i - opponent_i == 2:  # loss
            score += me_i + 1
    return f"Total Score: {score}"


def part2(data):
    """Solve part 2"""
    score = 0
    for i in range(len(data)):
        opponent_i = opponent.index(data[i][0])
        me_i = me.index(data[i][1])
        me_outcome = data[i][1]
        if me_outcome == "Y":  # draw
            score += (opponent_i + 1) + 3
        elif me_outcome == "Z":  # win
            score += (0 if opponent_i == 2 else opponent_i + 1) + 1 + 6
        elif me_outcome == "X":  # loss
            score += (2 if opponent_i == 0 else opponent_i - 1) + 1
    return f"Total Score: {score}"


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    DAY = "2"
    YEAR = "2022"

    puzzle_input = get_input(DAY, YEAR)

    solutions = solve(puzzle_input)
    print("\nSolutions:")
    print(f"\tPart 1: {solutions[0]}\n\tPart 2: {solutions[1]}")
