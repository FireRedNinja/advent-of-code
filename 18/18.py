import pathlib
import sys
from pdb import set_trace as st
from collections import deque
import math
import json

def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split('\n')]

def set_left(val, data):
    for i in range(len(data)-1, -1, -1):
        if isinstance(data[i], int):
            return True, val + data[i]
        else:
            return set_left(val, data[i])
    return False, None

def set_right(val, data):
    for i in data:
        if isinstance(i, int):
            return True, val + i
        else:
            return set_right(val, i)
    return False, None

def explode(depth: int, data: list):
    """Explode the data"""
    depth += 1

    if all(isinstance(item, int) for item in data) and depth > 4:
        return True, data, (False, data[0]), (False, data[1]), False

    exploded = False
    left_set = False
    left_val = None
    right_set = False
    right_val = None
    pair_set = False

    for i in range(len(data)):
        if isinstance(data[i], list):
            exploded, pair, (left_set, left_val), (right_set, right_val), pair_set = explode(depth, data[i])
            data[i] = pair

            if exploded:
                new_right = None

                if not left_set:
                    left_set, new_left = set_left(left_val, data[:i])   

                if not right_set and i+1 < len(data):
                    right_set, new_right = set_right(right_val, data[i+1:])

                if not pair_set:
                    if left_set:
                        data = [new_left]
                    else:
                        data = [0]
                    
                    if right_set:
                        data.append(new_right)
                    else:
                        data.append(0)
                    
                    pair_set = True

                return exploded, data, (left_set, left_val), (right_set, right_val), pair_set
    
    return exploded, data, (left_set, left_val), (right_set, right_val), pair_set

def split(left, right, digit):
    digit = int(digit)

    replaced = f'[{math.floor(digit/2)},{math.ceil(digit/2)}]'

    return left + replaced + right
    

def part1(data):
    """Solve part 1"""
    snailfish = None

    first = True
    for line in data:
        line = json.loads(line)
        snailfish = line if snailfish is None else [snailfish, line]

        if first:
            first = False
            continue

        exploded = False
        split = False

        while True:
            exploded, snailfish, left, right, split = explode(0, snailfish)

            if not exploded and not split:
                break
        # while not exploded and not split:
        

    return f'Not implemented'


def part2(data):
    """Solve part 2"""

    return f'Not implemented'


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    path = "./18/18.txt"
    print(f"Input Data: {path}")
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print('\nSolutions:')
    print(f'\tPart 1: {solutions[0]}\n\tPart 2: {solutions[1]}')
