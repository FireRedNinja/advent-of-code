import pathlib
import sys
from pdb import set_trace

import numpy as np


def parse(puzzle_input):
    """Parse input"""
    draws, *boards = [section.split("\n") for section in puzzle_input.split("\n\n")]

    draws = [int(i) for i in draws[0].split(",")]
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            boards[i][j] = [int(k) for k in row.split()]
    return (draws, boards)


def part1(data):
    """Solve part 1"""
    draws, boards = data
    boards = np.array(boards)
    markers = np.zeros_like(boards)

    winning_board_index = None
    winning_draw = None

    for draw in draws:
        marker_locations = np.where(boards == draw)
        markers[marker_locations] = 1

        # for each board
        for i in range(markers.shape[0]):
            # for each row
            for j in range(markers.shape[1]):
                if np.all([markers[i, j, :], np.ones(markers.shape[1])]):
                    winning_board_index = i
                    break

            if winning_board_index is not None:
                break

            # for each column
            for j in range(markers.shape[2]):
                if np.all([markers[i, :, j], np.ones(markers.shape[2])]):
                    winning_board_index = i
                    break

            if winning_board_index is not None:
                break

        if winning_board_index is not None:
            winning_draw = draw
            break

    unmarked_numbers = np.where(markers[winning_board_index] == 0)
    unmarked_sum = sum(boards[winning_board_index][unmarked_numbers])

    return f"{unmarked_sum} * {winning_draw} = {unmarked_sum * winning_draw}"


def part2(data):
    """Solve part 2"""
    draws, boards = data
    boards = np.array(boards)
    markers = np.zeros_like(boards)

    winning_board = None
    winning_markers = None
    winning_board_index = []
    winning_draw = None

    for draw in draws:
        marker_locations = np.where(boards == draw)
        markers[marker_locations] = 1
        winning_board_index = []

        # for each board
        for i in range(markers.shape[0]):
            # for each row
            for j in range(markers.shape[1]):
                if np.all([markers[i, j, :], np.ones(markers.shape[1])]):
                    winning_board_index.append(i)
                    winning_board = boards[i]
                    winning_markers = markers[i]
                    break

            if len(winning_board_index) > 0:
                continue

            # for each column
            for j in range(markers.shape[2]):
                if np.all([markers[i, :, j], np.ones(markers.shape[2])]):
                    winning_board_index.append(i)
                    winning_board = boards[i]
                    winning_markers = markers[i]
                    break

            if len(winning_board_index) > 0:
                winning_draw = draw
                continue

        boards = np.delete(boards, winning_board_index, axis=0)
        markers = np.delete(markers, winning_board_index, axis=0)

    unmarked_numbers = np.where(winning_markers == 0)
    unmarked_sum = sum(winning_board[unmarked_numbers])

    return f"{unmarked_sum} * {winning_draw} = {unmarked_sum * winning_draw}"


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
        print("\nSolutions:")
        print(f"\tPart 1: {solutions[0]}\n\tPart 2: {solutions[1]}")
