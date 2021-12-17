import pathlib
import sys
from pdb import set_trace as st
from collections import deque
from functools import reduce


def parse(puzzle_input):
    """Parse input"""
    h = puzzle_input.split('\n')[0]
    return (bin(int(h, 16))[2:]).zfill(len(h) * 4)

def pop_left(queue, n):
    """Pop the leftmost element"""
    return ''.join(deque(queue.popleft() for _ in range(n)))

def type_id(type_id, values):
    match type_id:
        case 0:
            return sum(values)
        case 1:
            return reduce(lambda x, y: x * y, values)
        case 2:
            return min(values)
        case 3:
            return max(values)
        case 5:
            return 1 if values[0] > values[1] else 0
        case 6:
            return 1 if values[0] < values[1] else 0
        case 7:
            return 1 if values[0] == values[1] else 0


def parse_packet(packet):
    """Parse a packet"""
    packet_version = int(pop_left(packet, 3), 2)
    packet_type_id = int(pop_left(packet, 3), 2)
    literal_val = None
    values = []


    if packet_type_id == 4:
        num = ''
        while True:
            last_group = int(pop_left(packet, 1)) == 0
            num += pop_left(packet, 4)
            if last_group:
                break
        literal_val = int(num, 2)

    else:
        length_type_id = int(pop_left(packet, 1))
        length = None

        if length_type_id == 0:
            length = 15
            total_length = int(pop_left(packet, length), 2)

            sub_packets = deque(pop_left(packet, total_length))

            while len(sub_packets) > 0:
                sub_packet_version, value, sub_packets = parse_packet(sub_packets)
                packet_version += sub_packet_version
                values.append(value)

        else:
            length = 11
            number_of_sub_packets = int(pop_left(packet, length), 2)

            for _ in range(number_of_sub_packets):
                sub_packet_version, value, packet = parse_packet(packet)
                packet_version += sub_packet_version
                values.append(value)

    value = literal_val
    if value is None:
        value = type_id(packet_type_id, values)

    return packet_version, value, packet


def part1(data):
    """Solve part 1"""
    data = deque(data)
    packet_version, *_ = parse_packet(data)
    return f'Version: {packet_version}'


def part2(data):
    """Solve part 2"""
    data = deque(data)
    _, value, _ = parse_packet(data)
    return f'Value: {value}'


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
