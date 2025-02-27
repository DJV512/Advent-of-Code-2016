FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

import time
import utils
from hashlib import md5

sample_salt = "abc"
real_salt = "ahsbgdzn"

# salt = sample_salt
salt = real_salt

def main():
    start_time = time.time()

    parse_time = time.time()

    answer1 = part1()
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



def first_triple(hash):
    for i in range(2,len(hash)):
        if hash[i] == hash[i-1] and hash[i] == hash[i-2]:
            return str(hash[i])
    return ""


def has_quints(hash):
    quints = []
    for i in range(4,len(hash)):
        if hash[i] == hash[i-1] and hash[i] == hash[i-2] and hash[i] == hash[i-3] and hash[i] == hash[i-4]:
            quints.append(str(hash[i]))
    return quints


def part1():
    i = 0
    actual_keys = []
    potential_keys = {}
    while len(actual_keys) <= 80:
        password = salt + str(i)
        hash = md5(password.encode()).hexdigest()
        trip = first_triple(hash)
        quints = has_quints(hash)
        
        if quints:
            for quint in quints:
                for key in potential_keys.copy():
                    if potential_keys[key] == quint and i-key <= 1000:
                        actual_keys.append((key, md5((salt+str(key)).encode()).hexdigest(), i, md5((salt+str(i)).encode()).hexdigest()))
                        potential_keys.pop(key)

        if trip != "":
            potential_keys[i] = trip
        
        i += 1

    sorted_keys = sorted(actual_keys, key=lambda x: x[0])

    # for i, (first_key, first_hash, second_key, second_hash) in enumerate(sorted_keys):
    #     print(f"{i+1} \n{first_key}: {first_hash} \n{second_key}: {second_hash}\n")

    return sorted_keys[63][0]


def part2():
    i = 0
    actual_keys = []
    potential_keys = {}
    while len(actual_keys) <= 80:
        hash = salt + str(i)

        for _ in range(2017):
            hash = md5(hash.encode()).hexdigest()

        trip = first_triple(hash)
        quints = has_quints(hash)
        
        if quints:
            for quint in quints:
                for key in potential_keys.copy():
                    if potential_keys[key] == quint and i-key <= 1000:
                        actual_keys.append((key, md5((salt+str(key)).encode()).hexdigest(), i, md5((salt+str(i)).encode()).hexdigest()))
                        potential_keys.pop(key)

        if trip != "":
            potential_keys[i] = trip
        
        i += 1

    sorted_keys = sorted(actual_keys, key=lambda x: x[0])

    # for i, (first_key, first_hash, second_key, second_hash) in enumerate(sorted_keys):
    #     print(f"{i+1} \n{first_key}: {first_hash} \n{second_key}: {second_hash}\n")

    return sorted_keys[63][0]


if __name__ == "__main__":
    main()