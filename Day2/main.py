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
    
    data = [line.strip() for line in data]

    # # grid based input
    # data = [list(line.strip()) for line in data]

    return data


def part1(data):
    keypad = {
        (0,0): "1",
        (0,1): "2",
        (0,2): "3",
        (1,0): "4",
        (1,1): "5",
        (1,2): "6",
        (2,0): "7",
        (2,1): "8",
        (2,2): "9",
    }

    position = (1,1)
    code = ""
    for line in data:
        for char in line:
            if char == "U":
                if position[0] != 0:
                    position = (position[0]-1, position[1])
            elif char == "D":
                if position[0] != 2:
                    position = (position[0]+1, position[1])
            elif char == "L":
                if position[1] != 0:
                    position = (position[0], position[1]-1)
            elif char == "R":
                if position[1] != 2:
                    position = (position[0], position[1]+1)
        code += keypad[position]
                

    return code


def part2(data):
    keypad = {
        (0,0): "",
        (0,1): "",
        (0,2): "1",
        (0,3): "",
        (0,4): "",
        (1,0): "",
        (1,1): "2",
        (1,2): "3",
        (1,3): "4",
        (1,4): "",
        (2,0): "5",
        (2,1): "6",
        (2,2): "7",
        (2,3): "8",
        (2,4): "9",
        (3,0): "",
        (3,1): "A",
        (3,2): "B",
        (3,3): "C",
        (3,4): "",
        (4,0): "",
        (4,1): "",
        (4,2): "D",
        (4,3): "",
        (4,4): "",
    }

    position = (2,0)
    code = ""
    for line in data:
        for char in line:
            if char == "U":
                if 0 <= position[0]-1 <= 4:
                    if keypad[(position[0]-1, position[1])] != "":
                        position = (position[0]-1, position[1])
            elif char == "D":
                if 0 <= position[0]+1 <= 4:
                    if keypad[(position[0]+1, position[1])] != "":
                        position = (position[0]+1, position[1])
            elif char == "L":
                if 0 <= position[1]-1 <= 4:
                    if keypad[(position[0], position[1]-1)] != "":
                        position = (position[0], position[1]-1)
            elif char == "R":
                if 0 <= position[1]+1 <= 4:
                    if keypad[(position[0], position[1]+1)] != "":
                        position = (position[0], position[1]+1)
        code += keypad[position]
                

    return code


if __name__ == "__main__":
    main()