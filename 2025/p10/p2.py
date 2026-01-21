with open('p10/input.txt', 'r') as file:
    lines = file.read().splitlines()
    buttons = []
    joltages = []
    for line in lines:
        [l, r] = line.split("{")
        [_, button] = l.split("]")
        buttons.append([tuple(int(v) for v in b[1:-1].split(",")) for b in button.strip().split()])
        joltages.append(tuple(int(v) for v in r[:-1].split(",")))

# takes the current state and the operator (both tuples)
# returns the new state after applying that operator
def get_next(s, o):
    ns = list(s)
    for v in o:
        ns[v] += 1
    return tuple(ns)

def is_out(s, rs):
    for v1, v2 in zip(s, rs):
        if v1 > v2:
            return True
    return False

# takes a tuple (required state) and a list of tuples (possible operations)
# returns the minimum steps required to reach rs from 0
def bfs_till(rs, ops):
    cs = [tuple([0] * len(rs))]
    ns = set()
    d = 1

    visited = set()
    visited.add(cs[0])

    while len(cs) > 0:
        print(f"Checking {len(cs)}")
        for s in cs:
            for o in ops:
                next_state = get_next(s, o)
                if next_state == rs:
                    return d
                if not is_out(next_state, rs) and next_state not in visited:
                    ns.add(next_state)
                    visited.add(next_state)
        d += 1
        cs = list(ns)

    print(f"didn't find any path for {rs}")
    return 0

ans = 0
for i in range(len(joltages)):
    ans += bfs_till(joltages[i], buttons[i])

print(f"ans = {ans}")
