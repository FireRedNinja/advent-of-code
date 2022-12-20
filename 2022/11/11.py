from utils import get_input
from collections import defaultdict, deque
from functools import reduce
from copy import deepcopy

DAY = "11"
YEAR = "2022"


def parse(puzzle_input: str):
    """Parse input"""
    input = [line.splitlines() for line in puzzle_input.strip().split("\n\n")]
    data = defaultdict(dict)
    for i in input:
        monkey_no = int(i[0].split(" ")[1][:-1])

        items = deque([int(j.strip(",")) for j in i[1].split(" ")[4:]])

        operation = i[2].split(" ")
        op = operation[6]
        op_l = operation[5]
        op_r = operation[7]

        div_by = int(i[3].split(" ")[-1])
        throw_true = int(i[4].split(" ")[-1])
        throw_false = int(i[5].split(" ")[-1])

        data[monkey_no] = {
            "items": items,
            "operation": op,
            "operation_l": op_l,
            "operation_r": op_r,
            "div_by": div_by,
            "throw_true": throw_true,
            "throw_false": throw_false,
            "inspected": 0,
        }
    return data


def old_or_int(old, val):
    if val == "old":
        return old
    else:
        return int(val)


def performOp(old, op: str, op_l, op_r, modulo):
    l = old_or_int(old, op_l)
    r = old_or_int(old, op_r)

    res = None
    if op == "*":
        res = l * r
    elif op == "+":
        res = l + r
    else:
        res = l - r

    return res % modulo


def part1(data):
    """Solve part 1"""
    modulo = reduce(lambda x, y: x * y, [data[i]["div_by"] for i in data.keys()])

    for round in range(20):
        for monkey_no in range(len(data.keys())):
            monkey = data[monkey_no]
            items = monkey["items"]
            div_by = monkey["div_by"]
            throw_true = monkey["throw_true"]
            throw_false = monkey["throw_false"]
            op = monkey["operation"]
            op_l = monkey["operation_l"]
            op_r = monkey["operation_r"]

            while len(items) > 0:
                item = items.popleft()
                item = performOp(item, op, op_l, op_r, modulo)
                item //= 3

                if item % div_by == 0:
                    data[throw_true]["items"].append(item)
                else:
                    data[throw_false]["items"].append(item)

                monkey["inspected"] += 1

    monkey_business = [data[i]["inspected"] for i in data.keys()]
    monkey_business.sort()
    return reduce((lambda x, y: x * y), monkey_business[-2:])


def part2(data):
    """Solve part 2"""
    print("part2")

    modulo = reduce(lambda x, y: x * y, [data[i]["div_by"] for i in data.keys()])

    for round in range(10000):
        for monkey_no in range(len(data.keys())):
            monkey = data[monkey_no]
            items = monkey["items"]
            div_by = monkey["div_by"]
            throw_true = monkey["throw_true"]
            throw_false = monkey["throw_false"]
            op = monkey["operation"]
            op_l = monkey["operation_l"]
            op_r = monkey["operation_r"]

            while len(items) > 0:
                item = items.popleft()
                item = performOp(item, op, op_l, op_r, modulo)

                if item % div_by == 0:
                    data[throw_true]["items"].append(item)
                else:
                    data[throw_false]["items"].append(item)

                monkey["inspected"] += 1

    monkey_business = [data[i]["inspected"] for i in data.keys()]
    monkey_business.sort()
    return reduce((lambda x, y: x * y), monkey_business[-2:])


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    data2 = deepcopy(data)
    solution1 = part1(data)
    solution2 = part2(data2)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 10605
    assert test_solutions[1] == 2713310158

    solutions = solve(puzzle_input)
    assert solutions[0] == 110220
    assert solutions[1] == 19457438264

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
