import time
import utils
from collections import deque

sample_number = 10
real_number = 1358

sample_goal = (4,7)
real_goal = (39,31)

# number = sample_number
number = real_number

# goal = sample_goal
goal = real_goal

def main():
    start_time = time.time()


    parse_time = time.time()

    answer1 = part1(goal)
    part1_time = time.time()
    answer2 = part2()
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


def determine_space(pos):
    y, x = pos
    value = x*x + 3*x + 2*x*y + y + y*y + number
    bit_value = bin(value)
    ones = sum(bit == "1" for bit in str(bit_value))

    if ones % 2 == 0:
        return "."
    else:
        return "#"
    

def print_path(visited):
    print(utils.CLEAR)
    for y in range(50):
        for x in range(50):
            if (y,x) in visited:
                print(f"{utils.RED}O{utils.RESET}", end="")
            else:
                print(determine_space((y, x)), end="")
        print()


def part1(goal):
    start = (1,1)
    bfs_q = deque()
    bfs_q.append((start, set()))

    while bfs_q:
        position, visited = bfs_q.popleft()

        if position == goal:
            visited.add(goal)
            steps = len(visited) - 1
            break

        new_visited = visited.copy()
        new_visited.add(position)

        for direction in [(1,0), (-1, 0), (0, 1), (0, -1)]:
            next_position = (position[0]+direction[0], position[1]+direction[1])

            if (
                next_position[0] >= 0
                and next_position[1] >= 0
                and next_position not in new_visited
                and determine_space(next_position) != "#"
            ):
                bfs_q.append((next_position, new_visited))
  
    # print_path(visited)
    return steps


def part2():
    start = (1,1)
    bfs_q = deque()
    bfs_q.append((start, set(), 0))
    can_visit = set()

    while bfs_q:
        position, visited, steps = bfs_q.popleft()

        can_visit.add(position)

        new_visited = visited.copy()
        new_visited.add(position)

        for direction in [(1,0), (-1, 0), (0, 1), (0, -1)]:
            next_position = (position[0]+direction[0], position[1]+direction[1])

            if (
                next_position[0] >= 0
                and next_position[1] >= 0
                and next_position not in new_visited
                and determine_space(next_position) != "#"
            ):
                if steps + 1 <= 50:
                    bfs_q.append((next_position, new_visited, steps+1))

    # print_path(can_visit)
    
    return len(can_visit)


if __name__ == "__main__":
    main()