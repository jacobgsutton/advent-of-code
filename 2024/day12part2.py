from collections import defaultdict

ans = 0
m = open(0).read().splitlines()
r = len(m)
c = len(m[0])

visited = set()
fences = defaultdict(list)

def dfs(x, y, dx, dy, plant):
    if x < 0 or x >= c or y < 0 or y >= r or m[y][x] != plant:
        if dx != 0: fences[('x', x, dx)].append(y)
        else: fences[('y', y, dy)].append(x)
        return 0
    if (x, y) in visited: return 0

    visited.add((x, y))

    area = 1
    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        area += dfs(x+dx, y+dy, dx, dy, plant)
    return area

for i in range(r):
    for j in range(c):
        area = dfs(j, i, 0, 0, m[i][j])
        sides = 0
        for key in fences:
            sides += 1
            sorted_fences = sorted(fences[key])
            prev = sorted_fences[0]
            for fence in sorted_fences[1:]:
                if fence != prev+1:
                    sides += 1
                prev = fence
        ans += area * sides
        fences.clear()
print(ans)