with open('p11/input.txt', 'r') as file:
    lines = file.read().splitlines()
    outs = {k.strip(): v.strip().split() for line in lines for k, v in [line.split(': ', 1)]}

start = "svr"
end = "out"

should_contain = set(["dac", "fft"])
status = {v: False for v in should_contain}

def are_found():
    for k in status:
        if not status[k]:
            return False
    return True

def try_add(v):
    if v in should_contain:
        status[v] = True

def try_remove(v):
    if v in should_contain:
        status[v] = False

def dfs(s, visited):
    if s == end:
        return 1 if are_found() else 0
    n = 0
    for o in outs[s]:
        if o not in visited:
            visited.add(o)
            try_add(o)
            n += dfs(o, visited)
            visited.remove(o)
            try_remove(o)

    return n

print(f"ans = {dfs(start, set([start]))}")