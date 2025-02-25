# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
import re
from collections import deque

def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1 = part1(data)
    part1_time = time.time()
    answer2 = part2(data)
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
        data = f.readline()
    
    pattern = r"(\(\d+x\d+\))"
    parts = re.split(pattern, data.strip())
    for part in parts.copy():
        if part == "":
            parts.remove(part)
    return parts


def part1(parts):
    total = 0
    repeat = False
    for part in parts:
        if part[0] != "(" and not repeat:
            total += len(part)
        elif part[0] == "(" and not repeat:
            characters, times = part[1:-1].split("x")
            repeat = True
        elif repeat:
            length = len(part)
            if length >= int(characters):
                total += int(characters) * int(times) + (length-int(characters))
                repeat = False
            if length < int(characters):
                total += length * int(times)
                characters = int(characters) - length

    return total


def part2(parts):
    total = 0
    current = deque()
    for part in parts:
        if part[0] != "(" and len(current) == 0:
            total += len(part)
        elif part[0] != "(" and len(current) > 0:
            part_length = len(part)
            keep_going = True
            while keep_going:
                characters, times = current.popleft()
                if part_length > characters:
                    total += characters*times
                    part_length -= characters
                    if len(current) == 0:
                        total += part_length
                        keep_going = False
                elif part_length == characters:
                    total += characters*times
                    part_length -= characters
                    keep_going = False
                else:
                    total += part_length * times
                    current.appendleft((characters-part_length, times))
                    keep_going = False
        elif part[0] == "(":
            characters, times = part[1:-1].split("x")
            if len(current) == 0:
                current.append((int(characters), int(times)))
            else:
                part_length = len(part)
                new_current = deque()
                for i, (prev_char, prev_times) in enumerate(current):
                    if i == 0:
                        new_current.append((int(characters), int(times)*prev_times))
                        if prev_char-int(characters)-part_length >0:
                            new_current.append((prev_char-int(characters)-part_length, prev_times))
                    else:
                        new_current.append((prev_char, prev_times))
                current = new_current
    return total


if __name__ == "__main__":
    main()