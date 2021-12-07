import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split(',')]


def part1(data):
    """Solve part 1"""
    least_fuel = None
    for i in range(0, max(data)):
        fuel = 0
        for j in data:
            fuel += abs(j - i)
            if least_fuel is not None and fuel > least_fuel:
                break
        if least_fuel is None or fuel < least_fuel:
            least_fuel = fuel
            
    return f'Least fuel: {least_fuel}'


def part2(data):
    """Solve part 2"""
    least_fuel = None
    for i in range(0, max(data)):
        fuel = 0
        for j in data:
            fuel += sum(range(abs(j - i)+1))
            if least_fuel is not None and fuel > least_fuel:
                break
        if least_fuel is None or fuel < least_fuel:
            least_fuel = fuel
            
    return f'Least fuel: {least_fuel}'


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"Input Data: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print('\nSolutions:')
        print(f'\tPart 1: {solutions[0]}\n\tPart 2: {solutions[1]}')
