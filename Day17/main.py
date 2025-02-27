FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

import time
import utils
from hashlib import md5
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
    # sample_data = "hijkl"
    # sample_data = "ihgpwlah"
    # sample_data = "kglvqrro"
    # sample_data = "ulqzkmiv"
    data = "hhhxzeay"
     
    return data


def check_doors(string):
    hash = md5(string.encode()).hexdigest()
    open = ["b", "c", "d", "e", "f"]
    return [True if hash[0] in open else False, True if hash[1] in open else False, True if hash[2] in open else False, True if hash[3] in open else False]


def part1(data):
    position = (0,0)
    stack = deque()
    stack.append((position, ""))
    while stack:
        position, directions = stack.popleft()

        if position == (3,3):
            return directions
        
        possibles = check_doors(data+directions)

        for i, possibility in enumerate(possibles):
            if possibility:
                if i == 0:
                    next_position = (position[0]-1, position[1])
                    if next_position[0] >= 0:
                        stack.append((next_position, directions+"U"))
                elif i == 1:
                    next_position = (position[0]+1, position[1])
                    if next_position[0] <= 3:
                        stack.append((next_position, directions+"D"))
                elif i == 2:
                    next_position = (position[0], position[1]-1)
                    if next_position[1] >= 0:
                        stack.append((next_position, directions+"L"))
                elif i == 3:
                    next_position = (position[0], position[1]+1)
                    if next_position[1] <= 3:
                        stack.append((next_position, directions+"R"))

    return "No solution"


def part2(data):
    position = (0,0)
    stack = deque()
    stack.append((position, ""))
    longest_path = 0
    while stack:
        position, directions = stack.popleft()

        if position == (3,3):
            if len(directions) > longest_path:
                longest_path = len(directions)
            continue
        
        possibles = check_doors(data+directions)

        for i, possibility in enumerate(possibles):
            if possibility:
                if i == 0:
                    next_position = (position[0]-1, position[1])
                    if next_position[0] >= 0:
                        stack.append((next_position, directions+"U"))
                elif i == 1:
                    next_position = (position[0]+1, position[1])
                    if next_position[0] <= 3:
                        stack.append((next_position, directions+"D"))
                elif i == 2:
                    next_position = (position[0], position[1]-1)
                    if next_position[1] >= 0:
                        stack.append((next_position, directions+"L"))
                elif i == 3:
                    next_position = (position[0], position[1]+1)
                    if next_position[1] <= 3:
                        stack.append((next_position, directions+"R"))

    return longest_path


if __name__ == "__main__":
    main()