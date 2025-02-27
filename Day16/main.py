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

    sample_data = ("10000", 20)
    data_p1 = ("11110010111001001", 272)
    data_p2 = ("11110010111001001", 35651584)

    return data_p1, data_p2


def find_checksum(data):
    a = data[0]
    while len(a) < data[1]:
        b = a[::-1]
        b = "".join(["0" if val == "1" else "1" for val in b])
        a = a + "0" + b
        
    a = a[:data[1]]

    keep_going = True
    while keep_going:
        a = [a[i:i+2] for i in range(0, len(a), 2)]
        a = "".join(["1" if val[0]==val[1] else "0" for val in a])

        if len(a) % 2 == 1:
            keep_going = False

    return a


def part1(data):
    return find_checksum(data)
    

def part2(data):
    return find_checksum(data)


if __name__ == "__main__":
    main()