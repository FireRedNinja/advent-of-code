from utils import get_input

DAY = "10"
YEAR = "2022"


def parse(puzzle_input: str):
    """Parse input"""
    return [line.split() for line in puzzle_input.strip().splitlines()]


def part1(data):
    """Solve part 1"""
    X = 1
    cycle = 0
    cycles = [20, 60, 100, 140, 180, 220]
    signal_strength = 0


    for op in data:
        cycle += 1

        if cycle in cycles:
            signal_strength += X * cycle

        if op[0] == "addx":
            cycle += 1

            if cycle in cycles:
                signal_strength += X * cycle

            X += int(op[1])

    return signal_strength


def part2(data):
    """Solve part 2"""

    X = 1
    cycle = 0
    cycles = [40, 80, 120, 160, 200, 240]

    print_str = "\n"
    crt = []
    line_counter = -1


    for op in data:
        cycle += 1
        line_counter += 1
        
        if line_counter in [X-1,X, X+1]:
            print_str += "#"
        else:
            print_str += "."
        
        if line_counter == 39:
            print_str += "\n"
            crt.append(print_str)
            print_str = ""
            line_counter = -1
        

        if op[0] == "addx":
            cycle += 1
            line_counter += 1
            
            if line_counter in [X-1,X, X+1]:
                print_str += "#"
            else:
                print_str += "."

            if line_counter == 39:
                print_str += "\n"
                crt.append(print_str)
                print_str = ""
                line_counter = -1

            X += int(op[1])

    crt = "".join(crt)
    return crt


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 13140
    assert test_solutions[1] == "".join([
        "\n",
        "##..##..##..##..##..##..##..##..##..##..\n",
        "###...###...###...###...###...###...###.\n",
        "####....####....####....####....####....\n",
        "#####.....#####.....#####.....#####.....\n",
        "######......######......######......####\n",
        "#######.......#######.......#######.....\n",
    ])

    solutions = solve(puzzle_input)
    assert solutions[0] == 11960
    assert solutions[1] == "".join([
        "\n",
        "####...##..##..####.###...##..#....#..#.\n",
        "#.......#.#..#.#....#..#.#..#.#....#..#.\n",
        "###.....#.#....###..#..#.#....#....####.\n",
        "#.......#.#....#....###..#.##.#....#..#.\n",
        "#....#..#.#..#.#....#....#..#.#....#..#.\n",
        "####..##...##..#....#.....###.####.#..#.\n",
    ])

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
