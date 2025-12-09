import math

T = 999
TOP = 3

with open('p8/input.txt', 'r') as file:
    lines = file.read().splitlines()
    nums = [[int(n) for n in l.split(",")] for l in lines]

M = len(nums)
cir = list(range(M))

def get_dist(p1, p2):
    return math.sqrt(sum([(a-b)**2 for a, b in zip(p1, p2)]))

def update_cir(p, q):
    v1 = cir[p]
    v2 = cir[q]
    for i in range(len(cir)):
        if cir[i] == v2:
            cir[i] = v1

# Sorting the pairs in ascending order according to there distance in n*log(n) time complexity
pairs = [(i, j) for i in range(M) for j in range(i+1, M)]
pairs = sorted(pairs, key=lambda p: get_dist(nums[p[0]], nums[p[1]]))

# Getting the smallest pair which is not already connected and updating the circuits
i = 0
for t in range(T):
    # This was needed according to the explanation in the question
    # But apparently, not required :(
    # while cir[pairs[i][0]] == cir[pairs[i][1]]:
    #     i += 1
    update_cir(pairs[i][0], pairs[i][1])
    i += 1

# Getting the lens of different circuits and calculating the product of the length of top `TOP` circuits
lens_dict = dict()
for c in cir:
    if c in lens_dict:
        lens_dict[c] += 1
    else:
        lens_dict[c] = 1
lens = sorted(list(lens_dict.values()), reverse=True)
ans = 1
for i in range(TOP):
    ans *= lens[i]

print(f"ans = {ans}")
