from collections import deque
from copy import deepcopy

import numpy as np

from utils import get_input

DAY = "5"
YEAR = "2022"
TEST_DATA = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def parse(puzzle_input: str):
    """Parse input"""
    stack, instructions = [
        [line for line in section.splitlines()]
        for section in puzzle_input.split("\n\n")
    ]
    stack = [[line[i] for i in range(1, len(line), 4)] for line in stack]
    instructions = [line.split(" ") for line in instructions]
    stack = np.array(stack)
    stack = [list("".join(stack[:, col][:-1]).strip()) for col in range(stack.shape[1])]
    stack = [deque(line) for line in stack]
    return (stack, instructions)


def part1(data):
    """Solve part 1"""
    stack, instructions = data
    my_stack = deepcopy(stack)

    for i in instructions:
        val = [my_stack[int(i[3]) - 1].popleft() for j in range(int(i[1]))]
        my_stack[int(i[-1]) - 1].extendleft(val)

    ret = [i.popleft() for i in my_stack]
    return "".join(ret)


def part2(data):
    """Solve part 2"""
    stack, instructions = data
    my_stack = deepcopy(stack)

    for i in instructions:
        val = [my_stack[int(i[3]) - 1].popleft() for j in range(int(i[1]))]
        my_stack[int(i[-1]) - 1].extendleft(val[::-1])

    ret = [i.popleft() for i in my_stack]
    return "".join(ret)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = get_input(DAY, YEAR)

    test_solutions = solve(TEST_DATA)
    assert test_solutions[0] == "CMZ"
    assert test_solutions[1] == "MCD"

    solutions = solve(puzzle_input)
    assert solutions[0] == "VQZNJMWTR"
    assert solutions[1] == "NLCDCLVMQ"

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
