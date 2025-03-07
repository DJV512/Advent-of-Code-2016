# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
import heapq
from copy import deepcopy


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1, start_location, nodes, side_lengths = part1(data)
    part1_time = time.time()
    answer2 = part2(start_location, nodes, side_lengths)
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

    return utils.grid_parse(data)


def serialize(goals):
    return frozenset(goals)


## This version of part 1 is a straight solver of the problem, and works well on the sample input.
## But because backtracking has to be allowed for this problem, on a larger input it takes forever.
## Instead used the algorithm to find the shortest distance between each of the nodes, and then 
## used that data to find the shortest path. See updated part1 below.

# def part1(data):
#     goals = []
#     length = len(data)
#     width = len(data[0])
#     start = (0,0)
#     for y in range(length):
#         for x in range(width):
#             if data[y][x] in ["1","2","3","4","5","6","7","8","9"]:
#                 goals.append((y,x))
#             elif data[y][x] == "0":
#                 start = (y,x)

#     pq = []
#     heapq.heappush(pq, (0, start, (0,0), set(), set(), []))

#     while pq:
#         steps, position, previous, visited, goals_found, path = heapq.heappop(pq)
#         # print(f"{steps=}, {position=}, {previous=}, {goals_found=}")
#         # print()

#         new_goals_found = deepcopy(set(goals_found))
#         if (
#             data[position[0]][position[1]] in ["1","2","3","4","5","6","7","8","9"]
#             and position not in goals_found
#         ):
#             new_goals_found.add(position)

#         if len(new_goals_found) == len(goals):
#             path.append(position)
#             # print(path)
#             return steps
        
#         state = (steps, position, previous, serialize(goals_found))

#         if state in visited:
#             continue
#         new_visited = deepcopy(visited)
#         new_visited.add(state)

#         new_path = deepcopy(path)
#         new_path.append(position)

#         for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
#             next_position  = (position[0]+direction[0], position[1]+direction[1])

#             if (
#                 0 <= next_position[0] < length
#                 and 0 <= next_position[1] < width
#                 and data[next_position[0]][next_position[1]] != "#"
#             ):
#                 heapq.heappush(pq, (steps+1, next_position, position, new_visited, new_goals_found, new_path))

#     return "Not solved"


def part1(data):
    nodes = []
    length = len(data)
    width = len(data[0])
    for y in range(length):
        for x in range(width):
            if data[y][x] in ["0", "1","2","3","4","5","6","7","8","9"]:
                nodes.append((y,x))
            if data[y][x] == "0":
                start_location = (y,x)


    side_lengths = {}
    for goal1 in nodes:
        for goal2 in nodes:
            if goal1 != goal2 and (goal1, goal2) not in side_lengths:

                pq = []
                heapq.heappush(pq, (0, goal1, set()))

                while pq:
                    steps, position, visited  = heapq.heappop(pq)

                    if position == goal2:
                        side_lengths[(goal1, goal2)] = steps
                        side_lengths[(goal2, goal1)] = steps
                        break

                    if position in visited:
                        continue
                    visited.add(position)

                    for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
                        next_position  = (position[0]+direction[0], position[1]+direction[1])

                        if (
                            0 <= next_position[0] < length
                            and 0 <= next_position[1] < width
                            and data[next_position[0]][next_position[1]] != "#"
                        ):
                            heapq.heappush(pq, (steps+1, next_position, visited))
    
    pq = []
    left = []
    possible_lengths = []
    nodes.remove(start_location)
    for node in nodes:
        deep_nodes = deepcopy(nodes)
        deep_nodes.remove(node)
        heapq.heappush(pq, (0, start_location, node, deep_nodes, [start_location, node]))

    while pq:
        steps, start, end, left, path = heapq.heappop(pq)

        new_steps = steps + side_lengths[(start, end)]

        if len(left) == 0:
            possible_lengths.append((new_steps, path))
            continue

        for node in left:
            new_left = deepcopy(left)
            new_left.remove(node)

            new_path = deepcopy(path)
            new_path.append(node)
            heapq.heappush(pq, (new_steps, end, node, new_left, new_path))

    return sorted(possible_lengths)[0], start_location, nodes, side_lengths


def part2(start_location, nodes, side_lengths):

    pq = []
    left = []
    possible_lengths = []
    for node in nodes:
        deep_nodes = deepcopy(nodes)
        deep_nodes.remove(node)
        heapq.heappush(pq, (0, start_location, node, deep_nodes, [start_location, node], False))

    while pq:
        steps, start, end, left, path, endgame = heapq.heappop(pq)

        new_steps = steps + side_lengths[(start, end)]

        if len(left) == 0:
            if endgame:
                possible_lengths.append((new_steps, path))
            else:
                new_path = deepcopy(path)
                new_path.append(start_location)

                heapq.heappush(pq, (new_steps, end, start_location, [], new_path, True))
            continue

        for node in left:
            new_left = deepcopy(left)
            new_left.remove(node)

            new_path = deepcopy(path)
            new_path.append(node)
            heapq.heappush(pq, (new_steps, end, node, new_left, new_path, False))

    return sorted(possible_lengths)[0]

if __name__ == "__main__":
    main()