with open('p7/input.txt', 'r') as file:
    lines = file.read().splitlines()
    M = [[v for v in line] for line in lines]

def add(d, c, v):
    if c in d:
        d[c] += v
    else:
        d[c] = v

beam = {i: 1 for i, s in enumerate(M[0]) if s == "S"}

m = len(M)
n = len(M[0])
for r in range(len(M)-1):
    new_beams = dict()
    for c in beam:
        if M[r][c] == "^":
            if c-1 >= 0:
                add(new_beams, c-1, beam[c])
            if c+1 < n:
                add(new_beams, c+1, beam[c])
        else:
            add(new_beams, c, beam[c])
    beam = new_beams

ans = 0
for v in beam.values():
    ans += v

print(f"ans = {ans}")