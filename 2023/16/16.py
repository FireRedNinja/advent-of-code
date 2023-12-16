from utils import get_input

DAY = "16"
YEAR = "2023"


def parse(puzzle_input: str):
    """Parse input"""
    return [list(line) for line in puzzle_input.strip().splitlines()]


# (row, col)
DIRECTIONS = {"l": (0, -1), "r": (0, 1), "u": (-1, 0), "d": (1, 0)}


def move_beam(beam, data):
    dir = beam[2]
    new_beams = []
    dirs = []
    match data[beam[0]][beam[1]]:
        case "/":
            if dir == "d":
                dirs.append("l")
            elif dir == "r":
                dirs.append("u")
            elif dir == "l":
                dirs.append("d")
            else:
                dirs.append("r")
        case "\\":
            if dir == "d":
                dirs.append("r")
            elif dir == "r":
                dirs.append("d")
            elif dir == "l":
                dirs.append("u")
            else:
                dirs.append("l")
        case "-":
            if dir == "u" or dir == "d":
                dirs.append("l")
                dirs.append("r")
            else:
                dirs.append(dir)
        case "|":
            if dir == "l" or dir == "r":
                dirs.append("u")
                dirs.append("d")
            else:
                dirs.append(dir)
        case other:
            dirs.append(dir)

    for d in dirs:
        new_beam = (beam[0] + DIRECTIONS[d][0], beam[1] + DIRECTIONS[d][1], d)

        if new_beam[0] in range(len(data)) and new_beam[1] in range(len(data[1])):
            new_beams.append(new_beam)
    return new_beams


def part1(data):
    """Solve part 1"""
    # visited without directions
    energised = set()
    # visited with directions
    visited = set()
    beams = []
    energised.add((0, 0))
    beams.append((0, 0, "r"))
    visited.add((0, 0, "r"))
    while len(beams) > 0:
        beam = beams.pop()
        new_beams = move_beam(beam, data)

        for new_beam in new_beams:
            if new_beam not in visited:
                energised.add((new_beam[0], new_beam[1]))
                beams.append(new_beam)
                visited.add(new_beam)

    ans = len(energised)
    return ans


def part2(data):
    """Solve part 2"""
    max_energised = 0

    edges = []
    for i in range(len(data)):
        edges.append((i, 0, "r"))
        edges.append((1, len(data[0]) - 1, "l"))
    for i in range(len(data[0])):
        edges.append((0, i, "d"))
        edges.append((len(data) - 1, i, "u"))

    for edge in edges:
        # visited without directions
        energised = set()
        # visited with directions
        visited = set()
        beams = []
        energised.add((edge[0], edge[1]))
        beams.append(edge)
        visited.add(edge)

        while len(beams) > 0:
            beam = beams.pop()
            new_beams = move_beam(beam, data)

            for new_beam in new_beams:
                if new_beam not in visited:
                    energised.add((new_beam[0], new_beam[1]))
                    beams.append(new_beam)
                    visited.add(new_beam)

        max_energised = max(max_energised, len(energised))
    return max_energised


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 46
    assert test_solutions[1] == 51

    solutions = solve(puzzle_input)
    assert solutions[0] == 7979
    assert solutions[1] == 8437

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
