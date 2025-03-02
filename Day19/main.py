FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

import time
import utils
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
    sample_data = 5
    data = 3001330
    return data


def part1(data):
    elves = [i for i in range(1, data+1)]
    while len(elves) > 1:
        if len(elves) % 2 == 0:
            elves = [i for x, i in enumerate(elves) if x%2 == 0]
        else:
            elves = [i for x, i in enumerate(elves) if x%2 == 0][1:]

    return elves[0]


def part2(data):
    # Found this code by aceshades here:
    # https://www.reddit.com/r/adventofcode/comments/5j4lp1/2016_day_19_solutions/
    # Still not sure how it works, but I couldn't figure out a way to do it on my own
    # without it taking forever.

    left = deque()
    right = deque()
    for i in range(1, data+1):
        if i < (data // 2) + 1:
            left.append(i)
        else:
            right.appendleft(i)

    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()

        # rotate
        right.appendleft(left.popleft())
        left.append(right.pop())

    return left[0] or right[0]


if __name__ == "__main__":
    main()