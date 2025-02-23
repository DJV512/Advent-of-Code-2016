# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
import hashlib


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
        data = f.readline().strip()

    # return utils.grid_parse(data)

    return data


def part1(data):
    password = ""
    for i in range(1000000000):
        hash = hashlib.md5((data+str(i)).encode())
        m = hash.hexdigest()
        if m[0:5] == "00000":
            password += m[5]
        if len(password) == 8:
            break
    return password


def part2(data):
    chars = 0
    password = ["#" for _ in range(8)]
    for i in range(1000000000):
        hash = hashlib.md5((data+str(i)).encode())
        m = hash.hexdigest()
        if m[0:5] == "00000":
            if 48 <= ord(m[5]) <= 55:
                if password[int(m[5])] == "#":
                    password[int(m[5])] = m[6]
                    chars += 1
        if chars == 8:
            break
    return "".join(password)


if __name__ == "__main__":
    main()