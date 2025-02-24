# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils

GRID_X = 50
GRID_Y = 6

# GRID_X = 7
# GRID_Y = 3

def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1, grid = part1(data)
    part1_time = time.time()
    answer2 = part2(grid)
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

    rules = []
    for line in data:
        line = line.strip()
        if "rect" in line:
            _, size = line.split(" ")
            x, y = size.split("x")
            rules.append(("rect", y, x, "N/A"))
        elif "rotate" in line:
            half1, half2 = line.split("=")
            variable = half1[-1]
            which, how_much = half2.split(" by ")
            rules.append(("rotate", variable, which, how_much))
        else:
            raise TypeError("Unknown input")


    return rules


def part1(data):
    grid = [["." for _ in range(GRID_X)] for _ in range(GRID_Y)]
    for rule_type, first, second, third in data:
        if rule_type == "rect":
            for y in range(int(first)):
                for x in range(int(second)):
                    grid[y][x] = "#"
        elif rule_type == "rotate":
            if first == "x":
                old_column = []
                for y in range(GRID_Y):
                    old_column.append(grid[y][int(second)])
                new_column = ["." for _ in range(len(old_column))]
                for i in range(len(old_column)):
                    new_column[(i+int(third))%len(old_column)] = old_column[i]
                for i, char in enumerate(new_column):
                    grid[i][int(second)] = char

            elif first == "y":
                old_row = []
                for x in range(GRID_X):
                    old_row.append(grid[int(second)][x])
                new_row = ["." for _ in range(len(old_row))]
                for i in range(len(old_row)):
                    new_row[(i+int(third))%len(old_row)] = old_row[i]
                for i, char in enumerate(new_row):
                    grid[int(second)][i] = char
       
    total=0
    for row in grid:
        print(row)
        for column in row:
            if column == "#":
                total += 1
    print()
    return total, grid


def part2(data):
    for row in data:
        print("".join(row))
    return None


if __name__ == "__main__":
    main()