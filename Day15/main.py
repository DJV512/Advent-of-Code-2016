FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

import time
import utils


def main():
    start_time = time.time()

    data_p1, data_p2 = parse_data()
    parse_time = time.time()

    answer1 = part1(data_p1)
    part1_time = time.time()
    answer2 = part2(data_p2)
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
    sample_data = [
        (1, 5, 4),
        (2, 2, 1)
    ]

    data_p1 = [
        (1, 7, 0),
        (2, 13, 0),
        (3, 3, 2),
        (4, 5, 2),
        (5, 17, 0),
        (6, 19, 7)
    ]

    data_p2 = [
        (1, 7, 0),
        (2, 13, 0),
        (3, 3, 2),
        (4, 5, 2),
        (5, 17, 0),
        (6, 19, 7),
        (7, 11, 0)
    ]

    return data_p1, data_p2


def part1(data):
    for i in range(1000000000000000):
        positions = []
        for x, (disc_name, disc_size, disc_position) in enumerate(data, start=1):
            new_position = (disc_position + i + x) % disc_size
            positions.append((disc_name, new_position))
        keep_going = False
        for _, position in positions:
            if position != 0:
                keep_going = True
                break

        if not keep_going:
            break

    return i


def part2(data):
    for i in range(1000000000000000):
        positions = []
        for x, (disc_name, disc_size, disc_position) in enumerate(data, start=1):
            new_position = (disc_position + i + x) % disc_size
            positions.append((disc_name, new_position))
        keep_going = False
        for _, position in positions:
            if position != 0:
                keep_going = True
                break

        if not keep_going:
            break
        
    return i


if __name__ == "__main__":
    main()