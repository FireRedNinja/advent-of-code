import pathlib
import numpy as np

def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split('\n')]

def enhance_image(input_image, image_enhancement_algorithm):
    """Enhance the image"""
    output_image = np.zeros(input_image.shape)
    return output_image

def part1(data):
    """Solve part 1"""
    image_enhancement_algorithm = data[0]
    input_image = data[2:]
    input_image = np.array(list(map(list, input_image)))

    steps = 2
    for _ in range(steps):
        input_image = enhance_image(input_image, image_enhancement_algorithm)


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
    path = "20/20.txt"
    print(f"Input Data: {path}")
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print('\nSolutions:')
    print(f'\tPart 1: {solutions[0]}\n\tPart 2: {solutions[1]}')
