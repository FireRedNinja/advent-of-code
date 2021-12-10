import pathlib
import sys
from collections import deque, Counter


def parse(puzzle_input):
    """Parse input"""
    return [list(line) for line in puzzle_input.split('\n')]


def part1(data):
    """Solve part 1"""
    syntax_structure = {
        '(': {
            'close': ')',
            'score': 3
        },
        '[': {
            'close': ']',
            'score': 57
        },
        '{': {
            'close': '}',
            'score': 1197
        },
        '<': {
            'close': '>',
            'score': 25137
        }
    }

    illegal_chars = []
    for line in data:
        syntax = deque()
        for char in line:
            if char in ')]}>':
                if char == syntax_structure[syntax[-1]]['close']:
                    syntax.pop()
                else:
                    illegal_chars.append(char)
                    break
            else:
                syntax.append(char)

    score = 0
    for key, val in Counter(illegal_chars).items():
        score += val * syntax_structure[key]['score']

    return f'Score: {score}'


def part2(data):
    """Solve part 2"""
    syntax_structure = {
        '(': {
            'close': ')',
            'value': 1
        },
        '[': {
            'close': ']',
            'value': 2
        },
        '{': {
            'close': '}',
            'value': 3
        },
        '<': {
            'close': '>',
            'value': 4
        }
    }

    incomplete_chars = []
    for line in data:
        syntax = deque()
        for char in line:
            if char in ')]}>':
                if char == syntax_structure[syntax[-1]]['close']:
                    syntax.pop()
                else:
                    syntax.clear()
                    break
            else:
                syntax.append(char)

        syntax.reverse()
        if len(syntax) > 0:
            incomplete_chars.append(syntax)

    scores = []
    for line in incomplete_chars:
        score = 0
        for char in line:
            score = (score * 5) + syntax_structure[char]['value']
        scores.append(score)

    scores.sort()
    return f'Score: {scores[(len(scores)-1)//2]}'


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
