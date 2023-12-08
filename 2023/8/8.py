from utils import get_input
from itertools import cycle
import re
from math import lcm

DAY = "8"
YEAR = "2023"


def parse(puzzle_input: str):
    """Parse input"""
    input = [
        line for line in puzzle_input.strip().splitlines()
    ]
    data = {
        "instructions": input[0]
    }

    input = input[2:]

    for line in input:
        [key, l, r] = re.findall(r"\w+", line)
        data[key] = (l, r)

    return data


def part1(data):
    """Solve part 1"""

    instructions = cycle(data["instructions"])
    curr_node = "AAA"
    steps = 0
    while curr_node != "ZZZ":
        next_node = next(instructions)
        if next_node == "R":
            curr_node = data[curr_node][1]
        else:
            curr_node = data[curr_node][0]
        steps += 1


    return steps


def part2(data):
    """Solve part 2"""

    instructions = cycle(data["instructions"])

    curr_node = list(filter(lambda x: x[-1] == "A", data.keys()))
    node_steps = [0 for i in curr_node]
    steps = 0

    while not all([i[-1] == "Z" for i in curr_node]):
        next_node = next(instructions)

        for n in range(len(curr_node)):
            if curr_node[n][-1] == "Z":
                continue

            if next_node == "R":
                curr_node[n] = data[curr_node[n]][1]
            else:
                curr_node[n] = data[curr_node[n]][0]
            
            if curr_node[n][-1] == "Z":
                if node_steps[n] == 0:
                    node_steps[n] = steps + 1
                continue
        steps += 1
    

    return lcm(*node_steps)



def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    # test_solutions = solve(test_input)
    # assert test_solutions[0] == 6
    # assert test_solutions[1] == 6

    solutions = solve(puzzle_input)
    assert solutions[0] == 17263
    assert solutions[1] == 14631604759649

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
