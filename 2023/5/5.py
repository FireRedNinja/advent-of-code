import re
from collections import defaultdict

from utils import get_input

DAY = "5"
YEAR = "2023"


def parse(puzzle_input: str):
    """Parse input"""
    data = [line for line in puzzle_input.strip().splitlines()]
    seed_data = defaultdict(list)
    seed_data["seeds"] = [int(i) for i in re.findall(r"\d+", data[0].split(":")[1])]

    title = None
    for line in data[1:]:
        if line == "":
            continue

        if line[0].isdigit():
            seed_data[title].append([int(i) for i in re.findall(r"\d+", line)])
            seed_data[title].sort(key=lambda x: x[1])
        else:
            title = line.split(" ")[0]

    return seed_data


# memo = defaultdict(dict)
order = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


def reduce_map(start: int, end: int):
    pass


# def build_intervals(data) -> dict[int]:
#     intervals = defaultdict(list)
#     for o in order:
#         stage = o.split("-")[-1]
#         intervals[stage] = [
#             (destination_range_start, destination_range_start + range_length - 1)
#             for [destination_range_start, _, range_length] in data[o]
#         ]
#         intervals[stage].sort(key=lambda x: x[0])
#     return intervals


def getLocationOfSeed(data: dict[list], seed_id: int) -> int:
    # seed_location[seed_id] = {}
    seed_location = defaultdict(dict)

    start_id = seed_id
    for i, map in enumerate(order):
        end = map.split("-")[-1]

        # if start_id in memo[map].keys():
        #     seed_location[end] = memo[map][start_id]
        #     start_id = seed_location[end]
        #     continue

        for [destination_range_start, source_range_start, range_length] in data[map]:
            if (
                start_id >= source_range_start
                and start_id < source_range_start + range_length
            ):
                seed_location[end] = destination_range_start + (
                    start_id - source_range_start
                )
                # memo[map][start_id] = seed_location[end]
                start_id = seed_location[end]
                break

        if seed_location[end] == {}:
            # memo[map][start_id] = start_id
            seed_location[end] = start_id

    return seed_location["location"]


def part1(data):
    """Solve part 1"""
    min_location = None
    for i in data["seeds"]:
        if min_location == None:
            min_location = getLocationOfSeed(data, i)
        else:
            min_location = min(min_location, getLocationOfSeed(data, i))

    return min_location


def part2(data):
    """Solve part 2"""
    min_location = None

    # for each seed interval
    # go through each stage
    # sort the source intervals
    # for each source interval
    # filter the seeds to source by creating intervals
    # transpose to destination
    # if seeds dont have a source keep same
    # get the minimum of the location

    for i in range(0, len(data["seeds"]), 2):
        seed_id_start = data["seeds"][i]
        seed_id_range = data["seeds"][i + 1]

        seed_intervals = []
        seed_intervals.append((seed_id_start, seed_id_start + seed_id_range - 1))

        for stage in order:
            filtered = []
            for seed_interval in seed_intervals:
                for [dst, src, rang] in data[stage]:
                    stage_interval = (src, src + rang - 1)
                    transpose = dst - src

                    # left seed_interval is outside stage_interval
                    if seed_interval[0] < stage_interval[0]:
                        # full seed_interval outside stage_interval
                        if seed_interval[1] < stage_interval[0]:
                            filtered.append(seed_interval)
                            seed_interval = None
                            break

                        # right seed_interval is outside stage_interval
                        if seed_interval[1] > stage_interval[1]:
                            filtered.append((seed_interval[0], stage_interval[0] - 1))
                            filtered.append(
                                (
                                    stage_interval[0] + transpose,
                                    stage_interval[1] + transpose,
                                )
                            )
                            seed_interval = (stage_interval[1] + 1, seed_interval[1])
                        # right seed_interval is inside stage_interval
                        else:
                            filtered.append((seed_interval[0], stage_interval[0] - 1))
                            filtered.append(
                                (
                                    stage_interval[0] + transpose,
                                    seed_interval[1] + transpose,
                                )
                            )
                            seed_interval = None
                            break
                    # left seed_interval is inside stage_interval
                    elif seed_interval[0] <= stage_interval[1]:
                        # full seed_interval inside stage_interval
                        if seed_interval[1] <= stage_interval[1]:
                            filtered.append(
                                (
                                    seed_interval[0] + transpose,
                                    seed_interval[1] + transpose,
                                )
                            )
                            seed_interval = None
                            break
                        # right seed_interval is outside stage_interval
                        else:
                            filtered.append(
                                (
                                    seed_interval[0] + transpose,
                                    stage_interval[1] + transpose,
                                )
                            )
                            seed_interval = (stage_interval[1] + 1, seed_interval[1])

                # full seed_interval is outside stage_interval
                if seed_interval != None:
                    filtered.append(seed_interval)
            seed_intervals = filtered

        if min_location == None:
            min_location = min([i[0] for i in seed_intervals])
        else:
            min_location = min(min_location, min([i[0] for i in seed_intervals]))

    return min_location


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input, test_input = get_input(DAY, YEAR)

    test_solutions = solve(test_input)
    assert test_solutions[0] == 35
    assert test_solutions[1] == 46

    solutions = solve(puzzle_input)
    assert solutions[0] == 551761867
    # assert solutions[1] ==

    print("\nSolutions:")
    print(
        f"""
    Part 1: {solutions[0]}
    Part 2: {solutions[1]}
        """
    )
