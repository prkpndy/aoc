with open('p7/input.txt', 'r') as file:
    lines = file.read().splitlines()
    M = [[v for v in line] for line in lines]

beam = set([i for i, s in enumerate(M[0]) if s == "S"])

m = len(M)
n = len(M[0])
ans = 0
for r in range(len(M)-1):
    to_add = set()
    to_remove = set()
    for c in beam:
        if M[r][c] == "^":
            ans += 1
            to_remove.add(c)
            if c-1 >= 0:
                to_add.add(c-1)
            if c+1 < n:
                to_add.add(c+1)
    beam.difference_update(to_remove)
    beam = beam.union(to_add)

print(f"ans = {ans}")