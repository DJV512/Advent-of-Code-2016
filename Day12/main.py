# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from collections import defaultdict, namedtuple


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

    Rule = namedtuple("Rule", ["i", "f", "s"])

    rules = []

    for line in data:
        parts = line.strip().split()
        if len(parts) == 2:
            rules.append(Rule(parts[0], parts[1], "N/A"))
        else:
            rules.append(Rule(parts[0], parts[1], parts[2]))


    return rules


def part1(data):
    i = 0
    registers = defaultdict(int)
    while 0 <= i < len(data):
        current_rule = data[i]

        if current_rule.i == "cpy":
            try:
                value = int(current_rule.f)
                registers[current_rule.s] = value
            except ValueError:
                registers[current_rule.s] = registers[current_rule.f]
        elif current_rule.i == "inc":
            registers[current_rule.f] += 1
        elif current_rule.i == "dec":
            registers[current_rule.f] -= 1
        elif current_rule.i == "jnz":
            try:
                value = int(current_rule.f)
                if value != 0:
                    i += int(current_rule.s)
                    continue
            except ValueError:
                if registers[current_rule.f] != 0:
                    i += int(current_rule.s)
                    continue
        
        i += 1

    return registers["a"]


def part2(data):
    i = 0
    registers = defaultdict(int)
    registers["c"] = 1
    while 0 <= i < len(data):
        current_rule = data[i]

        if current_rule.i == "cpy":
            try:
                value = int(current_rule.f)
                registers[current_rule.s] = value
            except ValueError:
                registers[current_rule.s] = registers[current_rule.f]
        elif current_rule.i == "inc":
            registers[current_rule.f] += 1
        elif current_rule.i == "dec":
            registers[current_rule.f] -= 1
        elif current_rule.i == "jnz":
            try:
                value = int(current_rule.f)
                if value != 0:
                    i += int(current_rule.s)
                    continue
            except ValueError:
                if registers[current_rule.f] != 0:
                    i += int(current_rule.s)
                    continue
        
        i += 1

    return registers["a"]


if __name__ == "__main__":
    main()