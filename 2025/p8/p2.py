import math

with open('p8/input.txt', 'r') as file:
    lines = file.read().splitlines()
    nums = [[int(n) for n in l.split(",")] for l in lines]

M = len(nums)
cir = list(range(M))

def get_dist(p1, p2):
    return math.sqrt(sum([(a-b)**2 for a, b in zip(p1, p2)]))

def is_single_circuit():
    for i in range(1, M):
        if cir[0] != cir[i]:
            return False
    return True

def update_cir(p, q):
    v1 = cir[p]
    v2 = cir[q]
    for i in range(M):
        if cir[i] == v2:
            cir[i] = v1

# Sorting the pairs in ascending order according to there distance in n*log(n) time complexity
pairs = [(i, j) for i in range(M) for j in range(i+1, M)]
pairs = sorted(pairs, key=lambda p: get_dist(nums[p[0]], nums[p[1]]))

# Getting the smallest pair which is not already connected and updating the circuits
i = 0
ans = -1
while True:
    # This was needed according to the explanation in the question
    # But apparently, not required :(
    # while cir[pairs[i][0]] == cir[pairs[i][1]]:
    #     i += 1
    update_cir(pairs[i][0], pairs[i][1])
    if is_single_circuit():
        print(f"Last two pairs are {nums[pairs[i][0]]} and {nums[pairs[i][1]]}")
        ans = nums[pairs[i][0]][0] * nums[pairs[i][1]][0]
        break
    i += 1

print(f"ans = {ans}")
