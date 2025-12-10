with open('p9/input.txt', 'r') as file:
    lines = file.read().splitlines()
    nums = [[int(n) for n in l.split(",")] for l in lines]

def get_area(p1, p2):
    return (abs(nums[p1][0] - nums[p2][0]) + 1) * (abs(nums[p1][1] - nums[p2][1]) + 1)

M = len(nums)
pairs = [(i, j) for i in range(M) for j in range(i+1, M)]
pairs = sorted(pairs, key=lambda p: get_area(p[0], p[1]), reverse=True)
p = pairs[0]

print(f"Larges rectangle is made by red tiles at {nums[p[0]]} and {nums[p[1]]} with area {get_area(p[0], p[1])}")
