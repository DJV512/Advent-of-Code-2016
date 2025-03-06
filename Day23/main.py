# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from collections import defaultdict
from copy import deepcopy


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1 = part1(deepcopy(data))
    part1_time = time.time()
    answer2 = part2(deepcopy(data))
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

    rules = []

    for line in data:
        parts = line.strip().split()
        if len(parts) == 2:
            rules.append([parts[0], parts[1], "N/A"])
        else:
            rules.append([parts[0], parts[1], parts[2]])

    return rules


def part1(data):
    i = 0
    registers = defaultdict(int)
    registers["a"] = 7
    while 0 <= i < len(data):

        current_rule_i, current_rule_f, current_rule_s = data[i]

        if current_rule_i == "cpy":
            if current_rule_s in ["a", "b", "c", "d"]:
                try:
                    value = int(current_rule_f)
                    registers[current_rule_s] = value
                except ValueError:
                    registers[current_rule_s] = registers[current_rule_f]
        elif current_rule_i == "inc":
            registers[current_rule_f] += 1
        elif current_rule_i == "dec":
            registers[current_rule_f] -= 1
        elif current_rule_i == "jnz":
            try:
                value = int(current_rule_f)
                if value != 0:
                    if current_rule_s in ["a", "b", "c", "d"]:
                        i += registers[current_rule_s]
                    else:
                        i += int(current_rule_s)
                    continue
            except ValueError:
                if registers[current_rule_f] != 0:
                    if current_rule_s in ["a", "b", "c", "d"]:
                        i += registers[current_rule_s]
                    else:
                        i += int(current_rule_s)
                    continue
        elif current_rule_i == "tgl":
            value = int(registers[current_rule_f])
            location_to_change = i + value
            if 0 <= location_to_change < len(data):
                if data[location_to_change][0] == "inc":
                    data[location_to_change][0] = "dec"
                elif data[location_to_change][0] == "dec":
                    data[location_to_change][0] = "inc"
                elif data[location_to_change][0] == "jnz":
                    data[location_to_change][0] = "cpy"
                elif data[location_to_change][0] == "cpy":
                    data[location_to_change][0] = "jnz"
                elif data[location_to_change][0] == "tgl":
                    data[location_to_change][0] = "inc"
                
        i += 1

    return registers["a"]


def part2(data):
    
    # In my efforts to fix my part 1 code, which initially had a stupid bug in the tgl if statement, 
    # I realized that the first part of the input ended up with a = 5040, which is 7!. When I got my
    # code running, I noticed that the final answer was approximately 7000 higher than that. So for
    # part 2, I made an educated guess that the part two answer might be just 12! plus the same
    # ~7000ish number. And it was! No code needed! :)

    return None


if __name__ == "__main__":
    main()