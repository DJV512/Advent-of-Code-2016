# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from collections import Counter


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1, one, two, three, four, five, six, seven, eight = part1(data)
    part1_time = time.time()
    answer2 = part2(one, two, three, four, five, six, seven, eight)
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

    return data


def part1(data):
    first = ""
    second = ""
    third = ""
    fourth = ""
    fifth = ""
    sixth = ""
    seventh = ""
    eighth = ""
    for line in data:
        line = line.strip()
        first += line[0]
        second += line[1]
        third += line[2]
        fourth += line[3]
        fifth += line[4]
        sixth += line[5]
        seventh += line[6]
        eighth += line[7]
    one = Counter(first)
    two = Counter(second)
    three = Counter(third)
    four = Counter(fourth)
    five = Counter(fifth)
    six = Counter(sixth)
    seven = Counter(seventh)
    eight = Counter(eighth)

    answer = max(one, key=one.get) + max(two, key=two.get) + max(three, key=three.get) + max(four, key=four.get) + max(five, key=five.get) + max(six, key=six.get) + max(seven, key=seven.get) + max(eight, key=eight.get)

    return answer, one, two, three, four, five, six, seven, eight


def part2(one, two, three, four, five, six, seven, eight):
    answer = min(one, key=one.get) + min(two, key=two.get) + min(three, key=three.get) + min(four, key=four.get) + min(five, key=five.get) + min(six, key=six.get) + min(seven, key=seven.get) + min(eight, key=eight.get)
    return answer


if __name__ == "__main__":
    main()