from utils import get_input

DAY = "7"
YEAR = "2022"


class Node:
    def __init__(self, name: str, parent=None):
        self.name = name
        self.size = None
        self.parent = parent
        self.children = {}


def parse(puzzle_input: str):
    """Parse input"""
    dir_tree = None
    curr_node = None
    data = [line for line in puzzle_input.strip().splitlines()]
    for line in puzzle_input.strip().splitlines():
        if line.startswith("$ cd"):
            name = line.split(" ")[-1]
            if dir_tree is None:
                dir_tree = Node(name)
                curr_node = dir_tree
            elif name == "..":
                curr_node = curr_node.parent
            else:
                curr_node = curr_node.children[name]
        elif line.startswith("$ ls"):
            continue
        else:
            line_data = line.split(" ")
            type = line_data[0]
            name = line_data[-1]
            if type == "dir":
                curr_node.children[name] = Node(name, curr_node)
            else:
                curr_node.children[name] = Node(name, curr_node)
                curr_node.children[name].size = int(type)
    return dir_tree


def add_sizes(node):
    count = 0
    if len(node.children) == 0:
        return node.size

    for child in node.children.values():
        if len(child.children) > 0:
            add_sizes(child)

    count += sum([child.size for child in node.children.values()])

    node.size = count
    return node


def part1(data):
    """Solve part 1"""
    dirs = get_dirs(data)
    return sum([x.size for x in filter(lambda x: x.size <= 100000, dirs)])


def get_dirs(node):
    dirs = []

    if len(node.children) == 0:
        return []

    for child in node.children.values():
        dirs += get_dirs(child)

    dirs += [node]
    return dirs


def part2(data):
    """Solve part 2"""
    space_unused = 70000000 - data.size
    space_to_remove = 30000000 - space_unused
    dirs = get_dirs(data)

    remove_dir_size = None
    for dir in dirs:
        if dir.size > space_to_remove:
            if remove_dir_size is None:
                remove_dir_size = dir.size
            elif dir.size < remove_dir_size:
                remove_dir_size = dir.size
    return remove_dir_size


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    data = add_sizes(data)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 95437
    assert test_solutions[1] == 24933642

    solutions = solve(puzzle_input)
    assert solutions[0] == 1491614
    assert solutions[1] == 6400111

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
