from collections import defaultdict, deque

from utils import get_input

DAY = "4"
YEAR = "2023"


def parse(puzzle_input: str):
    """Parse input"""
    return [
        [
            int(line.split(":")[0].split()[1]),
            [
                [int(number) for number in lists.strip().split()]
                for lists in line.split(":")[1].split("|")
            ],
        ]
        for line in puzzle_input.strip().splitlines()
    ]


def part1(data):
    """Solve part 1"""
    total_points = []
    for card in data:
        winning_numbers = set(card[1][0])
        my_numbers = set(card[1][1])

        matching = my_numbers.intersection(winning_numbers)

        points = 0
        for i in matching:
            if points == 0:
                points = 1
            else:
                points *= 2

        total_points.append(points)

    return sum(total_points)


def part2(data):
    """Solve part 2"""
    total_scratchcards = 0
    cards = defaultdict(int)
    for card in data:
        card_id = card[0]
        cards[card_id] += 1

        winning_numbers = set(card[1][0])
        my_numbers = set(card[1][1])

        matching = my_numbers.intersection(winning_numbers)

        for i in range(card_id + 1, card_id + 1 + len(matching)):
            cards[i] += cards[card_id]

        total_scratchcards += cards[card_id]

    return total_scratchcards


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 13
    assert test_solutions[1] == 30

    solutions = solve(puzzle_input)
    assert solutions[0] == 32609
    assert solutions[1] == 14624680

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
