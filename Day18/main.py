FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

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
    sample_data = ".^^.^.^^^^"
    data = "^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^"
    
    return data


def determine_tile(a, b, c):
    if a == b == "^" and c != "^":
        return "^"
    elif b == c == "^" and a != "^":
        return "^"
    elif a == "^" and b != "^" and c != "^":
        return "^"
    elif c == "^" and a != "^" and b != "^":
        return "^"
    else:
        return "."
    

def part1(data):
    total_safe = 0
    final_length = 40
    for y in range(final_length):
        new_data = ""
        for i, char in enumerate(data):
            if char == ".":
                total_safe += 1
            if y != final_length-1:
                if i == 0:
                    new_data += determine_tile(".", data[i], data[i+1])
                elif i == len(data)-1:
                    new_data += determine_tile(data[i-1], data[i], ["."])
                else:
                    new_data += determine_tile(data[i-1], data[i], data[i+1])

        data = new_data

    return total_safe


def part2(data):
    total_safe = 0
    final_length = 400000
    for y in range(final_length):
        new_data = ""
        for i, char in enumerate(data):
            if char == ".":
                total_safe += 1
            if y != final_length-1:
                if i == 0:
                    new_data += determine_tile(".", data[i], data[i+1])
                elif i == len(data)-1:
                    new_data += determine_tile(data[i-1], data[i], ["."])
                else:
                    new_data += determine_tile(data[i-1], data[i], data[i+1])

        data = new_data

    return total_safe


if __name__ == "__main__":
    main()