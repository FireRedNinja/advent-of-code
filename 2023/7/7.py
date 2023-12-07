from collections import Counter, defaultdict

from utils import get_input

DAY = "7"
YEAR = "2023"


def parse(puzzle_input: str):
    """Parse input"""
    return [
        (line.split(" ")[0], int(line.split(" ")[1]))
        for line in puzzle_input.strip().splitlines()
    ]


def part1(data):
    """Solve part 1"""
    card_ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    strengths = defaultdict(list)

    for line in data:
        hand, bid = line
        type = Counter(hand)
        m_c = type.most_common()
        if m_c[0][1] == 5:
            strengths["five"].append(line)
        elif m_c[0][1] == 4:
            strengths["four"].append(line)
        elif m_c[0][1] == 3:
            if m_c[1][1] == 2:
                strengths["full"].append(line)
            else:
                strengths["three"].append(line)
        elif m_c[0][1] == 2:
            if m_c[1][1] == 2:
                strengths["two"].append(line)
            else:
                strengths["one"].append(line)
        else:
            strengths["high"].append(line)

    order = ["high", "one", "two", "three", "full", "four", "five"]

    winnings = 0
    rank = 1
    for o in order:
        hands = strengths[o]
        if hands == []:
            continue
        hands.sort(key=lambda x: [card_ranks.index(i) for i in x[0]], reverse=True)

        for _, bid in hands:
            winnings += bid * rank
            rank += 1

    return winnings


def part2(data):
    """Solve part 2"""
    card_ranks = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    order = ["high", "one", "two", "three", "full", "four", "five"]
    strengths = defaultdict(list)

    for line in data:
        hand, bid = line
        counts = Counter(hand)
        joker_map = {
            1: {
                "high": "one",
                "one": "three",
                "two": "full",
                "three": "four",
                "full": "four",
                "four": "five",
            },
            2: {
                "high": "three",
                "one": "four",
                "three": "five",
                "full": "five",
            },
            3: {
                "high": "four",
                "one": "five",
            },
            4: {"high": "five"},
            5: {"five": "five"},
        }
        joker_counts = counts["J"]
        del counts["J"]

        m_c = counts.most_common()
        t = "high"
        if len(m_c) == 0:
            # 5 Js
            t = "five"
        elif m_c[0][1] == 5:
            t = "five"
        elif m_c[0][1] == 4:
            t = "four"
        elif m_c[0][1] == 3:
            # last 2 are J
            if len(m_c) == 1 or m_c[1][1] == 1:
                t = "three"
            else:
                t = "full"
        elif m_c[0][1] == 2:
            # last 3 are J
            if len(m_c) == 1 or m_c[1][1] == 1:
                t = "one"
            else:
                t = "two"
        else:
            t = "high"

        if joker_counts > 0:
            t = joker_map[joker_counts][t]
        strengths[t].append(line)

    winnings = 0
    rank = 1
    for o in order:
        hands = strengths[o]
        if hands == []:
            continue
        hands.sort(key=lambda x: [card_ranks.index(i) for i in x[0]], reverse=True)

        for _, bid in hands:
            winnings += bid * rank
            rank += 1

    return winnings


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 6440
    assert test_solutions[1] == 5905

    solutions = solve(puzzle_input)
    assert solutions[0] == 248217452
    assert solutions[1] == 245576185

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
