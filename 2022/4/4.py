from utils import get_input

DAY = "4"
YEAR = "2022"
TEST_DATA = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def parse(puzzle_input):
    """Parse input"""
    return [
        [
            [int(section) for section in sections.split("-")]
            for sections in line.split(",")
        ]
        for line in puzzle_input.strip().splitlines()
    ]


def part1(data):
    """Solve part 1"""
    count = 0
    for [a, b] in data:
        if [max(a[0], b[0]), min(a[1], b[1])] in [a, b]:
            count += 1
    return count


def part2(data):
    """Solve part 2"""
    count = 0
    for i in data:
        i.sort(key=lambda x: x[0])
        i1 = i[0]
        i2 = i[1]
        if i1[1] >= i2[0]:
            count += 1
    return count


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = get_input(DAY, YEAR)

    test_solutions = solve(TEST_DATA)
    assert test_solutions[0] == 2
    assert test_solutions[1] == 4

    solutions = solve(puzzle_input)
    assert solutions[0] == 494
    assert solutions[1] == 833

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
