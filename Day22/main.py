# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
import re
import heapq
from copy import deepcopy
from itertools import count

def main():
    start_time = time.time()

    data, start = parse_data()
    parse_time = time.time()

    answer1 = part1(data)
    part1_time = time.time()
    answer2 = part2(data, start)
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

    nodes = {}
    start = (100,100)
    for i, line in enumerate(data):
        if i == 0 or i == 1:
            continue

        parts = line.strip().split()

        pattern = r"\d{1,2}"

        result = re.findall(pattern, parts[0])
        x=int(result[0])
        y=int(result[1])

        used = parts[2][:-1]
        available = parts[3][:-1]

        nodes[(y,x)] = [int(used), int(available)]
        if int(used) == 0:
            start = (y,x)

    return nodes, start


def part1(data):
    total = 0
    for node1 in data:
        for node2 in data:
            if node1 == node2:
                continue

            if data[node1][0] > 0 and data[node1][0] < data[node2][1]:
                total += 1
            
    return total


def distance(position, goal):
    manhattan = (abs(position[0] - goal[0]) + abs(position[1] - goal[1])) + (goal[0] + goal[1])

    if position[0] >= 11 and position[1] > 20: # while we're still below "the wall"
        penalty = (position[0] - 11) * 5 + (position[1] - 19) * 5 # Decreases as we move up and left
        manhattan +=  penalty

    return manhattan


def serialize(data):
    return frozenset((k, tuple(v)) for k, v in data.items())


def draw_big_network(data, position):
    for y in range(25):
        for x in range(35):
            if (y,x) == position:
                print(f"({data[(y,x)][0]}T/{data[(y,x)][0] + data[(y,x)][1]}T) -- ", end="")
            else:
                print(f"{data[(y,x)][0]}T/{data[(y,x)][0] + data[(y,x)][1]}T -- ", end="")
        print()
        print("    |     "*35)
    print()


def draw_small_network(data, position, goal):
    print(utils.CLEAR)
    for y in range(25):
        for x in range(35):
            if y == 11 and x>=21:
                print("#", end="")
            elif (y,x) == goal:
                print("G", end="")
            elif (y,x) == position:
                print("_", end="")
            else:
                print(".", end="")
        print()
    print()


def part2(data, start):

    counter = count()
    max_x = 34
    max_y = 24
    goal = (0,34)
    pq = []
    heapq.heappush(pq, (distance(start, goal), 0, start, goal, next(counter), data))

    visited = set()

    while pq:
        _, steps, position, goal, _, data = heapq.heappop(pq)
        # draw_small_network(data, position, goal)

        if goal == (0, 0):
            return steps

        state = (position, goal, serialize(data))
        if state in visited:
            continue
        visited.add(state)

        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_data = deepcopy(data)
            next_position = (position[0]+direction[0], position[1]+direction[1])
            if (
                0 <= next_position[0] <= max_y 
                and 0 <= next_position[1] <= max_x
            ):
                if new_data[next_position][0] < new_data[position][1]:
                    new_data[position][0] += new_data[next_position][0]
                    new_data[position][1] -= new_data[next_position][0]
                    new_data[next_position][1] += new_data[next_position][0]
                    new_data[next_position][0] = 0
                    if next_position == goal:
                        heapq.heappush(pq, (distance(next_position, goal), steps + 1, next_position, position, next(counter), new_data))
                    else:
                        heapq.heappush(pq, (distance(next_position, goal), steps + 1, next_position, goal, next(counter), new_data))

    return "Not solved"
        
                    


    
    
    


if __name__ == "__main__":
    main()