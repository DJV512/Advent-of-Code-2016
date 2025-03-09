# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from collections import defaultdict


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

    rules = []

    for line in data:
        parts = line.strip().split()
        if len(parts) == 2:
            rules.append([parts[0], parts[1], "N/A"])
        else:
            rules.append([parts[0], parts[1], parts[2]])

    return rules


def part1(data):
    
    for initial_value in range(1000):
        output = []
        i = 0
        registers = defaultdict(int)
        registers["a"] = initial_value

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
            elif current_rule_i == "out":
                if len(output) == 0:
                    output.append(registers["b"])
                else:
                    if registers["b"] == output[-1]:
                        break
                    else:
                        output.append(registers["b"])

                if len(output) > 50:
                    for i in range(len(output), 0, 2):
                        if output[i] != 0:
                            break
                    for i in range(len(output), 1, 2):
                        if output[i] != 1:
                            break
                    return initial_value
            i += 1

    return "None found"



def part2(data):
    return None


if __name__ == "__main__":
    main()