# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from collections import defaultdict

# TO_COMPARE = [2,5]
TO_COMPARE = [17, 61]

def main():
    start_time = time.time()

    who_has_what, what_goes_where = parse_data()
    parse_time = time.time()

    answer1, output = part1(who_has_what, what_goes_where)
    part1_time = time.time()
    answer2 = part2(output)
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
    who_has_what = {}
    for i in range(210):
        who_has_what[str(i)] = []
    what_goes_where = {}
    for line in data:
        parts = line.strip().split()
        if "value" in line:
            who_has_what[parts[5]].append(int(parts[1]))
        else:
            first = (parts[5] == "output")
            second = (parts[10] == "output")
            what_goes_where[parts[1]] = {
                "low": (("output" if first else "bot"), parts[6]),
                "high": (("output" if second else "bot"), parts[11]),
            }

    return who_has_what, what_goes_where


def part1(who_has_what, what_goes_where):
    output = {}
    keep_going = True
    while keep_going:
        keep_going = False
        for bot in who_has_what:
            if len(who_has_what[bot]) == 2:
                keep_going = True
                num1, num2 = who_has_what[bot]
                if num1 in TO_COMPARE and num2 in TO_COMPARE:
                    answer = bot
                low_num = min(num1, num2)
                high_num = max(num1, num2)
                low_dest, low_dest_num = what_goes_where[bot]["low"]
                high_dest, high_dest_num = what_goes_where[bot]["high"]
                if low_dest == "output":
                    output[low_dest_num] = low_num
                else:
                    who_has_what[low_dest_num].append(low_num)
                if high_dest == "output":
                    output[high_dest_num] = high_num
                else:
                    who_has_what[high_dest_num].append(high_num)

                who_has_what[bot] = []

    return answer, output


def part2(output):
    return output["0"]*output["1"]*output["2"]


if __name__ == "__main__":
    main()