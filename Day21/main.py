# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils

descrambled_sample = "abcde"
descrambled_real = "abcdefgh"

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

    rules = []
    for line in data:
        parts = line.strip().split()

        if parts[0] == "rotate":
            if parts[1] == "based":
                rules.append((parts[0], parts[1], parts[6]))
            else:
                rules.append((parts[0], parts[1], parts[2]))
        elif parts[0] == "swap":
            rules.append((parts[0], parts[2], parts[5]))
        elif parts[0] == "reverse":
            rules.append((parts[0], parts[2], parts[4]))
        elif parts[0] == "move":
            rules.append((parts[0], parts[2], parts[5]))

    return rules


def part1(data):
    password = descrambled_real
    for r1, r2, r3 in data:
        if r1 == "rotate" and r2 == "based":
            index = password.index(r3)
            if index >= 4:
                extra = 1
            else:
                extra = 0
            amount_to_rotate = (index + 1 + extra) % len(password)
            password = password[len(password)-amount_to_rotate:] + password[:len(password)-amount_to_rotate]
        elif r1 == "rotate":
            amount_to_rotate = int(r3) % len(password)
            if r2 == "right":
                password = password[len(password)-amount_to_rotate:] + password[:len(password)-amount_to_rotate]
            else:
                password = password[amount_to_rotate:] + password[:amount_to_rotate]
        elif r1 == "move":
            to_move = password[int(r2)]
            password = list(password)
            password.remove(to_move)
            password.insert(int(r3), to_move)
            password = "".join(password)
        elif r1 == "swap":
            try:
                first = password[int(r2)]
                second = password[int(r3)]
                password = list(password)
                password[int(r2)] = second
                password[int(r3)] = first
                password = "".join(password)
            except ValueError:
                password = list(password)
                first = password.index(r2)
                second = password.index(r3)
                password[first] = r3
                password[second] = r2
                password = "".join(password)
        elif r1 == "reverse":
            to_reverse = password[int(r2):int(r3)+1]
            reversed = to_reverse[::-1]
            password = list(password)
            r2 = int(r2)
            for char in reversed:
                password[r2] = char
                r2 +=1
            password = "".join(password)

    return password


def part2(data):
    password = "fbgdceah"
    for r1, r2, r3 in data[::-1]:
        if r1 == "rotate" and r2 == "based": #fine
            index = password.index(r3)
            if index == 0:
                amount_to_rotate = 9
            elif index == 1:
                amount_to_rotate = 1
            elif index == 2:
                amount_to_rotate = 6
            elif index == 3:
                amount_to_rotate = 2
            elif index == 4:
                amount_to_rotate = 7
            elif index == 5:
                amount_to_rotate = 3
            elif index == 6:
                amount_to_rotate = 0
            elif index == 7:
                amount_to_rotate = 4

            password = password[amount_to_rotate:] + password[:amount_to_rotate]
        elif r1 == "rotate": #fine
            amount_to_rotate = int(r3) % len(password)
            if r2 == "left":
                password = password[len(password)-amount_to_rotate:] + password[:len(password)-amount_to_rotate]
            else:
                password = password[amount_to_rotate:] + password[:amount_to_rotate]
        elif r1 == "move": #fine
            to_move = password[int(r3)]
            password = list(password)
            password.remove(to_move)
            password.insert(int(r2), to_move)
            password = "".join(password)
        elif r1 == "swap": #fine
            try:
                first = password[int(r2)]
                second = password[int(r3)]
                password = list(password)
                password[int(r2)] = second
                password[int(r3)] = first
                password = "".join(password)
            except ValueError:
                password = list(password)
                first = password.index(r2)
                second = password.index(r3)
                password[first] = r3
                password[second] = r2
                password = "".join(password)
        elif r1 == "reverse": # fine
            to_reverse = password[int(r2):int(r3)+1]
            reversed = to_reverse[::-1]
            password = list(password)
            r2 = int(r2)
            for char in reversed:
                password[r2] = char
                r2 +=1
            password = "".join(password)

    return password


if __name__ == "__main__":
    main()