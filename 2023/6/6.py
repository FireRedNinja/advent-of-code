import re
from functools import reduce

from utils import get_input

DAY = "6"
YEAR = "2023"


def parse(puzzle_input: str):
    """Parse input"""
    data = [
        list(map(int, re.findall(r"\d+", line.split(":")[1])))
        for line in puzzle_input.strip().splitlines()
    ]
    return data


def part1(data):
    """Solve part 1"""

    new_data = list(zip(data[0], data[1]))
    records = []
    for [time_limit, distance_limit] in new_data:
        i = 1
        record_breakers = 0
        while i < time_limit:
            # distance = speed * time
            d = (i) * (time_limit - i)

            if d > distance_limit:
                record_breakers += 1
            i += 1

        records.append(record_breakers)

    ans = reduce(lambda x, y: x * y, records)
    return ans


def part2(data):
    """Solve part 2"""
    new_data = [map(str, line) for line in data]
    time_limit = int("".join(new_data[0]))
    distance_limit = int("".join(new_data[1]))

    i = 1
    record_breakers = 0
    while i < time_limit:
        # distance = speed * time
        d = (i) * (time_limit - i)

        if d > distance_limit:
            record_breakers += 1
        i += 1

    return record_breakers

    return f"Not implemented"


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 288
    assert test_solutions[1] == 71503

    solutions = solve(puzzle_input)
    assert solutions[0] == 1108800
    assert solutions[1] == 36919753

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
