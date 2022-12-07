from utils import get_input

DAY = "6"
YEAR = "2022"


def parse(puzzle_input: str):
    """Parse input"""
    return puzzle_input.strip()


def part1(data):
    """Solve part 1"""
    for i in range(3, len(data)):
        if len(set(data[i - 3 : i + 1])) == 4:
            return i + 1
    return 0


def part2(data):
    """Solve part 2"""
    for i in range(13, len(data)):
        if len(set(data[i - 13 : i + 1])) == 14:
            return i + 1
    return 0


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve("bvwbjplbgvbhsrlpgdmjqwftvncz")
    assert test_solutions[0] == 5
    assert test_solutions[1] == 23

    test_solutions = solve("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
    assert test_solutions[1] == 19

    test_solutions = solve("nppdvjthqldpwncqszvftbrmjlhg")
    assert test_solutions[1] == 23

    test_solutions = solve("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
    assert test_solutions[1] == 29

    solutions = solve(puzzle_input)
    assert solutions[0] == 1262
    assert solutions[1] == 3444

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
