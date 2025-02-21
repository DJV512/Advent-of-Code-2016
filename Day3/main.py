# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time

RESET = "\033[0m"         # Resets all styles
BLACK = "\033[30;1m"      # Black text
RED = "\033[31;1m"        # Red text
GREEN = "\033[32;1m"      # Green text
YELLOW = "\033[33;1m"     # Yellow text
BLUE = "\033[34;1m"       # Blue text
MAGENTGA = "\033[35;1m"   # Magenta text
CYAN = "\033[36;1m"       # Cyan text
WHITE = "\033[37;1m"      # White text

BOLD = "\033[1m"          # Bold text
UNDERLINE = "\033[4m"     # Underlined text

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

    coords = []
    for line in data:
        s1, s2, s3 = line.split()
        coords.append((int(s1), int(s2), int(s3)))

    return coords


def part1(data):
    possible = 0
    for s1, s2, s3 in data:
        if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
            possible += 1

    return possible


def part2(data):
    possible = 0

    for i in range(2, len(data),3):
        if data[i-2][0] + data[i-1][0] > data[i][0] and data[i-2][0] + data[i][0] > data[i-1][0] and data[i-1][0] + data[i][0] > data[i-2][0]:
            possible += 1
        if data[i-2][1] + data[i-1][1] > data[i][1] and data[i-2][1] + data[i][1] > data[i-1][1] and data[i-1][1] + data[i][1] > data[i-2][1]:
            possible += 1
        if data[i-2][2] + data[i-1][2] > data[i][2] and data[i-2][2] + data[i][2] > data[i-1][2] and data[i-1][2] + data[i][2] > data[i-2][2]:
            possible += 1

    return possible


if __name__ == "__main__":
    main()