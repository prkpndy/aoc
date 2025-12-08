import math

T = 1000
TOP = 3

with open('p8/input.txt', 'r') as file:
    lines = file.read().splitlines()
    nums = [[int(n) for n in l.split(",")] for l in lines]

M = len(nums)

cir = list(range(M))

def update_cir(p, q):
    for i in range(len(cir)):
        if cir[i] == cir[q]:
            cir[i] = cir[p]

def get_dist(p1, p2):
    return math.sqrt(sum([(a-b)**2 for a, b in zip(p1, p2)]))

def get_smallest():
    sv, si, sj = -1, -1, -1
    for i in range(M):
        for j in range(i+1, M):
            if cir[i] != cir[j]:
                if sv == -1:
                    sv = get_dist(nums[i], nums[j])
                    si, sj = i, j
                else:
                    v = get_dist(nums[i], nums[j])
                    if v < sv:
                        sv, si, sj = v, i, j
    return si, sj

for t in range(T):
    i, j = get_smallest()
    update_cir(i, j)


lens_dict = dict()

for c in cir:
    if c in lens_dict:
        lens_dict[c] += 1
    else:
        lens_dict[c] = 1


lens = [v for v in lens_dict.values()]
lens.sort(reverse=True)

ans = 1
for i in range(TOP):
    ans *= lens[i]

print(f"ans = {ans}")
