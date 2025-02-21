# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

from collections import Counter

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

    item_counts = []
    for line in data:
        name_and_id, checksum = line.strip().split("[")
        checksum = checksum[:-1]
        name_and_id_list = name_and_id.split("-")
        id = int(name_and_id_list.pop())
        name = "".join(name_and_id_list)
        count = Counter(name)
        item_counts.append((name, count, id, checksum))
    
    return item_counts


def part1(data):
    total = 0
    for _, count, id, checksum in data:
        add_in = True
        most = count.most_common()
        sorted_most = sorted(most, key=lambda x: (-x[1], x[0]))
        for i, char in enumerate(checksum):
            if char != sorted_most[i][0]:
                add_in = False
                break
        if add_in:
            total += id

    return total


def part2(data):
    for name, _, id, _ in data:
        shift = id % 26
        numbers = [ord(char) + shift for char in name]
        new_numbers = []
        for number in numbers:
            if number > 122:
                number -= 26
            new_numbers.append(number)
        new_name = [chr(num) for num in new_numbers ]
        final_name = "".join(new_name)
        if "north" in final_name:
            print(final_name)
            print(id)
        if final_name == "northpoleobjectstorage":
            return id



if __name__ == "__main__":
    main()