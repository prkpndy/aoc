with open('p11/input.txt', 'r') as file:
    lines = file.read().splitlines()
    outs = {k.strip(): v.strip().split() for line in lines for k, v in [line.split(': ', 1)]}

start = "you"
end = "out"

def dfs(s, visited):
    if s == end:
        return 1

    n = 0
    for o in outs[s]:
        if o not in visited:
            visited.add(o)
            n += dfs(o, visited)
            visited.remove(o)

    return n

print(f"ans = {dfs(start, set([start]))}")