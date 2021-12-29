import pathlib
import sys
from pdb import set_trace as st
from collections import defaultdict, Counter


def parse(puzzle_input):
    """Parse input"""
    lines = [line for line in puzzle_input.split('\n')]
    template = lines[0]
    rules = defaultdict(str)
    for line in lines[2:]:
        rule, result = line.split(' -> ')
        rules[rule] = result
    
    return template, rules


def part1(data):
    """Solve part 1"""
    template, rules = data
    steps = 10

    for _ in range(steps):
        l = 0
        r = 2
        while r < len(template)+1:
            if template[l:r] in rules:
                template = template[:l+1] + rules[template[l:r]] + template[r-1:]
                l = r
                r += 2
            else:
                l += 1
                r += 1
    
    counts = Counter(template).most_common()
    return f'Most - Least common element: {counts[0][1] - counts[-1][1]}'


def part2(data):
    """Solve part 1"""
    template, rules = data
    steps = 40

    template_dict = defaultdict(int)

    for i in range(len(template)-1):
        template_dict[template[i:i+2]] += 1

    for _ in range(steps):
        new_template_dict = defaultdict(int)
        for pair in template_dict:
            if pair in rules:
                new_template_dict[pair[0] + rules[pair]] += template_dict[pair]
                new_template_dict[rules[pair] + pair[1]] += template_dict[pair]
                template_dict[pair] = 0
        template_dict = {**template_dict, **new_template_dict}
    

    unique_characters = set(list(''.join(template_dict.keys())))
    counts = defaultdict(int)
    for char in unique_characters:
        start_chars = 0
        end_chars = 0
        for pair in template_dict:
            if pair[0] == char:
                start_chars += template_dict[pair]
            if pair[1] == char:
                end_chars += template_dict[pair]
        
        counts[char] = max(end_chars, start_chars)
    
    values = sorted(counts.values())
    return f'Most - Least common element: {values[-1] - values[0]}'


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
