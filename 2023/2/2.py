from collections import defaultdict
from functools import reduce

from utils import get_input

DAY = "2"
YEAR = "2023"


def parse(puzzle_input: str):
    """Parse input"""
    return [
        {
            "id": int(line[: line.index(":")].split()[1]),
            "games": [
                [colour.split() for colour in game.strip().split(", ")]
                for game in line[line.index(":") + 1 :].split(";")
            ],
        }
        for line in puzzle_input.strip().splitlines()
    ]


def part1(data):
    """Solve part 1"""
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    game_ids = []
    for line in data:
        id = line["id"]
        games = line["games"]

        invalid = False
        for game in games:
            for colour in game:
                [num, colour_name] = colour
                if int(num) > max_cubes[colour_name]:
                    invalid = True
                    break
                if invalid:
                    break
            if invalid:
                break
        if not invalid:
            game_ids.append(id)
        invalid = False
    return sum(game_ids)


def part2(data):
    """Solve part 2"""
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    powers = []
    for line in data:
        games = line["games"]

        max_cubes = defaultdict(int)
        for game in games:
            for colour in game:
                [num, colour_name] = colour
                num = int(num)
                max_cubes[colour_name] = max(max_cubes[colour_name], num)
        powers.append(reduce(lambda x, y: x * y, max_cubes.values()))
    return sum(powers)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 8
    assert test_solutions[1] == 2286

    solutions = solve(puzzle_input)
    assert solutions[0] == 2239
    # assert solutions[1] ==

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
