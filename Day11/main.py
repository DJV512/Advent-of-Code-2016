FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

# I could not even begin to undestand how to code this, so I used code from bcongdon on reddit.
# That code is is main2.py (his original code) and main3.py (modified with my inputs).
# I cannot thank you enough bcongdon!


import time
import utils


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

    # return utils.grid_parse(data)

    return data


def part1(data):
    return None


def part2(data):
    return None


if __name__ == "__main__":
    main()