from utils import get_input
from collections import defaultdict

DAY = "21"
YEAR = "2022"


def parse(puzzle_input: str):
    """Parse input"""
    data = {}
    for line in puzzle_input.strip().splitlines():
        name, *rest = line.split(" ")
        name = name.strip(":")
        data[name] = rest
    return data


def part1(data):
    """Solve part 1"""

    def evaluate(name: str) -> int:
        if len(data[name]) > 1:
            return eval(
                f"{evaluate(data[name][0])} {data[name][1]} {evaluate(data[name][2])}"
            )
        else:
            return int(data[name][0])

    root = evaluate("root")
    return int(root)


def get_path(data):
    path = ["humn"]
    while True:
        for i in data:
            if path[-1] in data[i]:
                if i == "root":
                    return path
                path.append(i)


def part2(data):
    """Solve part 2"""
    data["root"][1] = "="
    data["humn"][0] = None

    OPERATIONS = {
        "+": "-",
        "-": "+",
        "*": "/",
        "/": "*",
    }

    memo = defaultdict(None)

    # find path from l / r to humn
    path = get_path(data)

    def evaluate(name: str) -> int:
        if len(data[name]) > 1:
            val = eval(
                f"{int(evaluate(data[name][0]))} {data[name][1]} {evaluate(data[name][2])}"
            )
            memo[name] = val
            return val
        else:
            val = int(data[name][0])
            memo[name] = val
            return val

    # eval node without humn
    start_name = None
    if data["root"].index(path[-1]) == 0:
        start_name = data["root"][-1]
        memo[start_name] = evaluate(start_name)
        memo[data["root"][0]] = memo[start_name]
    else:
        start_name = data["root"][0]
        memo[start_name] = evaluate(start_name)
        memo[data["root"][1]] = memo[start_name]

    path.reverse()
    for p in path:
        operation = data[p]
        if len(operation) > 1:
            l, op, r = operation
            if l in path:
                memo[r] = evaluate(r)
                memo[l] = eval(f"{memo[p]} {OPERATIONS[op]} {memo[r]}")
            else:
                memo[l] = evaluate(l)
                if op == "/":
                    memo[r] = eval(f"{memo[l]} {op} {memo[p]}")
                elif op == "-":
                    memo[r] = eval(f"{memo[l]} {op} {memo[p]}")
                else:
                    memo[r] = eval(f"{memo[p]} {OPERATIONS[op]} {memo[l]}")

    return int(memo["humn"])


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 152
    assert test_solutions[1] == 301

    solutions = solve(puzzle_input)
    assert solutions[0] == 145167969204648
    assert solutions[1] == 3330805295850

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
