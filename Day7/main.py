# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
import re


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
        data = f.readlines()

    items = []
    for line in data:
        pattern = r'\[(.*?)\]'
        parts = re.split(pattern, line.strip())
        outside = parts[::2]
        brackets = parts[1::2]
        items.append((outside, brackets))

    return items


def part1(data):
    total_tls = 0
    for outside, brackets in data:
        tls = True
        keep_going = True
        for string in brackets:
            for i, _ in enumerate(string[3:], start=3):
                if string[i] == string[i-3] and string[i-1] == string[i-2] and string[i] != string[i-1]:
                    tls = False
                    keep_going = False
                    break
                if not keep_going:
                    break

        if tls:
            keep_going = True
            for string in outside:
                for i, _ in enumerate(string[3:], start=3):
                    if string[i] == string[i-3] and string[i-1] == string[i-2] and string[i] != string[i-1]:
                        total_tls += 1
                        keep_going = False
                        break
                if not keep_going:
                    break
                        

    return total_tls


def part2(data):
    total_ssl = 0
    for outside, brackets in data:
        keep_going = True
        possibles = []
        for string in outside:
            for i, _ in enumerate(string[2:], start=2):
                if string[i] == string[i-2] and string[i] != string[i-1]:
                    new_string = string[i-2:i+1]
                    possibles.append(new_string)

        for string in brackets:
            for i, _ in enumerate(string[2:], start=2):
                if string[i] == string[i-2] and string[i] != string[i-1]:
                    new_string = string[i-1]+string[i]+string[i-1]
                    print(new_string)
                    if new_string in possibles:
                        total_ssl += 1
                        keep_going = False
                        break
            if not keep_going:
                break

    return total_ssl


if __name__ == "__main__":
    main()