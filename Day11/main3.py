from collections import deque, namedtuple
import sys
import time

# This is NOT my code. I had less than zero idea of how to solve this problem. I found this code
# from the AOC subreddit, from micro_apple (bcongdon), linked here:
# https://www.reddit.com/r/adventofcode/comments/5hqeau/2016_day_11_python_elevator_trips_animated/
# https://github.com/bcongdon/advent_of_code_2016/blob/master/Day10-19/11.py
# This works incredibly fast and solved both of my parts (once I changed it to my own input).
# There are also several minor changes between this and main2.py as I worked through it adding print statements
# and changing variable names to try and figure out how it was working.
# Many many thanks to bcongdon for saving me hours of pulling my hair out, and also
# for the time I spent poring over your code and figuring out how it works. I definitely learned alot!


indicies = ["stg", "stm", "plg", "plm", "thg", "thm", "rug", "rum", "cug", "cum", "elg", "elm", "dig", "dim"]
part1 = [1, 1, 1, 1, 2, 3, 2, 2, 2, 2]
part2 = [1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 1, 1, 1, 1]

State = namedtuple('State', ['f', 'e', 's', 'p'])


def valid(state):
    if not 1 <= state.e <= 4:
        return False
    if any(not 1 <= i <= 4 for i in state.f):
        return False

    for idx, v in enumerate(state.f[1::2]):
        idx = idx * 2 + 1
        if v != state.f[idx - 1] and any(v == i for i in state.f[0::2]):
            return False
    return True


def generalize(state):
    g = [sum(1 for v in state.f[::2] if v == fn) for fn in range(1, 5)]
    m = [sum(1 for v in state.f[1::2] if v == fn) for fn in range(1, 5)]
    return ''.join(map(str, g + m)) + str(state.e)


def solved(state):
    return all(i == 4 for i in state.f)


def make_animation(state):
    parents = []
    while state:
        parents.append(state)
        state = state.p
    
    parents.reverse()
    for p in parents:
        sys.stdout.write('\033c')
        for fn in range(1, 5):
            out = 'F%s: ' % fn
            out += ' '.join(indicies[idx].upper()
                            if i == fn else '   ' for idx, i in enumerate(p.f))
            if fn == p.e:
                out += ' [E]'
            print(out)
        time.sleep(0.2)

    print('\n')


def bfs(floor_config, part, animate=True):
    bfs_q = deque()
    bfs_q.append(State(floor_config, 1, 0, None))
    seen = set()
    nodes = 1
    while bfs_q:
        state = bfs_q.popleft()
        generalized = generalize(state)
        
        if generalized in seen or not valid(state):
            continue
        seen.add(generalized)

        if solved(state):
            if animate:
                make_animation(state)
            print("Part %s:\tSolved in %s steps." % (part, state.s))
            print("\tConsidered %s nodes." % nodes)
            return

        for idx in range(len(state.f)):
            i = state.f[idx]
            if i != state.e:  # item can't be moved bc not in elevator
                continue
            state.f[idx] -= 1
            bfs_q.append(State(list(state.f), state.e - 1, state.s + 1, state))
            state.f[idx] += 2
            bfs_q.append(State(list(state.f), state.e + 1, state.s + 1, state))
            state.f[idx] -= 1

            nodes += 2

            for jdx in range(idx + 1, len(state.f)):
                if state.f[jdx] != state.e:
                    continue
                state.f[jdx] -= 1
                state.f[idx] -= 1
                bfs_q.append(State(list(state.f), state.e - 1,
                                   state.s + 1, state))
                state.f[jdx] += 2
                state.f[idx] += 2
                bfs_q.append(State(list(state.f), state.e + 1,
                                   state.s + 1, state))
                state.f[jdx] -= 1
                state.f[idx] -= 1
                nodes += 2
    else:
        print("Unable to solve. :(")


if __name__ == '__main__':
    bfs(part1, 1, True)
    bfs(part2, 2, True)