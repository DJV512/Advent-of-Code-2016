# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import matplotlib.pyplot as plt

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
    for line in data:
        moves = line.strip().split(", ")

    return moves


def part1(data):
    location = (0,0)
    direction = (-1,0)
    map = [(0,0)]
    for move in data:
        if move[0] == "L":
            if direction == (-1, 0):
                location = (location[0], location[1] - int(move[1:]))
                direction = (0,-1)
            elif direction == (1, 0):
                location = (location[0], location[1] + int(move[1:]))
                direction = (0, 1)
            elif direction == (0, 1):
                location = (location[0] - int(move[1:]), location[1])
                direction = (-1, 0)
            elif direction == (0, -1):
                location = (location[0] + int(move[1:]), location[1])
                direction = (1, 0)
        elif move[0] == "R":
            if direction == (-1, 0):
                location = (location[0], location[1] + int(move[1:]))
                direction = (0, 1)
            elif direction == (1, 0):
                location = (location[0], location[1] - int(move[1:]))
                direction = (0, -1)
            elif direction == (0, 1):
                location = (location[0] + int(move[1:]), location[1])
                direction = (1, 0)
            elif direction == (0, -1):
                location = (location[0] - int(move[1:]), location[1])
                direction = (-1, 0)
        map.append(location)


    # # Unzip into separate x and y lists
    # x, y = zip(*map)

    # # Change the sign of the "y" values because of the way I stored directions
    # # I stored direction as (y,x) so it needs to be reversed. And I stored the y value
    # # as south being +1 and north being -1, which needs to be reversed to properly
    # # plot the left and right turns.
    # x = [-val for val in x]

    # # Plot the points and lines
    # plt.plot(y, x, marker="o", linestyle="-", color="r")

    # # Add labels
    # plt.xlabel("X-axis")
    # plt.ylabel("Y-axis")
    # plt.title("Path Plot")

    # # Show the plot
    # plt.show()
        
    return abs(location[0]) + abs(location[1])


def part2(data):
    location = (0,0)
    direction = (-1,0)
    map = set()
    map.add((0,0))
    for move in data:
        if move[0] == "L":
            if direction == (-1, 0):
                for _ in range(int(move[1:])):
                    location = (location[0], location[1] - 1)
                    if location in map:
                        print(location)
                        return abs(location[0]) + abs(location[1])
                    else:
                        map.add(location)
                direction = (0,-1)
            elif direction == (1, 0):
                for _ in range(int(move[1:])):
                    location = (location[0], location[1] + 1)
                    if location in map:
                        print(location)
                        return abs(location[0]) + abs(location[1])
                    else:
                        map.add(location)
                direction = (0, 1)
            elif direction == (0, 1):
                for _ in range(int(move[1:])):
                    location = (location[0] - 1, location[1])
                    if location in map:
                        print(location)
                        return abs(location[0]) + abs(location[1])
                    else:
                        map.add(location)
                direction = (-1, 0)
            elif direction == (0, -1):
                for _ in range(int(move[1:])):
                    location = (location[0] + 1, location[1])
                    if location in map:
                        print(location)
                        return abs(location[0]) + abs(location[1])
                    else:
                        map.add(location)
                direction = (1, 0)
        elif move[0] == "R":
            if direction == (-1, 0):
                for _ in range(int(move[1:])):
                    location = (location[0], location[1] + 1)
                    if location in map:
                        print(location)
                        return abs(location[0]) + abs(location[1])
                    else:
                        map.add(location)
                direction = (0, 1)
            elif direction == (1, 0):
                for _ in range(int(move[1:])):
                    location = (location[0], location[1] - 1)
                    if location in map:
                        print(location)
                        return abs(location[0]) + abs(location[1])
                    else:
                        map.add(location)
                direction = (0, -1)
            elif direction == (0, 1):
                for _ in range(int(move[1:])):
                    location = (location[0] + 1, location[1])
                    if location in map:
                        print(location)
                        return abs(location[0]) + abs(location[1])
                    else:
                        map.add(location)
                direction = (1, 0)
            elif direction == (0, -1):
                for _ in range(int(move[1:])):
                    location = (location[0] - 1, location[1])
                    if location in map:
                        print(location)
                        return abs(location[0]) + abs(location[1])
                    else:
                        map.add(location)
                direction = (-1, 0)

if __name__ == "__main__":
    main()