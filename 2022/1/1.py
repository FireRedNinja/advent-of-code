import requests
from pathlib import Path
import sys

from dotenv import dotenv_values

config = dotenv_values('.env')
session_token = config["AOC_TOKEN"]

def get_input(day, year):
    puzzle_input = Path(f"./{year}/{day}/input.txt")
    print(f"Input Data: {puzzle_input}")

    if puzzle_input.is_file():
        return Path(puzzle_input).read_text().strip()
    
    url = "https://adventofcode.com/2022/day/"+str(day)+"/input"
    headers = {'Cookie': 'session='+session_token}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        puzzle_input.write_text(r.text)
        return r.text
    else:
        sys.exit(f"/api/alerts response: {r.status_code}: {r.reason} \n{r.content}")


def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split('\n')]


def parse(puzzle_input):
    """Parse input"""
    return [[int(cal) for cal in line.split('\n')] for line in puzzle_input.split('\n\n')]


def part1(data):
    """Solve part 1"""
    for i in range(len(data)):
        data[i] = sum(data[i])
    data.sort()
    return f'Most Calories: {data[-1]}'


def part2(data):
    """Solve part 2"""
    return f'Most Calories: {sum(data[-3:])}'


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    day = '1'
    year = "2022"

    puzzle_input = get_input(day, year)

    solutions = solve(puzzle_input)
    print('\nSolutions:')
    print(f'\tPart 1: {solutions[0]}\n\tPart 2: {solutions[1]}')
