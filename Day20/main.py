# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1, forbidden = part1(data)
    part1_time = time.time()
    answer2 = part2(forbidden)
    part2_time = time.time()

    print("---------------------------------------------------")
    print(f"Part 1 Answer: {answer1}")
    print()
    print(f"Part 2 Answer: {answer2}")
    print()
    print(f"Data Parse Execution Time: {1000*(parse_time - start_time)} ms")
    print(f"Part 1 Execution Time:     {1000*(part1_time - parse_time)} ms")
    print(f"Part 2 Execution Time:     {1000*(part2_time - part1_time)} ms")
    print(f"Total Execution Time:      {1000*(part2_time - start_time)} ms")
    print("---------------------------------------------------")


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()

    data = [tuple(map(int, (line.strip().split("-")))) for line in data]

    return data


def part1(data):
    forbidden = set()
    for low, high in sorted(data):
        new = True
        for range_low, range_high in forbidden.copy():
            if range_low <= low <= range_high:
                if high <= range_high:
                    new = False
                else:
                    forbidden.remove((range_low, range_high))
                    forbidden.add((range_low, high))
                    new = False

            if range_low <= high <= range_high:
                if low > range_low:
                    new = False
                else:
                    forbidden.remove((range_low, range_high))
                    forbidden.add((low, range_high))
                    new = False

            if low <= range_low and high >= range_high:
                forbidden.remove((range_low, range_high))
                forbidden.add((low, high))
                new = False

        if new:
            forbidden.add((low, high))
        
    forbidden = sorted(forbidden)
    changes = True
    while changes:
        changes = False
        new_forbidden = []
        skip = False
        for i, (low, high) in enumerate(forbidden):
            if skip:
                skip = False
                continue

            if i == len(forbidden)-1:
                new_forbidden.append((low, high))
                continue

            if high == forbidden[i+1][0] - 1:
                new_forbidden.append((low, forbidden[i+1][1]))
                changes = True
                skip = True
            elif high < forbidden[i+1][0]:
                new_forbidden.append((low, high))
            else:
                new_forbidden.append((low, forbidden[i+1][1]))
                changes = True
                skip = True
    
        forbidden = new_forbidden
    
    return forbidden[0][1] + 1, forbidden


def part2(forbidden):

    total_ips = 2**32
    for low, high in forbidden:
        forbidden_ips = high-low+1
        total_ips -= forbidden_ips
    return total_ips


if __name__ == "__main__":
    main()