import pathlib
import pdb
import sys
import numpy as np
import pandas as pd


def parse(puzzle_input):
    """Parse input"""
    return [list(line) for line in puzzle_input.split('\n')]


def part1(data):
    """Solve part 1"""
    df = pd.DataFrame(data)

    gamma = ''.join([df[i].value_counts().idxmax() for i in range(12)])
    epsilon = ''.join([df[i].value_counts().idxmin() for i in range(12)])

    decimal = int(gamma, 2) * int(epsilon, 2)
    binary = bin(decimal)

    return f'Binary: {binary}, Decimal: {decimal}'


def part2(data):
    """Solve part 2"""
    df = pd.DataFrame(data)

    oxygen_generator_rating_df = df.copy()
    CO2_scrubber_rating_df = df.copy()
    for i in range(len(df.columns)):
        if len(oxygen_generator_rating_df) == 1:
            pass
        elif oxygen_generator_rating_df[i].value_counts().idxmax(
        ) == oxygen_generator_rating_df[i].value_counts().idxmin():
            oxygen_generator_rating_df = oxygen_generator_rating_df[
                oxygen_generator_rating_df[i] == '1']
        else:
            oxygen_generator_rating_df = oxygen_generator_rating_df[
                oxygen_generator_rating_df[i] ==
                oxygen_generator_rating_df[i].value_counts().idxmax()]

        if len(CO2_scrubber_rating_df) == 1:
            pass
        if CO2_scrubber_rating_df[i].value_counts().idxmax(
        ) == CO2_scrubber_rating_df[i].value_counts().idxmin():
            CO2_scrubber_rating_df = CO2_scrubber_rating_df[
                CO2_scrubber_rating_df[i] == '0']
        else:
            CO2_scrubber_rating_df = CO2_scrubber_rating_df[
                CO2_scrubber_rating_df[i] ==
                CO2_scrubber_rating_df[i].value_counts().idxmin()]


    oxygen_generator_rating = ''.join(oxygen_generator_rating_df.iloc[0])
    CO2_scrubber_rating = ''.join(CO2_scrubber_rating_df.iloc[0])

    decimal = int(oxygen_generator_rating, 2) * int(CO2_scrubber_rating, 2)
    binary = bin(decimal)

    return f'Binary: {binary}, Decimal: {decimal}'


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
