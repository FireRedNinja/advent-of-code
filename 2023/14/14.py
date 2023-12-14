from utils import get_input
import numpy as np

DAY = "14"
YEAR = "2023"


def parse(puzzle_input: str):
    """Parse input"""
    return np.array([list(line) for line in puzzle_input.strip().splitlines()])


directions = {"N": 0, "E": 1, "S": 2, "W": 3}

def roll(pos, data):
    i, j = pos
    new_data = data
    new_pos = (i, j)
    for k in range(i - 1, -1, -1):
        if new_data[k][j] == ".":
            new_pos = (k, j)
        elif new_data[k][j] == "O" or new_data[k][j] == "#":
            break
    new_data[i][j] = "."
    new_data[new_pos[0]][new_pos[1]] = "O"
    return new_data


def tilt(data, dir):
    new_data = np.rot90(data, k=directions[dir])

    for i, row in enumerate(new_data):
        for j, col in enumerate(row):
            if col == "O":
                new_data = roll((i, j), new_data)

    new_data = np.rot90(new_data, k=-directions[dir])
    return new_data


def part1(data):
    """Solve part 1"""
    rocks = tilt(data, "N")

    load = 0
    for i, row in enumerate(rocks):
        load += len(list(filter(lambda x: x == "O", row))) * (len(rocks) - i)

    return load

def hash(rocks):
    return ''.join([''.join(i) for i in rocks])

def part2(data):
    """Solve part 2"""
    rocks = data
    prev_states = {}
    cycle_state = {}
    final_rocks = None
    for i in range(1000000000):
        rocks = tilt(rocks, "N")
        rocks = tilt(rocks, "W")
        rocks = tilt(rocks, "S")
        rocks = tilt(rocks, "E")
        
        if hash(rocks) in prev_states:
            cycle_start = prev_states[hash(rocks)]
            cycle_len =  i - cycle_start
            final_rocks = cycle_state[cycle_start + (((1000000000-1) - cycle_start) % cycle_len)]
            break

        prev_states[hash(rocks)] = i
        cycle_state[i] = rocks.copy()

    load = 0
    for i, row in enumerate(final_rocks):
        load += len(list(filter(lambda x: x == "O", row))) * (len(final_rocks) - i)

    return load


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 136
    assert test_solutions[1] == 64

    solutions = solve(puzzle_input)
    assert solutions[0] == 105982
    assert solutions[1] == 85175

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
