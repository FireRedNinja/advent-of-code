from functools import reduce

from utils import get_input

DAY = "3"
YEAR = "2023"


def parse(puzzle_input: str):
    """Parse input"""
    return [line for line in puzzle_input.strip().splitlines()]


DIRECTIONS = [
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [-1, 0],
    [-1, -1],
    [0, -1],
    [-1, 1],
]


def part1(data):
    """Solve part 1"""
    nums = []
    for row, _ in enumerate(data):
        i_1, i_2 = 0, 0
        number = None

        while i_2 < len(data[row]):
            i_1 = i_2

            while i_2 < len(data[row]) and data[row][i_2].isdigit():
                i_2 += 1

            number = data[row][i_1:i_2]
            if number == "":
                i_2 += 1
                continue

            number = int(number)

            is_part_num = False
            for i in range(i_1, i_2):
                if is_part_num is True:
                    break

                for direction in DIRECTIONS:
                    new_loc = [row + direction[0], i + direction[1]]

                    # ignore points for the current number
                    if new_loc[0] is row and new_loc[1] in range(i_1, i_2):
                        continue

                    if new_loc[0] in range(len(data)) and new_loc[1] in range(
                        len(data[row])
                    ):
                        engine = data[new_loc[0]][new_loc[1]]
                        if engine != "." and not engine.isdigit():
                            is_part_num = True
                            break

            if is_part_num is True:
                nums.append(number)

    return sum(nums)


def get_adjacent_numbers(data: list[str], row: int, col: int) -> list[int]:
    adjacent_numbers = []

    visited = set()
    for dir_x, dir_y in DIRECTIONS:
        new_point = (row + dir_y, col + dir_x)
        if new_point in visited:
            continue

        if data[new_point[0]][new_point[1]].isdigit():
            i_left, i_right = new_point[1], new_point[1]

            # watch out for overshoot
            while i_left >= 0 and data[new_point[0]][i_left].isdigit():
                i_left -= 1
                visited.add((new_point[0], i_left))

            while (
                i_right < len(data[new_point[0]])
                and data[new_point[0]][i_right].isdigit()
            ):
                i_right += 1
                visited.add((new_point[0], i_right))

            if data[new_point[0]][i_left + 1 : i_right] != "":
                adjacent_numbers.append(int(data[new_point[0]][i_left + 1 : i_right]))

    return adjacent_numbers


def part2(data: list[str]):
    """Solve part 2"""
    nums = []

    for row, line in enumerate(data):
        for col, character in enumerate(line):
            if character == "*":
                adjacent_numbers = get_adjacent_numbers(data, row, col)

                if len(adjacent_numbers) > 1:
                    nums.append(reduce(lambda x, y: x * y, adjacent_numbers))

    return sum(nums)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 4361
    assert test_solutions[1] == 467835

    solutions = solve(puzzle_input)
    assert solutions[0] == 535078
    assert solutions[1] == 75312571

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
