from utils import get_input
from json import loads
from random import randrange

DAY = "13"
YEAR = "2022"


def parse(puzzle_input: str):
    """Parse input"""
    return [
        [loads(i) for i in line.split("\n")]
        for line in puzzle_input.strip().split("\n\n")
    ]


def to_list(lst) -> list:
    if type(lst) == int:
        return [lst]
    return lst


def right_order(l, r) -> int:
    l_val = to_list(l)
    r_val = to_list(r)

    lp, rp = 0, 0
    while True:
        if lp == len(l_val) and rp == len(r_val):
            break
        elif lp == len(l_val) and rp < len(r_val):
            return 1
        elif lp < len(l_val) and rp == len(r_val):
            return -1

        if type(l_val[lp]) == list or type(r_val[rp]) == list:
            is_right_order = right_order(l_val[lp], r_val[rp])
            if is_right_order != 0:
                return is_right_order
        elif l_val[lp] > r_val[rp]:
            return -1
        elif l_val[lp] < r_val[rp]:
            return 1

        lp += 1
        rp += 1

    return 0


def sort(lst: list) -> list:
    if len(lst) < 2:
        return lst

    pivot_i = randrange(len(lst))
    pivot = lst[pivot_i]
    greater: list = []
    lesser: list = []

    for i in lst[:pivot_i]:
        (greater if right_order(i, pivot) == -1 else lesser).append(i)

    for i in lst[pivot_i + 1 :]:
        (greater if right_order(i, pivot) == -1 else lesser).append(i)

    return sort(lesser) + [pivot] + sort(greater)


def part1(data) -> int:
    """Solve part 1"""
    indexes = []
    for i in range(len(data)):
        l, r = data[i]
        if right_order(l, r) == 1:
            indexes.append(i + 1)
    return sum(indexes)


def part2(data):
    """Solve part 2"""
    new_data = []
    for i in data:
        l, r = i
        new_data.append(l)
        new_data.append(r)
    new_data.append([[2]])
    new_data.append([[6]])

    new_data = sort(new_data)

    return (new_data.index([[2]]) + 1) * (new_data.index([[6]]) + 1)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 13
    assert test_solutions[1] == 140

    solutions = solve(puzzle_input)
    assert solutions[0] == 6070
    assert solutions[1] == 20758

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
