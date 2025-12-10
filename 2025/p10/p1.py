with open('p10/input.txt', 'r') as file:
    lines = file.read().splitlines()
    lights = []
    buttons = []
    for line in lines:
        [l, _] = line.split("{")
        [light, button] = l.split("]")
        lights.append(tuple([v for v in light[1:]]))
        buttons.append([[int(v) for v in b[1:-1].split(",")] for b in button.strip().split()])

# takes the current state and the operator
# returns the new state after applying that operator
def get_next(s, o):
    ns = list(s)
    for v in o:
        ns[v] = "#" if ns[v] == "." else "."
    return tuple(ns)

def bfs_till(rs, ops):
    cs = [tuple(["."] * len(rs))]
    ns = set()
    d = 1

    visited = set()
    visited.add(cs[0])

    while len(cs) > 0:
        for s in cs:
            for o in ops:
                next_state = get_next(s, o)
                if next_state == rs:
                    return d
                if next_state not in visited:
                    ns.add(next_state)
        d += 1
        cs = list(ns)

    print(f"didn't find any path for {rs}")
    return 0

ans = 0
for i in range(len(lights)):
    ans += bfs_till(lights[i], buttons[i])

print(f"ans = {ans}")
